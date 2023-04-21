

## Civitai model url extract

A simple python script to extract model urls from civiai url.

### How to use

Put the long list of urls of civitai models into a file, say "urls.txt", then run

```python
python urls.txt models
```

make sure you have `tqdm` and `bs4` installed, this will create a new file named "models.txt" containing real models urls to be downloaded.

### What next

You may use any tool to download the models with the extracted urls, for example with wget:


```bash
wget -c --trust-server-names https://civitai.com/api/download/models/xxxxx
```
