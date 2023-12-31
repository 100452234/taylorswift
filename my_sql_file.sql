CREATE TABLE ARTIST(
  NAME VARCHAR2(50),
  INFO VARCHAR2(500),
  CONSTRAINT PK_ARTIST PRIMARY KEY (NAME)
);

CREATE TABLE CONCERT(
    CITY VARCHAR2(50),
    COUNTRY VARCHAR2(50),
    VENUE VARCHAR2(50),
    TICKET_SOLD INT(5),
    TICKET_AVAILABLE INT(5),
    REVENUE FLOAT(4),
    TOUR_NAME VARCHAR2(50)
);

// MULTIPLE OPENING ACT?
// ATTENDANCE: TICKET_SOLD / TICKET_AVAILABLE
// AVG TICKET PRICE: REVENUE / TICKET_SOLD
