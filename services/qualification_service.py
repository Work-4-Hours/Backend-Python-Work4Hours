from sqlalchemy.sql import text
from schemas import Qualification as QualificationSchema
from models.Qualification import Qualification
from utils.db import get_session

class QualificationService:

    @classmethod
    def add_qualification(cls, qualif_info: QualificationSchema) -> True or None:
        with get_session() as session:
            prevQualification = session.execute(session.query(Qualification).filter(Qualification.serviceid == qualif_info.serviceid).filter(Qualification.userId == qualif_info.userId))
            isQualified = bool(prevQualification.scalars().first())
            if (not isQualified):
                newQualification = Qualification(**qualif_info.dict())
                session.add(newQualification)
                session.commit()
                return True
            else:
                session.execute(text("UPDATE qualification SET qualification = :qualification WHERE userId = :userId and serviceid = :serviceid").bindparams(
                    userId = qualif_info.userId,
                    serviceid = qualif_info.serviceid,
                    qualification = qualif_info.qualification
                ))
                session.commit()
                return None

