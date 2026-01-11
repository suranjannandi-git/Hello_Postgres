CREATE TABLE public.candidate_metadata (
    candidate_id VARCHAR(255) NOT NULL,
    candidate_name VARCHAR(255),
    skills TEXT,
    experience VARCHAR(50),
    requestor_email VARCHAR(255),
    resume_uri TEXT,
    job_role VARCHAR(255),
    genai_evaluation_status VARCHAR(50),
    email_response_sent VARCHAR(10),
    qna_uri TEXT,
    evaluation_uri TEXT
);

INSERT INTO public.candidate_metadata
(candidate_id)
VALUES('ID001');

delete from public.candidate_metadata

Update public.candidate_metadata
SET candidate_name = 'Kiran Kumar',
    skills = 'Engineering',
    experience = '2 years',
    requestor_email = 'none@in.ibm.com'
WHERE candidate_id = 'ID001';

SELECT * FROM public.candidate_metadata;
