# Blurry Feed

Pelican plugin to add a RSS/Atom feed Tracker to your statically generated webpage.

## How to use

copy the blurry_feed directory to pelican-plugins directory.
Enable pelican plugins in your pelicanconf.py and add blurry_feed to the list of plugins.
add a .yaml file to the root directory of your site ( look at example.yaml )
add the .yaml file in your pelicanconf.py file like below

```
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['blurry_feed']
BLURRY_FEED_YAML="example.yaml"
```

## Example jinja code to include the feed.
```html
{% if BLURRY_FEED_YAML %}  
		<div >    
				<h2>Blurry Feed</h2>
				<ul>            
						{% for entry in blurry_feed %}  
								<li><b>{{entry.published_parsed.tm_year}}-{{entry.published_parsed.tm_mon}}-{{entry.published_parsed.tm_mday}} <a href={{entry.link}}>{{ entry.title }
						{% endfor %}
				</ul>
    </div>
{% endif %}  
```

## Todo

* Caching of the previously fetched entries.
* github CICD


Inspired from : https://github.com/osmoscraft/osmosfeed
