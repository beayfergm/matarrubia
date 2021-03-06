import webbrowser
import os
import re

# Movie class name
MOVIE_CLASS_NAME = "Movie";

# Videogame class name
VIDEOGAME_CLASS_NAME = "Videogame";

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>My Media Library</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            height: 450px;
            bottom:0;
            transition: transform .2s ease;
        }
        .movie-tile:hover {
            background-color: #eaeaea;
            cursor: pointer;
            transform: scale(1.05);
        }
        .movie-url {
            cursor: pointer;
        }
        .movie-url:hover {
            background-color: #bbbbbb;
            cursor: pointer;
        }
        .movie-thumbnail {
            max-width= 220px;
            height= 320px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        #bottom-anchor {
            position: absolute;
            margin-left: auto;
            margin-right: auto;
            left: 0;
            right: 0;
            bottom: 20;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Open IMDB link
        $(document).on('click', '.movie-url', function (event) {
            var imdb_url = $(this).attr('href')
            location.href = imdb_url
            event.stopPropagation()
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Media Library</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h3>{title}</h3>
    <h6> {actors} </h6> 
    <div class="movie-thumbnail">
      <img src="{thumbnail_url}" width="220" max-height="342">
    </div>
    {release_date}
    <a class="movie-url" href="{imdb_url}"> IMDB Page </a>
</div>
'''

# A single videogame entry html template
videogame_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h3>{title}</h3>
    <h6> {studio_name} </h6> 
    <div class="movie-thumbnail">
      <img src="{thumbnail_url}" width="220" max-height="342">
    </div>
    <img id="bottom-anchor" src="{pegi_rating_img_url}">
</div>
'''

# Creates an html div containing all the information of the media item and returns it
def create_movie_tiles_content(mediaitems):
    # The HTML content for this section of the page
    content = ''
    for media_item in mediaitems:
        # Default value for the item content is empty
        media_item_content = "";

        # Creates the content for the media item
        # It uses the class name instead of the class type in order to
        # avoid coupling between files. Using plain strings to determine
        # types makes this file to not have dependencies on either
        # Movie or Videogame classes
        if(get_class_name(media_item) is MOVIE_CLASS_NAME):
            media_item_content = create_movie_content(media_item);
        elif(get_class_name(media_item) is VIDEOGAME_CLASS_NAME):
            media_item_content = create_videogame_content(media_item);

        # Append the tile for the movie with its content filled in
        content += media_item_content;
    return content

# Returns the class name of a given object
def get_class_name(object):
    return object.__class__.__name__;

# Creates a media item of type "Movie"
def create_movie_content(movie_media_item):
    trailer_youtube_id = extract_youtube_id(movie_media_item.preview_youtube_url);
    return movie_tile_content.format(
            title=movie_media_item.title,
            thumbnail_url=movie_media_item.thumbnail_url,
            trailer_youtube_id=trailer_youtube_id,
            actors=movie_media_item.actors,
            release_date=movie_media_item.release_date,
            imdb_url=movie_media_item.imdb_url
        );

# Creates a media item of type "Videogame"
def create_videogame_content(videogame_media_item):
    trailer_youtube_id = extract_youtube_id(videogame_media_item.preview_youtube_url);
    return videogame_tile_content.format(
            title=videogame_media_item.title,
            thumbnail_url=videogame_media_item.thumbnail_url,
            trailer_youtube_id=trailer_youtube_id,
            studio_name=videogame_media_item.studio_name,
            pegi_rating_img_url=videogame_media_item.pegi_rating_img_url
        );

# Extract the youtube ID from a url and returns it
def extract_youtube_id(youtube_url):
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', youtube_url)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', youtube_url)
    trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
    return trailer_youtube_id;

def open_movies_page(mediaitems):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(mediaitems))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible