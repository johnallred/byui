# byui
This will compare each student's file to every other student's file and report the places where there is greater than 90% match.

At a bare minimum, you need to add your student's github ids to names = []

You can change base_url:

Examples:

check css

base_url = 'https://{}.github.io/wdd131/styles/place.css'

check html

base_url = 'https://{}.github.io/wdd131/place.html'

You can also change similarity percentage:

if similarity > 90:

Run from terminal:

python compare.py



