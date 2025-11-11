CREATE TABLE "users" (
  "id" uuid PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "password" text,
  "created_at" timestamp DEFAULT 'now()',
  "updated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "places" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "descreption" text,
  "location" text,
  "features" text,
  "created_at" timestamp DEFAULT 'now()',
  "updated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "favotite" (
  "id" integer PRIMARY KEY,
  "user_id" uuid,
  "place_id" uuid,
  "created_at" timestamp DEFAULT 'now()',
  "updated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "recommended" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "descreption" text,
  "location" text,
  "features" text,
  "place_id" uuid,
  "created_at" timestamp DEFAULT 'now()',
  "updated_at" timestamp DEFAULT 'now()'
);

ALTER TABLE "favotite" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "favotite" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");

ALTER TABLE "recommended" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");