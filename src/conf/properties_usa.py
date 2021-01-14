from src.conf import constants as c

from enum import Enum
import uuid

CONF = {
    c.REGION_NAME: "USA",

    # DL Paths
    c.DL_PATHS: {
        c.RAW_EVENTS: "C:\\Showcase\\Projekt\\M-HH-showcase-local\\data-lake\\S3_USA_RAW_EVENTS\\CAR\\",
        c.RAW: "C:\\Showcase\\Projekt\\M-HH-showcase-local\\data-lake\\S3_USA_RAW\\CAR\\",
        c.PROCESSED: "C:\\Showcase\\Projekt\\M-HH-showcase-local\\data-lake\\S3_USA_PROCESSED\\CAR\\",
        c.ANALYZED: "C:\\Showcase\\Projekt\\M-HH-showcase-local\\data-lake\\S3_USA_ANALYZED\\CAR\\"
    },
    # Available schemas
    c.SCHEMAS: {
        c.SCHEMA_USA: "src/conf/schemas/schema_usa.json"
    },

    # Kafka Topics
    c.TOPICS: {
        c.TOPIC_RAW: "car-usa",
        c.TOPIC_INFO_CAR: "car-usa-info",
        c.TOPIC_INFO_REGION: "region-usa-info"
    },

    # MongoDB config
    c.DB_NAME: "M-HH-USA",
    c.DB_COLS: {
        c.PROCESSED: "processed",
        c.ANALYZED: "analysis",
        c.ANALYZED_CAR: "analysis_car"
    }
}
