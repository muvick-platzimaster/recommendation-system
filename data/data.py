
from query_project import query_movies

import pandas as pd


cursor_movies = query_movies()
df = pd.DataFrame(cursor_movies)
