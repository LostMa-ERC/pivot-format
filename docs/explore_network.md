# 3a. Explore network

The `lostma graph build` command transforms the downloaded Heurist data into an embedded Kùzu graph database.

A convenient way to explore this network is with [Kùzu Explorer](https://docs.kuzudb.com/visualization/). To take advantage of this, do the following:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or some other [Docker](https://docs.docker.com/get-started/get-docker/) installation) and start the program. Docker needs to be running in the background for this to work.

2. Run the command `lostma explorer`.

```console
$ lostma explorer
[09:54:31.198] INFO (1): Access mode: READ_ONLY
[09:54:31.655] INFO (1): Version of Kuzu: 0.8.2
[09:54:31.656] INFO (1): Storage version of Kuzu: 36
[09:54:31.660] INFO (1): Deployed server started on port: 8000
```

This should open a new tab on your default browser. If not, navigate to [http://localhost:8000/](http://localhost:8000). At first, this page will not be loaded properly. This is normal! It will need to be refreshed after Docker has finished setting up Kùzu Explorer.

If this is the first time you're running the `lostma explorer` command, it will take time to download Kùzu Explorer into your Docker installation. You can watch this progress in your terminal.

Once everything's ready, you'll see the line `Deployed server started on port: 8000` (see the last line of the code block above).

Refresh the page that opened ([http://localhost:8000/](http://localhost:8000)) and you're ready to begin!

![Screenshot of Kuzu Explorer schema view](./img/kuzu_explorer.png)

> Note: I'm aware that Kùzu Explorer currently does not support dates from the Middle Ages. You'll notice this if you look at the property `creation_date` on a Text object, for example. I've opened an [issue](https://github.com/kuzudb/explorer/issues/262) about this on their GitHub. Hopefully it will be resovled in due time, and we can take full advantage of Kùzu Explorer for our LostMa data.

---
[<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M9.195 18.44c1.25.714 2.805-.189 2.805-1.629v-2.34l6.945 3.968c1.25.715 2.805-.188 2.805-1.628V8.69c0-1.44-1.555-2.343-2.805-1.628L12 11.029v-2.34c0-1.44-1.555-2.343-2.805-1.628l-7.108 4.061c-1.26.72-1.26 2.536 0 3.256l7.108 4.061Z" />
</svg>
**Back**
](./transform_into_graph.md) |
[**Next** <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16">
  <path d="M5.055 7.06C3.805 6.347 2.25 7.25 2.25 8.69v8.122c0 1.44 1.555 2.343 2.805 1.628L12 14.471v2.34c0 1.44 1.555 2.343 2.805 1.628l7.108-4.061c1.26-.72 1.26-2.536 0-3.256l-7.108-4.061C13.555 6.346 12 7.249 12 8.689v2.34L5.055 7.061Z" />
</svg>
](./pivot_data_to_tei.md)
