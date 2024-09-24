# Static Site Generator

This project is a simple static site generator written in Python. It converts markdown files into HTML pages using a specified template and copies static files to the output directory. The generated site can be served using a built-in Python HTTP server.

## Project Structure

```bash
.
├── content
│   ├── index.md
│   └── majesty
│       └── index.md
├── public
│   ├── index.html
│   └── majesty
│       └── index.html
├── static
│   └── [static files]
├── template.html
├── src
│   ├── main.py
│   └── [other source files]
├── main.sh
└── README.md
```

## Files and Directories

- [`content/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fcontent%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/content/"): Contains markdown files that will be converted to HTML.
- [`public/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fpublic%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/public/"): The output directory where the generated HTML files and copied static files are stored.
- [`static/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fstatic%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/static/"): Contains static files (e.g., CSS, JavaScript) that will be copied to the [`public/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fpublic%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/public/") directory.
- [`template.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Ftemplate.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/template.html"): The HTML template used to generate the HTML pages.
- [`src/main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/src/main.py"): The main script that performs the site generation.
- [`main.sh`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fmain.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/main.sh"): A shell script to run the main script and start a simple web server.

## Usage

### Prerequisites

- Python 3.x

### Running the Project

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Ensure the directory structure**:
    - [`content/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fcontent%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/content/") should contain your markdown files.
    - [`static/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Fstatic%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/static/") should contain your static files.
    - [`template.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fdimitrislivanas%2Frepos%2Fworkspace%2Fgithub.com%2FdimitrisLivanas%2Fstatic_site_generator%2Ftemplate.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%227260b9d7-b468-47d9-a7ba-74ea679f345f%22%5D "/Users/dimitrislivanas/repos/workspace/github.com/dimitrisLivanas/static_site_generator/template.html") should be your HTML template.

3. **Run the main script**:
    ```sh
    ./main.sh
    ```

4. **Open your browser**:
    - Navigate to [http://localhost:8888](http://localhost:8888) to view the generated site.


### Functions
``` py
copy_static(src, dest)
```
Copies all files and directories from the src directory to the dest directory.

```py
extract_title(markdown)
```
Extracts the h1 header from the markdown content. Raises an exception if no h1 header is found.

```py
generate_page(from_path, template_path, dest_path)
```
Generates an HTML page from a markdown file using a specified template and writes it to the destination path.

```py
generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
```
Recursively generates HTML pages for all markdown files in the content directory and writes them to the public directory, maintaining the directory structure.

### License
This project is licensed under the MIT License.
