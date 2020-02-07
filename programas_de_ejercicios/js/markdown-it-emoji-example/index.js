const fs = require("fs");
const path = require("path");

// const marked = require("marked")
const MarkdownIt = require('markdown-it')
const md = new MarkdownIt()
const emoji = require('markdown-it-emoji')
const twemoji = require('twemoji')

md.use(emoji);

md.renderer.rules.emoji = function(token, idx) {
  return twemoji.parse(token[idx].content);
};

// path de carpeta con markdowns
const MARKDOWN_FILE_DIR = "./md"

// Genera una lista
const markdownFilesData = fs
    // Lee el cotenido de la carpeta
    .readdirSync(MARKDOWN_FILE_DIR)
    // Toma solo archivos .md 
    .filter(filename => /\.md$/.test(filename))
    // por cada .md regresa el markdown normalizado y su filename
    .map(filename => {
        return {
            markdown: fs.readFileSync(path.join(MARKDOWN_FILE_DIR, filename), 'utf8'),
            filename,
        };
    });

markdownFilesData.map( obj => {
    let contenido = md.render(obj.markdown);
    obj.filename = obj.filename.replace(".md",".html")
    fs.writeFileSync(obj.filename, contenido)
})
