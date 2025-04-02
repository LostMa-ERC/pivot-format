# 3b. Pivot data to TEI

Run the `lostma pivot` command of this package to select all the texts loaded into the DuckDB database and transform them into TEI-XML documents. The documents will be written in the `output directory` folder you specified in the [`config.yml`](./config.yml) file.

```console
$ lostma pivot
Writing text documents... ━━━━━━━━━━━━━━━━━━━ 0:00:14 517/517
```

The command writes TEI-XML documents to sub-folders, organised by language, in the output directory specified in the config YAML file.

```
output/
|___dum/
|   |___text_46303.xml
|   |___text_46316.xml
|___frm/
|   |___text_557.xml
|   |___text_589.xml
|   |___text_590.xml
|   |___text_603.xml
```

---
[<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M9.195 18.44c1.25.714 2.805-.189 2.805-1.629v-2.34l6.945 3.968c1.25.715 2.805-.188 2.805-1.628V8.69c0-1.44-1.555-2.343-2.805-1.628L12 11.029v-2.34c0-1.44-1.555-2.343-2.805-1.628l-7.108 4.061c-1.26.72-1.26 2.536 0 3.256l7.108 4.061Z" />
</svg>
**Back**
](./transform_into_graph.md)
