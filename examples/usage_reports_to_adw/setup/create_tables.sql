
-------------------------------
-- OCI_USAGE
-------------------------------
create table OCI_USAGE (
    TENANT_NAME             VARCHAR2(100),
    TENANT_ID               VARCHAR2(100),
    FILE_ID                 VARCHAR2(30),
    USAGE_INTERVAL_START    DATE,
    USAGE_INTERVAL_END      DATE,
    PRD_SERVICE             VARCHAR2(100),
    PRD_RESOURCE            VARCHAR2(100),
    PRD_COMPARTMENT_ID      VARCHAR2(100),
    PRD_COMPARTMENT_NAME    VARCHAR2(100),
    PRD_COMPARTMENT_PATH    VARCHAR2(1000),
    PRD_REGION              VARCHAR2(100),
    PRD_AVAILABILITY_DOMAIN VARCHAR2(100),
    USG_RESOURCE_ID         VARCHAR2(1000),
    USG_BILLED_QUANTITY     NUMBER,
    USG_CONSUMED_QUANTITY   NUMBER,
    USG_CONSUMED_UNITS      VARCHAR2(100),
    USG_CONSUMED_MEASURE    VARCHAR2(100),
    IS_CORRECTION           VARCHAR2(10),
    TAGS_DATA               VARCHAR2(4000),
    TAG_SPECIAL             VARCHAR2(4000),
    TAG_SPECIAL2            VARCHAR2(4000)
) COMPRESS;

CREATE INDEX OCI_USAGE_1IX ON OCI_USAGE(TENANT_NAME,USAGE_INTERVAL_START);

-------------------------------
-- OCI_USAGE_TAG_KEYS
-------------------------------
CREATE TABLE OCI_USAGE_TAG_KEYS (
    TENANT_NAME VARCHAR2(100),
    TAG_KEY VARCHAR2(100),
    CONSTRAINT OCI_USAGE_TAG_KEYS_PK PRIMARY KEY(TENANT_NAME,TAG_KEY)
);

-------------------------------
-- OCI_USAGE_TAG_KEYS
-------------------------------
CREATE TABLE OCI_USAGE_STATS (
    TENANT_NAME             VARCHAR2(100),
    FILE_ID                 VARCHAR2(30),
    USAGE_INTERVAL_START    DATE,
    NUM_ROWS                NUMBER,
    UPDATE_DATE             DATE,
    AGENT_VERSION           VARCHAR2(30),
    CONSTRAINT OCI_USAGE_STATS_PK PRIMARY KEY (TENANT_NAME,FILE_ID,USAGE_INTERVAL_START)
);

-------------------------------
-- OCI_COST
-------------------------------
create table OCI_COST (
    TENANT_NAME             VARCHAR2(100),
    TENANT_ID               VARCHAR2(100),
    FILE_ID                 VARCHAR2(30),
    USAGE_INTERVAL_START    DATE,
    USAGE_INTERVAL_END      DATE,
    PRD_SERVICE             VARCHAR2(100),
    PRD_RESOURCE            VARCHAR2(100),
    PRD_COMPARTMENT_ID      VARCHAR2(100),
    PRD_COMPARTMENT_NAME    VARCHAR2(100),
    PRD_COMPARTMENT_PATH    VARCHAR2(1000),
    PRD_REGION              VARCHAR2(100),
    PRD_AVAILABILITY_DOMAIN VARCHAR2(100),
    USG_RESOURCE_ID         VARCHAR2(1000),
    USG_BILLED_QUANTITY     NUMBER,
    USG_BILLED_QUANTITY_OVERAGE NUMBER,
    COST_SUBSCRIPTION_ID    NUMBER,
    COST_PRODUCT_SKU        VARCHAR2(10),
    PRD_DESCRIPTION         VARCHAR2(1000),
    COST_UNIT_PRICE         NUMBER,
    COST_UNIT_PRICE_OVERAGE NUMBER,
    COST_MY_COST            NUMBER,
    COST_MY_COST_OVERAGE    NUMBER,
    COST_CURRENCY_CODE      VARCHAR2(10),
    COST_BILLING_UNIT       VARCHAR2(1000),
    COST_OVERAGE_FLAG       VARCHAR2(10),
    IS_CORRECTION           VARCHAR2(10),
    TAGS_DATA               VARCHAR2(4000),
    TAG_SPECIAL             VARCHAR2(4000),
    TAG_SPECIAL2            VARCHAR2(4000)
) COMPRESS;

