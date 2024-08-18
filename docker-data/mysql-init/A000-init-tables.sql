CREATE TABLE IF NOT EXISTS datacenter
(
    datacenter_id   BINARY(16)   DEFAULT (UUID_TO_BIN(UUID(), TRUE)) NOT NULL
        PRIMARY KEY,
    datacenter_name VARCHAR(64)                                      NOT NULL,
    code            VARCHAR(8)                                       NOT NULL,
    description     VARCHAR(256)                                     NULL,
    created_on      DATETIME     DEFAULT CURRENT_TIMESTAMP           NOT NULL,
    created_by      VARCHAR(128) DEFAULT 'system'                    NOT NULL,
    updated_on      DATETIME                                         NULL,
    updated_by      VARCHAR(128)                                     NULL,
    CONSTRAINT uix_datacenter_code
        UNIQUE (code),
    CONSTRAINT uix_datacenter_name
        UNIQUE (datacenter_name)
);