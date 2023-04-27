--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';

--
-- Name: w22; Type: TABLE; Schema: public; Owner: weboll; Tablespace:
--
CREATE OR REPLACE FUNCTION public.w22_numero_bollettino()
 RETURNS character varying
 LANGUAGE plpgsql
AS $function$
BEGIN
  RETURN
  (SELECT COUNT(data_emissione) + 1 || '/' || date_part('year', current_date)
  FROM w22
  WHERE data_emissione >= date_trunc('year', current_date) AND data_emissione < current_date);

END;
$function$
;


CREATE TABLE public.w22 (
    id_w22 bigint NOT NULL,
    data_emissione date DEFAULT ('now'::text)::date NOT NULL,
    ora_emissione character varying(5) NOT NULL,
    data_validita date NOT NULL,
    numero_bollettino character varying(30) DEFAULT public.w22_numero_bollettino() NOT NULL,
    annotazione text,
    situazione_evoluzione text,
    status character(1) DEFAULT 0 NOT NULL,
    pdf_ordinario character(1) DEFAULT '0' NOT NULL,
    last_update timestamp(0) without time zone DEFAULT ('now'::text)::timestamp(6) with time zone NOT NULL,
    username character varying(30) DEFAULT "current_user"() NOT NULL,
    validita character varying(50) DEFAULT '24 ore'::character varying
);

alter table public.w22 alter column pdf_ordinario set default '1';

ALTER TABLE public.w22 OWNER TO weboll;

--
-- Name: COLUMN w22.status; Type: COMMENT; Schema: public; Owner: weboll
--

COMMENT ON COLUMN public.w22.status IS '0 = Draft; 1 = Final';


--
-- Name: w22_id_w22_seq; Type: SEQUENCE; Schema: public; Owner: weboll
--

CREATE SEQUENCE public.w22_id_w22_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.w22_id_w22_seq OWNER TO weboll;

--
-- Name: w22_id_w22_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: weboll
--

ALTER SEQUENCE public.w22_id_w22_seq OWNED BY public.w22.id_w22;


--
-- Name: id_w22; Type: DEFAULT; Schema: public; Owner: weboll
--

ALTER TABLE ONLY public.w22 ALTER COLUMN id_w22 SET DEFAULT nextval('public.w22_id_w22_seq'::regclass);


--
-- Name: w23_pkey; Type: CONSTRAINT; Schema: public; Owner: weboll; Tablespace:
--

ALTER TABLE ONLY public.w22
    ADD CONSTRAINT w22_pkey PRIMARY KEY (id_w22);


--
-- Data for Name: w22; Type: TABLE DATA; Schema: public; Owner: weboll
--

COPY public.w22 (id_w22, data_emissione, ora_emissione, data_validita, numero_bollettino, annotazione, situazione_evoluzione, status, pdf_ordinario, last_update, username, validita) FROM stdin;
2077	2023-02-14	12:00	2023-02-15	23/2023	\N	\N	1	1	2022-02-03 12:08:33	weboll	36 ore
2078	2023-02-15	12:00	2023-02-18	24/2023	\N	\N	1	1	2022-02-04 12:07:38	weboll	36 ore
2079	2023-02-18	12:00	2023-02-19	25/2023	\N	\N	1	1	2022-02-07 12:03:16	weboll	36 ore
2080	2023-02-19	12:00	2023-02-20	26/2023	\N	\N	1	1	2022-02-08 12:03:55	weboll	36 ore
2081	2023-02-20	12:00	2023-02-21	27/2023	\N	\N	1	1	2022-02-09 12:07:14	weboll	36 ore
\.

--
-- Name: w22_id_w22_seq; Type: SEQUENCE SET; Schema: public; Owner: weboll
--

SELECT pg_catalog.setval('public.w22_id_w22_seq', 2081, true);


--
-- Name: w22_pkey; Type: CONSTRAINT; Schema: public; Owner: weboll; Tablespace:
--


--
-- Name: TABLE w22; Type: ACL; Schema: public; Owner: weboll
--



--
-- Name: SEQUENCE w22_id_w22_seq; Type: ACL; Schema: public; Owner: weboll
--



--
-- PostgreSQL database dump complete
--
