:compass: Python Systems Programming Roadmap
“From CLI utilities → servers → interpreters → distributed systems”

🩵 Stage 1: Command-Line & File I/O (Foundations)
	Learn how Linux tools work internally, file descriptors, streams, and process IO.
:white_check_mark: Goals: stdin/stdout, file reading/writing, pipes, buffering.
:hammer_and_wrench: Projects:
	1. cat — read multiple files, stream to stdout.
	2. wc — count lines, words, bytes.
	3. head / tail — read first or last N lines efficiently.
	4. sort — implement merge sort with stdin/stdout.
	5. uniq — remove duplicate lines.
	6. grep — implement regex matching manually.
	7. find — recursive directory walking.
	8. tee — duplicate stdin to file and stdout.
:mag: Skills: file streams, iterators, buffering, os and io modules, regex, recursion.

:green_heart: Stage 2: Process Control & OS Interaction
	Learn how processes, signals, and threads work.
:white_check_mark: Goals: process creation, signals, environment, pipes.
:hammer_and_wrench: Projects:
	1. ps — list running processes from /proc.
	2. kill — send Unix signals.
	3. xargs — feed stdin lines into new process args.
	4. watch — periodically run a command.
	5. shell — basic shell supporting pipes & redirects (ls | grep py > out.txt).
	6. thread-pool — create your own async executor.
:mag: Skills: subprocess, signal, threading, multiprocessing, OS introspection.

:orange_heart: Stage 3: Networking & Protocols
	Learn sockets, TCP/UDP, HTTP, and concurrency with I/O multiplexing.
:white_check_mark: Goals: socket programming, protocol parsing, network concurrency.
:hammer_and_wrench: Projects:
	1. nc (netcat) — TCP/UDP client and server.
	2. http-server — serve static files over HTTP.
	3. curl — send HTTP requests (GET/POST).
	4. proxy-server — forward HTTP requests with caching.
	5. ping — implement ICMP echo.
	6. dns-resolver — query DNS via UDP.
	7. chat-server — multi-client TCP chat with select/asyncio.
:mag: Skills: socket, asyncio, multiplexing, binary protocols, HTTP headers.

:blue_heart: Stage 4: Databases, Caching & Persistence
	Build small database-like systems to learn indexing, persistence, and transactions.
:white_check_mark: Goals: serialization, indexing, ACID basics, concurrency control.
:hammer_and_wrench: Projects:
	1. kv-store — key-value database with file persistence.
	2. mini-redis — TCP server with SET/GET and in-memory storage.
	3. lru-cache — implement LRU and LFU eviction.
	4. append-log — write-ahead log for durability.
	5. lsm-db — implement Log-Structured Merge tree.
	6. b-tree-index — build and query B-trees.
	7. time-series-db — append-only DB with range queries.
:mag: Skills: memory vs disk trade-offs, indexing, journaling, concurrency.

:purple_heart: Stage 5: Compilers & Interpreters
	Learn language design, lexing, parsing, and execution models.
:white_check_mark: Goals: tokenization, AST, evaluation, REPL loop.
:hammer_and_wrench: Projects:
	1. expr-interpreter — parse and evaluate math expressions.
	2. lisp-eval — implement a small Lisp interpreter.
	3. mini-python — parse Python subset (assignments, loops).
	4. bytecode-runner — execute a small VM instruction set.
	5. regex-engine — implement your own regex matcher.
	6. markdown-parser — convert Markdown to HTML.
:mag: Skills: parsing, ASTs, evaluation, recursive descent, interpreters.

:yellow_heart: Stage 6: Backend & Web Systems
	Learn web backend architecture — routing, middleware, REST, caching, jobs.
:white_check_mark: Goals: HTTP servers, middleware, job queues, caching, rate limiting.
:hammer_and_wrench: Projects:
	1. micro-framework — Flask-like routing and request handling.
	2. session-store — cookie + Redis-backed sessions.
	3. rate-limiter — token bucket or sliding window.
	4. job-scheduler — cron-like delayed task runner.
	5. metrics-server — expose Prometheus metrics via HTTP.
	6. log-aggregator — collect and search logs from multiple services.
:mag: Skills: web protocols, middleware pattern, Redis, scheduling, monitoring.

:heart: Stage 7: Distributed & Scalable Systems
	Advanced level — distributed coordination, replication, consensus.
:white_check_mark: Goals: distributed state, reliability, eventual consistency.
:hammer_and_wrench: Projects:
	1. message-queue — implement pub/sub like RabbitMQ.
	2. raft — distributed consensus algorithm.
	3. leader-election — build a distributed lock manager.
	4. distributed-cache — multi-node consistent hashing.
	5. load-balancer — proxy incoming requests to multiple servers.
	6. replicated-db — simulate leader-follower replication.
	7. container-runtime — lightweight Docker clone using namespaces (Linux-only).
:mag: Skills: distributed coordination, consensus, fault tolerance, OS namespaces, RPCs.

:jigsaw: Stage 8: Tooling & Developer Experience
	Build the tools developers use daily.
:hammer_and_wrench: Projects:
	1. git-lite — version control system (Codecrafters-style).
	2. build-system — like make or ninja, track dependencies.
	3. package-manager — install packages from registry (like pip).
	4. formatter — Python/JSON/YAML formatter.
	5. static-analyzer — find syntax errors or lint code.
:mag: Skills: hashing, dependency graphs, AST analysis, CLI UX.
