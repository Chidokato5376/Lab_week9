from sqlmodel import SQLModel, Field, Relationship

# ==========================
# CÁC MODEL DÀNH CHO TEAM
# ==========================
class TeamBase(SQLModel):
    name: str = Field(index=True, unique=True)
    headquarters: str

class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list["Hero"] = Relationship(back_populates="team")

class TeamCreate(TeamBase):
    pass

class TeamPublic(TeamBase):
    id: int

# ==========================
# BẢNG TRUNG GIAN (N-N)
# ==========================
class HeroMissionLink(SQLModel, table=True):
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
    mission_id: int | None = Field(default=None, foreign_key="mission.id", primary_key=True)

# ==========================
# CÁC MODEL DÀNH CHO HERO
# ==========================
class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    # Thêm trường power theo yêu cầu Task 9.1
    power: str | None = None

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    team: Team | None = Relationship(back_populates="heroes")
    missions: list["Mission"] = Relationship(back_populates="heroes", link_model=HeroMissionLink)

class HeroCreate(HeroBase):
    secret_name: str

class HeroPublic(HeroBase):
    id: int

class HeroUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    team_id: int | None = None
    secret_name: str | None = None
    # Thêm trường power vào HeroUpdate
    power: str | None = None

# ==========================
# CÁC MODEL DÀNH CHO MISSION
# ==========================
class MissionBase(SQLModel):
    title: str

class Mission(MissionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list["Hero"] = Relationship(back_populates="missions", link_model=HeroMissionLink)

class MissionCreate(MissionBase):
    pass

class MissionPublic(MissionBase):
    id: int