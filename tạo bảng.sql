CREATE TABLE commands (
    id SERIAL PRIMARY KEY,

    computer_id INTEGER NOT NULL,

    command VARCHAR(100) NOT NULL,

    status VARCHAR(20) DEFAULT 'Pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    executed_at TIMESTAMP,

    CONSTRAINT fk_computer
        FOREIGN KEY (computer_id)
        REFERENCES computers(id)
        ON DELETE CASCADE
);