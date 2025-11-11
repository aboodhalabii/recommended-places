from sqlalchemy import MetaData, Table, Column, SERIAL, Text,Datetime,ENUM

from enum import Enum



users_table = Table(
        "users",MetaData,
        Column("id", uuid, primary_key=True),
        Column("username", Text, nullable=False, unique=True),
        Column("email", Text, unique=True),
        Column("password_hash" ,default=True),
        Column("created_at",Datetime),
        Column("updated_at",Datetime)

    )

places = Table(
        "places",MetaData,
        Column("id", uuid, primary_key=True),
        Column("name", Text, nullable=False, unique=True),
        Column("description", Text, unique=True),
        Column("location" Text,),
        Column("created_at",Datetime),
        Column("updated_at",Datetime),
        Column(
            
        ),

    )
favorites = Table(
        "favorites",MetaData,
        Column("id", uuid, primary_key=True),
        Column("user_id", uuid, nullable=False, unique=True),
        Column("place_id", uuid, unique=True),
        Column("created_at",Datetime),
        Column("updated_at",Datetime),
        Column(
            
        ),
    )
    

 recommended = Table(
        "recommended",MetaData,
        Column("id", uuid, primary_key=True),
        Column("name", Text, nullable=False, unique=True),
        Column("description", Text, unique=True),
        Column("location" Text,),
        Column("created_at",Datetime),
        Column("updated_at",Datetime),
        
),

    