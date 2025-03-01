WITH RECURSIVE dayly_procecess_hackers AS(
	SELECT submission_date, hacker_id
	FROM public."Submissions"
	GROUP BY submission_date, hacker_id
)
SELECT 
    sb.submission_date,
    (
		SELECT COUNT(hacker_id)
		FROM public."Hackers" AS sub1_h
		WHERE sub1_h.hacker_id IN(
	        SELECT dph.hacker_id
	        FROM dayly_procecess_hackers AS dph
	        WHERE dph.submission_date BETWEEN DATE '2016-03-01' AND sb.submission_date
	        GROUP BY dph.hacker_id
	        HAVING COUNT(dph.submission_date) = (sb.submission_date - DATE '2016-03-01' )+ 1
		)
    ) AS daily_active_hackers,
    (
        SELECT sub2_sb.hacker_id
        FROM public."Submissions" AS sub2_sb 
        WHERE sub2_sb.submission_date = sb.submission_date
        GROUP BY sub2_sb.hacker_id
        ORDER BY COUNT(sub2_sb.submission_id) DESC, sub2_sb.hacker_id
        LIMIT 1
    ) AS max_hacker_id,
    (
        SELECT sub3_h.name
        FROM public."Submissions" AS sub3_sb 
        INNER JOIN public."Hackers" AS sub3_h 
        ON sub3_sb.hacker_id = sub3_h.hacker_id
        WHERE sub3_sb.submission_date = sb.submission_date
        GROUP BY sub3_h.hacker_id, sub3_h.name
        ORDER BY COUNT(sub3_sb.submission_id) DESC, sub3_h.hacker_id
        LIMIT 1
    ) AS hacker_name
 
FROM public."Submissions" AS sb
GROUP BY sb.submission_date
ORDER BY sb.submission_date;
