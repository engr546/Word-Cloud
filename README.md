# Word Cloud

A script to create a word cloud image

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install wordcloud
```

## Usage

```python
import wordcloud

cloud = wordcloud.WordCloud()
# Create a word_cloud from words and frequencie
cloud.generate_from_frequencies(frequencies)
# Export to image file.
cloud.to_file(image_name(fname))
# Returns a numpy array
cloud.to_array()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)