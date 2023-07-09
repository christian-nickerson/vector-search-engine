import strawberry
from fastapi import FastAPI, Response, status
from strawberry.fastapi import GraphQLRouter

from src.config import settings
from src.database.engine import connect
from src.database.models import create_tables
from src.graphql.core import Mutation, Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_route = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_route, prefix="/graphql")


@app.on_event("startup")
def build_tables() -> None:
    """create vector db tables"""
    conn = connect(
        host=settings.db.host,
        port=settings.db.port,
        username=settings.db.username,
        password=settings.db.password,
        database=settings.db.database,
    )
    create_tables(conn)


@app.get("/health")
def health_check() -> Response:
    """container health check endpoint"""
    return Response(status_code=status.HTTP_200_OK)
