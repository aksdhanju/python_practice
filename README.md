# 🧭 Python Systems Programming Roadmap
**From CLI utilities → servers → interpreters → distributed systems**

---

## 🩵 Stage 1: Command-Line & File I/O (Foundations)

Learn how Linux tools work internally, file descriptors, streams, and process I/O.

**Goals**
- stdin / stdout
- File reading & writing
- Pipes and buffering

**Projects**
1. `cat` — read multiple files, stream to stdout
2. `wc` — count lines, words, bytes
3. `head` / `tail` — read first or last N lines efficiently
4. `sort` — implement merge sort with stdin/stdout
5. `uniq` — remove duplicate lines
6. `grep` — implement regex matching manually
7. `find` — recursive directory walking
8. `tee` — duplicate stdin to file and stdout

**Skills**
- File streams
- Iterators
- Buffering
- `os` and `io` modules
- Regex
- Recursion

---

## 💚 Stage 2: Process Control & OS Interaction

Learn how processes, signals, and threads work.

**Goals**
- Process creation
- Signals
- Environment variables
- Pipes

**Projects**
1. `ps` — list running processes from `/proc`
2. `kill` — send Unix signals
3. `xargs` — feed stdin lines into new process args
4. `watch` — periodically run a command
5. `shell` — basic shell supporting pipes & redirects  
   (`ls | grep py > out.txt`)
6. `thread-pool` — create your own async executor

**Skills**
- `subprocess`
- `signal`
- `threading`
- `multiprocessing`
- OS introspection

---

## 🧡 Stage 3: Networking & Protocols

Learn sockets, TCP/UDP, HTTP, and concurrency with I/O multiplexing.

**Goals**
- Socket programming
- Protocol parsing
- Network concurrency

**Projects**
1. `nc` (netcat) — TCP/UDP client and server
2. `http-server` — serve static files over HTTP
3. `curl` — send HTTP requests (GET/POST)
4. `proxy-server` — forward HTTP requests with caching
5. `ping` — implement ICMP echo
6. `dns-resolver` — query DNS via UDP
7. `chat-server` — multi-client TCP chat with `select` / `asyncio`

**Skills**
- `socket`
- `asyncio`
- I/O multiplexing
- Binary protocols
- HTTP headers

---

## 💙 Stage 4: Databases, Caching & Persistence

Build database-like systems to learn indexing, persistence, and transactions.

**Goals**
- Serialization
- Indexing
- ACID basics
- Concurrency control

**Projects**
1. `kv-store` — key-value DB with file persistence
2. `mini-redis` — TCP server with SET/GET
3. `lru-cache` — LRU and LFU eviction
4. `append-log` — write-ahead log
5. `lsm-db` — Log-Structured Merge Tree
6. `b-tree-index` — B-Tree implementation
7. `time-series-db` — append-only DB with range queries

**Skills**
- Memory vs disk trade-offs
- Indexing
- Journaling
- Concurrency

---

## 💜 Stage 5: Compilers & Interpreters

Learn language design, lexing, parsing, and execution models.

**Goals**
- Tokenization
- AST
- Evaluation
- REPL loops

**Projects**
1. `expr-interpreter` — math expressions
2. `lisp-eval` — Lisp interpreter
3. `mini-python` — Python subset parser
4. `bytecode-runner` — small VM
5. `regex-engine` — regex matcher
6. `markdown-parser` — Markdown → HTML

**Skills**
- Parsing
- ASTs
- Recursive descent
- Interpreters

---

## 💛 Stage 6: Backend & Web Systems

Learn web backend architecture.

**Goals**
- HTTP servers
- Middleware
- Job queues
- Caching
- Rate limiting

**Projects**
1. `micro-framework` — Flask-like framework
2. `session-store` — Redis-backed sessions
3. `rate-limiter` — token bucket / sliding window
4. `job-scheduler` — cron-like task runner
5. `metrics-server` — Prometheus metrics
6. `log-aggregator` — centralized logging

**Skills**
- Web protocols
- Middleware patterns
- Redis
- Monitoring

---

## ❤️ Stage 7: Distributed & Scalable Systems

Advanced distributed systems concepts.

**Goals**
- Distributed state
- Reliability
- Eventual consistency

**Projects**
1. `message-queue` — pub/sub system
2. `raft` — consensus algorithm
3. `leader-election` — distributed locks
4. `distributed-cache` — consistent hashing
5. `load-balancer` — request proxy
6. `replicated-db` — leader-follower replication
7. `container-runtime` — Docker-lite (Linux)

**Skills**
- Consensus
- Fault tolerance
- OS namespaces
- RPCs

---

## 🧩 Stage 8: Tooling & Developer Experience

Build developer tools.

**Projects**
1. `git-lite` — version control system
2. `build-system` — make/ninja-style builder
3. `package-manager` — pip-like installer
4. `formatter` — Python/JSON/YAML formatter
5. `static-analyzer` — syntax & lint analysis

**Skills**
- Hashing
- Dependency graphs
- AST analysis
- CLI UX
