from enum import Enum
from typing import Type
from .api import (
    VectorDB,
    DBConfig,
    DBCaseConfig,
    EmptyDBCaseConfig,
    IndexType,
    MetricType,
)

from .milvus.milvus import Milvus
from .elastic_cloud.elastic_cloud import ElasticCloud
from .pinecone.pinecone import Pinecone
from .weaviate_cloud.weaviate_cloud import WeaviateCloud
from .qdrant_cloud.qdrant_cloud import QdrantCloud
from .zilliz_cloud.zilliz_cloud import ZillizCloud
from .pgvector.pgvector import PgVector
from .redis.redis import Redis
from .chroma.chroma import ChromaClient
from .lancedb.lancedb import LanceDB
from .lancedb_cloud.lancedb_cloud import LanceDBCloud

class DB(Enum):
    """Database types

    Examples:
        >>> DB.Milvus
        <DB.Milvus: 'Milvus'>
        >>> DB.Milvus.value
        "Milvus"
        >>> DB.Milvus.name
        "Milvus"
    """

    Milvus = "Milvus"
    ZillizCloud = "ZillizCloud"
    Pinecone = "Pinecone"
    ElasticCloud = "ElasticCloud"
    QdrantCloud = "QdrantCloud"
    WeaviateCloud = "WeaviateCloud"
    PgVector = "PgVector"
    Redis = "Redis"
    Chroma = "Chroma"
    LanceDB = "LanceDB"
    LanceDBCloud = "LanceDBCloud"


    @property
    def init_cls(self) -> Type[VectorDB]:
        return db2client.get(self)


db2client = {
    DB.Milvus: Milvus,
    DB.ZillizCloud: ZillizCloud,
    DB.WeaviateCloud: WeaviateCloud,
    DB.ElasticCloud: ElasticCloud,
    DB.QdrantCloud: QdrantCloud,
    DB.Pinecone: Pinecone,
    DB.PgVector: PgVector,
    DB.Redis: Redis,
    DB.Chroma: ChromaClient,
    DB.LanceDB: LanceDB,
    DB.LanceDBCloud: LanceDBCloud,
}

for db in DB:
    assert issubclass(db.init_cls, VectorDB)


__all__ = [
    "DB", "VectorDB", "DBConfig", "DBCaseConfig", "IndexType", "MetricType", "EmptyDBCaseConfig",
]
