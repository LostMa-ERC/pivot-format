# 1. Download Heurist data

First things first, run the `lostma heurist` command to download / refresh your downloaded Heurist data.

Everything about this workflow is local and designed to keep you up to date. So you personally need to have the data files downloaded on your machine. They're not installed with this project.

```console
$ lostma heurist
```

If you don't want to set up a `.env` file, you can still download the Heurist data by passing your username and password as options.

```console
$ lostma heurist --login "user.name" --password "pass"
```

---
[<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M9.195 18.44c1.25.714 2.805-.189 2.805-1.629v-2.34l6.945 3.968c1.25.715 2.805-.188 2.805-1.628V8.69c0-1.44-1.555-2.343-2.805-1.628L12 11.029v-2.34c0-1.44-1.555-2.343-2.805-1.628l-7.108 4.061c-1.26.72-1.26 2.536 0 3.256l7.108 4.061Z" />
</svg>
**Back**
](./configure_project.md) |
[**Next** <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M5.055 7.06C3.805 6.347 2.25 7.25 2.25 8.69v8.122c0 1.44 1.555 2.343 2.805 1.628L12 14.471v2.34c0 1.44 1.555 2.343 2.805 1.628l7.108-4.061c1.26-.72 1.26-2.536 0-3.256l-7.108-4.061C13.555 6.346 12 7.249 12 8.689v2.34L5.055 7.061Z" />
</svg>
](./transform_into_graph.md)
