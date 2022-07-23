-- Table: public.todos

-- DROP TABLE IF EXISTS public.todos;

CREATE TABLE IF NOT EXISTS public.todos
(
    todo_id integer NOT NULL DEFAULT nextval('todos_todo_id_seq'::regclass),
    todo_title text COLLATE pg_catalog."default" NOT NULL,
    todo_description text COLLATE pg_catalog."default" NOT NULL,
    priority numeric,
    status numeric(1,0) NOT NULL DEFAULT 0,
    create_at timestamp with time zone NOT NULL DEFAULT now(),
    update_at timestamp with time zone NOT NULL DEFAULT now(),
    CONSTRAINT todos_pkey PRIMARY KEY (todo_id),
    CONSTRAINT todos_priority_check CHECK (priority <= 3::numeric)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.todos
    OWNER to aplikacja;
