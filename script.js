const fileInput = document.getElementById('file-input');
const mapContainer = document.getElementById('map-container');

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            const mapData = e.target.result;
            try {
                const map = parseMap(mapData);
                renderMap(map);
            } catch (error) {
                alert('Error parsing map file. Please check the file format.');
            }
        };
        reader.readAsText(file);
    }
});

function parseMap(mapData) {
    return mapData.split('\\n').map(row => row.split(''));
}

function renderMap(map) {
    mapContainer.innerHTML = '';
    mapContainer.style.gridTemplateColumns = `repeat(${map[0].length}, 20px)`;

    for (let y = 0; y < map.length; y++) {
        for (let x = 0; x < map[y].length; x++) {
            const tile = document.createElement('div');
            tile.classList.add('tile');

            switch (map[y][x]) {
                case '#':
                    tile.classList.add('wall');
                    break;
                case '@':
                    tile.classList.add('player');
                    break;
            }

            mapContainer.appendChild(tile);
        }
    }
}
