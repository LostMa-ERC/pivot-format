# 2. Transform into graph

Because LostMa's data is so networked, a graph is the most intuitive way to structure it for analysis. In preparation for any future work (pivot to TEI documents, explore the network), use the command `lostma build graph` to transform and save the downloaded Heurist data in an embedded, in-process Kùzu graph database.

```console
$ lostma build graph
```

The graph database's files will be located in the directory indicated in the [`config.yml`](./config.yml) file, specifically the key `graph database`.

```yaml
file paths:
  heurist database: heurist.db
  graph database: kuzu_db
```

None of these files are human-readable (they're in binary), but Kùzu understands them. Don't manually add or change anything in the graph database directory.

---
[<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M9.195 18.44c1.25.714 2.805-.189 2.805-1.629v-2.34l6.945 3.968c1.25.715 2.805-.188 2.805-1.628V8.69c0-1.44-1.555-2.343-2.805-1.628L12 11.029v-2.34c0-1.44-1.555-2.343-2.805-1.628l-7.108 4.061c-1.26.72-1.26 2.536 0 3.256l7.108 4.061Z" />
</svg>
**Back**
](./download_heurist_data.md) |
[**Next** <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M5.055 7.06C3.805 6.347 2.25 7.25 2.25 8.69v8.122c0 1.44 1.555 2.343 2.805 1.628L12 14.471v2.34c0 1.44 1.555 2.343 2.805 1.628l7.108-4.061c1.26-.72 1.26-2.536 0-3.256l-7.108-4.061C13.555 6.346 12 7.249 12 8.689v2.34L5.055 7.061Z" />
</svg>
](./explore_network.md)