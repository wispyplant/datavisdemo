from pathlib import Path
from nicegui import app, ui
from nicegui.events import KeyEventArguments

content = '''
    <svg viewBox="0 0 200 200" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="78" fill="#ffde34" stroke="black" stroke-width="3" />
    <circle cx="80" cy="85" r="8" />
    <circle cx="120" cy="85" r="8" />
    <path d="m60,120 C75,150 125,150 140,120" style="fill:none; stroke:black; stroke-width:8; stroke-linecap:round" />
    </svg>'''
ui.html(content)

ui.markdown('<h1><strong>Data Visualisation</strong></h1')

# slideshow
# ui.query('.nicegui-content').classes('p-0')  # remove padding from the main content
#
# folder = Path(__file__).parent / 'slides'  # image source: https://pixabay.com/
# files = sorted(f.name for f in folder.glob('*.jpg'))
# index = 0
#
#
# def handle_key(event: KeyEventArguments) -> None:
#     global index
#     if event.action.keydown:
#         if event.key.arrow_right:
#             index += 1
#         if event.key.arrow_left:
#             index -= 1
#         index = index % len(files)
#         slide.set_source(f'slides/{files[index]}')
#
#
# app.add_static_files('/slides', folder)  # serve all files in this folder
# slide = ui.image(f'slides/{files[index]}')  # show the first image
# ui.keyboard(on_key=handle_key)  # handle keyboard event

with ui.image('https://picsum.photos/id/29/640/360'):
    ui.label('Nice!').classes('absolute-bottom text-subtitle2 text-center')

with ui.image('https://cdn.stocksnap.io/img-thumbs/960w/airplane-sky_DYPWDEEILG.jpg'):
    ui.html('''
        <svg viewBox="0 0 960 638" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
        <circle cx="445" cy="300" r="100" fill="none" stroke="red" stroke-width="20" />
        </svg>
    ''').classes('bg-transparent')


ui.chat_message('Hello NiceGUI!',
                name='Robot',
                stamp='now',
                avatar='https://robohash.org/ui')

ui.run()
