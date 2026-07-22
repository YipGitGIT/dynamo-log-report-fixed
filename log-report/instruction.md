Analyze the Apache-style access log at `/app/access.log` and write a summary to
`/app/report.json`.

Success criteria:

1. `/app/report.json` is a valid JSON object containing exactly the keys
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is an integer equal to the number of non-empty log entries.
3. `unique_ips` is an integer equal to the number of distinct client IP addresses,
   using the first whitespace-delimited field of each non-empty entry.
4. `top_path` is a string containing the request path that occurs most often in the
   quoted HTTP request lines.
