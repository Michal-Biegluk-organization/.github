## 2024-07-11 - Optimize External API Calls with Caching

**Learning:** External API calls, even for assets like images, can be a performance bottleneck. The `github-readme-stats` service allows for a `cache_seconds` parameter, which can significantly improve load times for repeat visitors by leveraging browser caching.

**Action:** When encountering external media or API calls in the future, investigate if the service provides caching parameters. A simple change can lead to a measurable performance improvement with minimal effort.
## 2026-02-03 - Optimize CI Workflows by Using Native GitHub Context

**Learning:** Redundant jobs in GitHub Actions that only serve to fetch branch names or basic environment info can be eliminated by using native GitHub context variables like `github.head_ref`. This reduces job overhead and saves runner time.

**Action:** Always check if a 'setup' job can be consolidated into its dependent jobs by leveraging built-in GitHub Action context variables.
