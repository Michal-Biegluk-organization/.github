## 2024-07-11 - Optimize External API Calls with Caching

**Learning:** External API calls, even for assets like images, can be a performance bottleneck. The `github-readme-stats` service allows for a `cache_seconds` parameter, which can significantly improve load times for repeat visitors by leveraging browser caching.

**Action:** When encountering external media or API calls in the future, investigate if the service provides caching parameters. A simple change can lead to a measurable performance improvement with minimal effort.
## 2024-07-11 - CI Workflow Consolidation
**Learning:** In repositories that are purely static or documentation-based (like a GitHub Profile README), performance wins can be found in the CI/CD pipeline. Consolidating small, single-purpose jobs into larger ones reduces the overhead of starting multiple GitHub Actions runners, which is a measurable improvement in developer experience and resource usage.
**Action:** Always check the .github/workflows directory for multi-job pipelines that could be combined to save time and resources.