CREATE INDEX OCI_COST_1IX ON OCI_COST(TENANT_NAME,USAGE_INTERVAL_START);

-------------------------------
-- OCI_COST_TAG_KEYS
-------------------------------
CREATE TABLE OCI_COST_TAG_KEYS (TENANT_NAME VARCHAR2(100), TAG_KEY VARCHAR2(100),
    CONSTRAINT OCI_COST_TAG_KEYS_PK PRIMARY KEY(TENANT_NAME,TAG_KEY)
);

-------------------------------
-- OCI_COST_STATS
-------------------------------
CREATE TABLE OCI_COST_STATS (
    TENANT_NAME             VARCHAR2(100),
    FILE_ID                 VARCHAR2(30),
    USAGE_INTERVAL_START    DATE,
    NUM_ROWS                NUMBER,
    COST_MY_COST            NUMBER,
    COST_MY_COST_OVERAGE    NUMBER,
    COST_CURRENCY_CODE      VARCHAR2(30),
    UPDATE_DATE             DATE,
    AGENT_VERSION           VARCHAR2(30),
    CONSTRAINT OCI_COST_STATS_PK PRIMARY KEY (TENANT_NAME,FILE_ID,USAGE_INTERVAL_START)
);

-------------------------------
-- OCI_COST_REFERENCE
-------------------------------
CREATE TABLE OCI_COST_REFERENCE (
    TENANT_NAME             VARCHAR2(100),
    REF_TYPE                VARCHAR2(100),
    REF_NAME                VARCHAR2(1000),
    CONSTRAINT OCI_REFERENCE_PK PRIMARY KEY (TENANT_NAME,REF_TYPE,REF_NAME)
) ;

-------------------------------
-- OCI_PRICE_LIST
-------------------------------
create table OCI_PRICE_LIST (
    TENANT_NAME             VARCHAR2(100),
    TENANT_ID               VARCHAR2(100),
    COST_PRODUCT_SKU        VARCHAR2(10),
    PRD_DESCRIPTION         VARCHAR2(1000),
    COST_CURRENCY_CODE      VARCHAR2(10),
    COST_UNIT_PRICE         NUMBER,
    COST_LAST_UPDATE        DATE,
    RATE_DESCRIPTION        VARCHAR2(1000),
    RATE_PAYGO_PRICE        NUMBER,
    RATE_MONTHLY_FLEX_PRICE NUMBER,
    RATE_UPDATE_DATE        DATE,
    CONSTRAINT OCI_PRICE_LIST_PK PRIMARY KEY (TENANT_NAME,TENANT_ID,COST_PRODUCT_SKU)
);

-------------------------------
-- OCI_INTERNAL_COST
-------------------------------
create table OCI_INTERNAL_COST (
    RESOURCE_NAME       varchar2(100) NOT NULL,
    SERVICE_NAME        varchar2(100),
    BILLED_USAGE_UNIT   varchar2(100),
    UNIT_COST           NUMBER,
    CONSTRAINT OCI_INTERNAL_COST_PK PRIMARY KEY (RESOURCE_NAME) USING INDEX ENABLE
);

-------------------------------
-- OCI_LOAD_STATUS
-------------------------------
create table OCI_LOAD_STATUS (
    TENANT_NAME      varchar2(100) NOT NULL,
    FILE_TYPE        varchar2(100) NOT NULL,
    FILE_ID          varchar2(1000) NOT NULL,
    FILE_NAME        varchar2(1000) NOT NULL,
    FILE_DATE        DATE,
    FILE_SIZE        number,
    NUM_ROWS         number,
    LOAD_START_TIME  DATE,
    LOAD_END_TIME    DATE,
    AGENT_VERSION    varchar2(100),
    BATCH_ID         number,
    BATCH_TOTAL      number,
    CONSTRAINT OCI_LOAD_STATUS PRIMARY KEY (TENANT_NAME, FILE_NAME) USING INDEX ENABLE
);

