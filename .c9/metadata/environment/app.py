{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "],"id":304}],[{"start":{"row":22,"column":2},"end":{"row":22,"column":3},"action":"insert","lines":["C"],"id":305},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["R"]},{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["E"]},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["A"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["T"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["E"]}],[{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "],"id":306}],[{"start":{"row":58,"column":2},"end":{"row":58,"column":3},"action":"insert","lines":["U"],"id":307},{"start":{"row":58,"column":3},"end":{"row":58,"column":4},"action":"insert","lines":["P"]},{"start":{"row":58,"column":4},"end":{"row":58,"column":5},"action":"insert","lines":["D"]},{"start":{"row":58,"column":5},"end":{"row":58,"column":6},"action":"insert","lines":["A"]},{"start":{"row":58,"column":6},"end":{"row":58,"column":7},"action":"insert","lines":["T"]},{"start":{"row":58,"column":7},"end":{"row":58,"column":8},"action":"insert","lines":["E"]}],[{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":308},{"start":{"row":60,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["",""]},{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":59,"column":0},"end":{"row":83,"column":24},"action":"insert","lines":["@app.route('/edit-animal/<animal_id>')","def show_edit_animal_form(animal_id):","    conn = get_connection()","    animal = conn[DATABASE_NAME]['animals'].find_one({","        '_id': ObjectId(animal_id)","    })","    ","    return render_template('edit_animal.template.html', animal=animal)","    ","@app.route(\"/edit-animal/<animal_id>\", methods=['POST'])","def process_edit_animal_form(animal_id):","    animal_name = request.form.get('animal-name')","    breed = request.form['breed']","    microchip = request.form['microchip']","    ","    conn = get_connection()","    conn[DATABASE_NAME][\"animals\"].update({","        '_id':ObjectId(animal_id)","    }, {","        'name':animal_name,","        'breed':breed,","        'microchip':microchip","    })","    ","    return redirect(\"/\")"],"id":309}],[{"start":{"row":59,"column":18},"end":{"row":59,"column":24},"action":"remove","lines":["animal"],"id":310},{"start":{"row":59,"column":18},"end":{"row":59,"column":19},"action":"insert","lines":["A"]},{"start":{"row":59,"column":19},"end":{"row":59,"column":20},"action":"insert","lines":["R"]},{"start":{"row":59,"column":20},"end":{"row":59,"column":21},"action":"insert","lines":["T"]}],[{"start":{"row":59,"column":20},"end":{"row":59,"column":21},"action":"remove","lines":["T"],"id":311},{"start":{"row":59,"column":19},"end":{"row":59,"column":20},"action":"remove","lines":["R"]},{"start":{"row":59,"column":18},"end":{"row":59,"column":19},"action":"remove","lines":["A"]}],[{"start":{"row":59,"column":18},"end":{"row":59,"column":19},"action":"insert","lines":["a"],"id":312},{"start":{"row":59,"column":19},"end":{"row":59,"column":20},"action":"insert","lines":["r"]},{"start":{"row":59,"column":20},"end":{"row":59,"column":21},"action":"insert","lines":["t"]},{"start":{"row":59,"column":21},"end":{"row":59,"column":22},"action":"insert","lines":["w"]},{"start":{"row":59,"column":22},"end":{"row":59,"column":23},"action":"insert","lines":["o"]},{"start":{"row":59,"column":23},"end":{"row":59,"column":24},"action":"insert","lines":["r"]},{"start":{"row":59,"column":24},"end":{"row":59,"column":25},"action":"insert","lines":["k"]}],[{"start":{"row":59,"column":27},"end":{"row":59,"column":33},"action":"remove","lines":["animal"],"id":313},{"start":{"row":59,"column":27},"end":{"row":59,"column":28},"action":"insert","lines":["w"]}],[{"start":{"row":59,"column":27},"end":{"row":59,"column":28},"action":"remove","lines":["w"],"id":314}],[{"start":{"row":59,"column":27},"end":{"row":59,"column":28},"action":"insert","lines":["a"],"id":315},{"start":{"row":59,"column":28},"end":{"row":59,"column":29},"action":"insert","lines":["r"]},{"start":{"row":59,"column":29},"end":{"row":59,"column":30},"action":"insert","lines":["t"]},{"start":{"row":59,"column":30},"end":{"row":59,"column":31},"action":"insert","lines":["w"]},{"start":{"row":59,"column":31},"end":{"row":59,"column":32},"action":"insert","lines":["o"]},{"start":{"row":59,"column":32},"end":{"row":59,"column":33},"action":"insert","lines":["r"]},{"start":{"row":59,"column":33},"end":{"row":59,"column":34},"action":"insert","lines":["k"]}],[{"start":{"row":60,"column":14},"end":{"row":60,"column":20},"action":"remove","lines":["animal"],"id":316},{"start":{"row":60,"column":14},"end":{"row":60,"column":15},"action":"insert","lines":["a"]},{"start":{"row":60,"column":15},"end":{"row":60,"column":16},"action":"insert","lines":["r"]},{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"insert","lines":["t"]},{"start":{"row":60,"column":17},"end":{"row":60,"column":18},"action":"insert","lines":["w"]},{"start":{"row":60,"column":18},"end":{"row":60,"column":19},"action":"insert","lines":["o"]},{"start":{"row":60,"column":19},"end":{"row":60,"column":20},"action":"insert","lines":["r"]},{"start":{"row":60,"column":20},"end":{"row":60,"column":21},"action":"insert","lines":["k"]}],[{"start":{"row":60,"column":27},"end":{"row":60,"column":33},"action":"remove","lines":["animal"],"id":317},{"start":{"row":60,"column":27},"end":{"row":60,"column":28},"action":"insert","lines":["a"]},{"start":{"row":60,"column":28},"end":{"row":60,"column":29},"action":"insert","lines":["r"]},{"start":{"row":60,"column":29},"end":{"row":60,"column":30},"action":"insert","lines":["t"]},{"start":{"row":60,"column":30},"end":{"row":60,"column":31},"action":"insert","lines":["w"]},{"start":{"row":60,"column":31},"end":{"row":60,"column":32},"action":"insert","lines":["o"]},{"start":{"row":60,"column":32},"end":{"row":60,"column":33},"action":"insert","lines":["r"]},{"start":{"row":60,"column":33},"end":{"row":60,"column":34},"action":"insert","lines":["k"]}],[{"start":{"row":62,"column":4},"end":{"row":62,"column":10},"action":"remove","lines":["animal"],"id":318},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":["a"]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["r"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["t"]},{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"insert","lines":["w"]},{"start":{"row":62,"column":8},"end":{"row":62,"column":9},"action":"insert","lines":["o"]},{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"insert","lines":["r"]},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"insert","lines":["k"]}],[{"start":{"row":62,"column":36},"end":{"row":62,"column":42},"action":"remove","lines":["nimals"],"id":319},{"start":{"row":62,"column":36},"end":{"row":62,"column":37},"action":"insert","lines":["r"]},{"start":{"row":62,"column":37},"end":{"row":62,"column":38},"action":"insert","lines":["t"]},{"start":{"row":62,"column":38},"end":{"row":62,"column":39},"action":"insert","lines":["w"]},{"start":{"row":62,"column":39},"end":{"row":62,"column":40},"action":"insert","lines":["r"]},{"start":{"row":62,"column":40},"end":{"row":62,"column":41},"action":"insert","lines":["o"]}],[{"start":{"row":62,"column":40},"end":{"row":62,"column":41},"action":"remove","lines":["o"],"id":320},{"start":{"row":62,"column":39},"end":{"row":62,"column":40},"action":"remove","lines":["r"]}],[{"start":{"row":62,"column":39},"end":{"row":62,"column":40},"action":"insert","lines":["o"],"id":321},{"start":{"row":62,"column":40},"end":{"row":62,"column":41},"action":"insert","lines":["r"]},{"start":{"row":62,"column":41},"end":{"row":62,"column":42},"action":"insert","lines":["k"]},{"start":{"row":62,"column":42},"end":{"row":62,"column":43},"action":"insert","lines":["s"]},{"start":{"row":62,"column":43},"end":{"row":62,"column":44},"action":"insert","lines":["A"]}],[{"start":{"row":62,"column":35},"end":{"row":62,"column":44},"action":"remove","lines":["artworksA"],"id":322},{"start":{"row":62,"column":35},"end":{"row":62,"column":56},"action":"insert","lines":["artworksAndConsigners"]}],[{"start":{"row":63,"column":24},"end":{"row":63,"column":30},"action":"remove","lines":["animal"],"id":323},{"start":{"row":63,"column":24},"end":{"row":63,"column":25},"action":"insert","lines":["A"]},{"start":{"row":63,"column":25},"end":{"row":63,"column":26},"action":"insert","lines":["R"]}],[{"start":{"row":63,"column":25},"end":{"row":63,"column":26},"action":"remove","lines":["R"],"id":324},{"start":{"row":63,"column":24},"end":{"row":63,"column":25},"action":"remove","lines":["A"]}],[{"start":{"row":63,"column":24},"end":{"row":63,"column":25},"action":"insert","lines":["a"],"id":325},{"start":{"row":63,"column":25},"end":{"row":63,"column":26},"action":"insert","lines":["r"]},{"start":{"row":63,"column":26},"end":{"row":63,"column":27},"action":"insert","lines":["t"]},{"start":{"row":63,"column":27},"end":{"row":63,"column":28},"action":"insert","lines":["w"]},{"start":{"row":63,"column":28},"end":{"row":63,"column":29},"action":"insert","lines":["o"]},{"start":{"row":63,"column":29},"end":{"row":63,"column":30},"action":"insert","lines":["r"]},{"start":{"row":63,"column":30},"end":{"row":63,"column":31},"action":"insert","lines":["k"]}],[{"start":{"row":66,"column":33},"end":{"row":66,"column":39},"action":"remove","lines":["animal"],"id":326},{"start":{"row":66,"column":33},"end":{"row":66,"column":34},"action":"insert","lines":["a"]},{"start":{"row":66,"column":34},"end":{"row":66,"column":35},"action":"insert","lines":["r"]},{"start":{"row":66,"column":35},"end":{"row":66,"column":36},"action":"insert","lines":["t"]},{"start":{"row":66,"column":36},"end":{"row":66,"column":37},"action":"insert","lines":["w"]},{"start":{"row":66,"column":37},"end":{"row":66,"column":38},"action":"insert","lines":["o"]},{"start":{"row":66,"column":38},"end":{"row":66,"column":39},"action":"insert","lines":["r"]},{"start":{"row":66,"column":39},"end":{"row":66,"column":40},"action":"insert","lines":["k"]}],[{"start":{"row":68,"column":18},"end":{"row":68,"column":24},"action":"remove","lines":["animal"],"id":327},{"start":{"row":68,"column":18},"end":{"row":68,"column":19},"action":"insert","lines":["a"]},{"start":{"row":68,"column":19},"end":{"row":68,"column":20},"action":"insert","lines":["r"]},{"start":{"row":68,"column":20},"end":{"row":68,"column":21},"action":"insert","lines":["t"]},{"start":{"row":68,"column":21},"end":{"row":68,"column":22},"action":"insert","lines":["w"]},{"start":{"row":68,"column":22},"end":{"row":68,"column":23},"action":"insert","lines":["o"]},{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["r"]},{"start":{"row":68,"column":24},"end":{"row":68,"column":25},"action":"insert","lines":["k"]}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":33},"action":"remove","lines":["nimal"],"id":328},{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["r"]},{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"insert","lines":["t"]},{"start":{"row":68,"column":30},"end":{"row":68,"column":31},"action":"insert","lines":["w"]},{"start":{"row":68,"column":31},"end":{"row":68,"column":32},"action":"insert","lines":["o"]},{"start":{"row":68,"column":32},"end":{"row":68,"column":33},"action":"insert","lines":["r"]},{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"insert","lines":["k"]}],[{"start":{"row":69,"column":18},"end":{"row":69,"column":23},"action":"remove","lines":["nimal"],"id":329},{"start":{"row":69,"column":18},"end":{"row":69,"column":19},"action":"insert","lines":["r"]},{"start":{"row":69,"column":19},"end":{"row":69,"column":20},"action":"insert","lines":["t"]},{"start":{"row":69,"column":20},"end":{"row":69,"column":21},"action":"insert","lines":["w"]},{"start":{"row":69,"column":21},"end":{"row":69,"column":22},"action":"insert","lines":["o"]},{"start":{"row":69,"column":22},"end":{"row":69,"column":23},"action":"insert","lines":["r"]},{"start":{"row":69,"column":23},"end":{"row":69,"column":24},"action":"insert","lines":["k"]}],[{"start":{"row":69,"column":31},"end":{"row":69,"column":36},"action":"remove","lines":["nimal"],"id":330},{"start":{"row":69,"column":31},"end":{"row":69,"column":32},"action":"insert","lines":["r"]},{"start":{"row":69,"column":32},"end":{"row":69,"column":33},"action":"insert","lines":["t"]},{"start":{"row":69,"column":33},"end":{"row":69,"column":34},"action":"insert","lines":["w"]},{"start":{"row":69,"column":34},"end":{"row":69,"column":35},"action":"insert","lines":["o"]},{"start":{"row":69,"column":35},"end":{"row":69,"column":36},"action":"insert","lines":["r"]},{"start":{"row":69,"column":36},"end":{"row":69,"column":37},"action":"insert","lines":["k"]}],[{"start":{"row":70,"column":5},"end":{"row":70,"column":10},"action":"remove","lines":["nimal"],"id":331},{"start":{"row":70,"column":5},"end":{"row":70,"column":6},"action":"insert","lines":["r"]},{"start":{"row":70,"column":6},"end":{"row":70,"column":7},"action":"insert","lines":["t"]},{"start":{"row":70,"column":7},"end":{"row":70,"column":8},"action":"insert","lines":["w"]},{"start":{"row":70,"column":8},"end":{"row":70,"column":9},"action":"insert","lines":["o"]},{"start":{"row":70,"column":9},"end":{"row":70,"column":10},"action":"insert","lines":["r"]},{"start":{"row":70,"column":10},"end":{"row":70,"column":11},"action":"insert","lines":["k"]}],[{"start":{"row":70,"column":0},"end":{"row":72,"column":41},"action":"remove","lines":["    artwork_name = request.form.get('animal-name')","    breed = request.form['breed']","    microchip = request.form['microchip']"],"id":332}],[{"start":{"row":70,"column":0},"end":{"row":76,"column":45},"action":"insert","lines":["    image = request.form.get('image')","    artist = request.form['artist']","    title = request.form['title']","    year = request.form['year']","    dimensions = request.form['dimensions']","    medium = request.form['medium']","    description = request.form['description']"],"id":333}],[{"start":{"row":76,"column":45},"end":{"row":77,"column":0},"action":"insert","lines":["",""],"id":334},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]},{"start":{"row":77,"column":4},"end":{"row":78,"column":0},"action":"insert","lines":["",""]},{"start":{"row":78,"column":0},"end":{"row":78,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":78,"column":4},"end":{"row":78,"column":31},"action":"insert","lines":["type = request.form['type']"],"id":335}],[{"start":{"row":81,"column":26},"end":{"row":81,"column":32},"action":"remove","lines":["nimals"],"id":336},{"start":{"row":81,"column":26},"end":{"row":81,"column":27},"action":"insert","lines":["r"]},{"start":{"row":81,"column":27},"end":{"row":81,"column":28},"action":"insert","lines":["t"]},{"start":{"row":81,"column":28},"end":{"row":81,"column":29},"action":"insert","lines":["w"]},{"start":{"row":81,"column":29},"end":{"row":81,"column":30},"action":"insert","lines":["o"]},{"start":{"row":81,"column":30},"end":{"row":81,"column":31},"action":"insert","lines":["r"]},{"start":{"row":81,"column":31},"end":{"row":81,"column":32},"action":"insert","lines":["k"]}],[{"start":{"row":81,"column":32},"end":{"row":81,"column":33},"action":"insert","lines":["s"],"id":337},{"start":{"row":81,"column":33},"end":{"row":81,"column":34},"action":"insert","lines":["a"]},{"start":{"row":81,"column":34},"end":{"row":81,"column":35},"action":"insert","lines":["n"]},{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"insert","lines":["d"]}],[{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"remove","lines":["d"],"id":338},{"start":{"row":81,"column":34},"end":{"row":81,"column":35},"action":"remove","lines":["n"]},{"start":{"row":81,"column":33},"end":{"row":81,"column":34},"action":"remove","lines":["a"]}],[{"start":{"row":81,"column":33},"end":{"row":81,"column":34},"action":"insert","lines":["A"],"id":339},{"start":{"row":81,"column":34},"end":{"row":81,"column":35},"action":"insert","lines":["d"]},{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"remove","lines":["n"],"id":340},{"start":{"row":81,"column":34},"end":{"row":81,"column":35},"action":"remove","lines":["d"]}],[{"start":{"row":81,"column":34},"end":{"row":81,"column":35},"action":"insert","lines":["n"],"id":341},{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"insert","lines":["d"]},{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"insert","lines":["C"]},{"start":{"row":81,"column":37},"end":{"row":81,"column":38},"action":"insert","lines":["o"]},{"start":{"row":81,"column":38},"end":{"row":81,"column":39},"action":"insert","lines":["n"]},{"start":{"row":81,"column":39},"end":{"row":81,"column":40},"action":"insert","lines":["s"]},{"start":{"row":81,"column":40},"end":{"row":81,"column":41},"action":"insert","lines":["i"]},{"start":{"row":81,"column":41},"end":{"row":81,"column":42},"action":"insert","lines":["g"]},{"start":{"row":81,"column":42},"end":{"row":81,"column":43},"action":"insert","lines":["n"]},{"start":{"row":81,"column":43},"end":{"row":81,"column":44},"action":"insert","lines":["e"]},{"start":{"row":81,"column":44},"end":{"row":81,"column":45},"action":"insert","lines":["r"]}],[{"start":{"row":81,"column":45},"end":{"row":81,"column":46},"action":"insert","lines":["s"],"id":342}],[{"start":{"row":82,"column":24},"end":{"row":82,"column":29},"action":"remove","lines":["nimal"],"id":343},{"start":{"row":82,"column":24},"end":{"row":82,"column":25},"action":"insert","lines":["r"]},{"start":{"row":82,"column":25},"end":{"row":82,"column":26},"action":"insert","lines":["t"]},{"start":{"row":82,"column":26},"end":{"row":82,"column":27},"action":"insert","lines":["w"]},{"start":{"row":82,"column":27},"end":{"row":82,"column":28},"action":"insert","lines":["o"]},{"start":{"row":82,"column":28},"end":{"row":82,"column":29},"action":"insert","lines":["r"]},{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"insert","lines":["k"]}],[{"start":{"row":84,"column":7},"end":{"row":86,"column":29},"action":"remove","lines":[" 'name':animal_name,","        'breed':breed,","        'microchip':microchip"],"id":344}],[{"start":{"row":84,"column":7},"end":{"row":93,"column":21},"action":"insert","lines":["\"image\" : image,","        \"artist\" : artist,","        \"title\" : title,","        \"year\" : year,","        \"dimensions\" : dimensions,","        \"medium\" : medium,","        \"description\" : description,","        ","    # pass value as ARRAY","        \"type\" : type"],"id":345}],[{"start":{"row":66,"column":57},"end":{"row":66,"column":70},"action":"remove","lines":["animal=animal"],"id":346},{"start":{"row":66,"column":57},"end":{"row":66,"column":58},"action":"insert","lines":["a"]},{"start":{"row":66,"column":58},"end":{"row":66,"column":59},"action":"insert","lines":["r"]},{"start":{"row":66,"column":59},"end":{"row":66,"column":60},"action":"insert","lines":["t"]},{"start":{"row":66,"column":60},"end":{"row":66,"column":61},"action":"insert","lines":["w"]},{"start":{"row":66,"column":61},"end":{"row":66,"column":62},"action":"insert","lines":["o"]},{"start":{"row":66,"column":62},"end":{"row":66,"column":63},"action":"insert","lines":["r"]},{"start":{"row":66,"column":63},"end":{"row":66,"column":64},"action":"insert","lines":["k"]},{"start":{"row":66,"column":64},"end":{"row":66,"column":65},"action":"insert","lines":["s"]},{"start":{"row":66,"column":65},"end":{"row":66,"column":66},"action":"insert","lines":["A"]}],[{"start":{"row":66,"column":66},"end":{"row":66,"column":67},"action":"insert","lines":["n"],"id":347}],[{"start":{"row":66,"column":57},"end":{"row":66,"column":67},"action":"remove","lines":["artworksAn"],"id":348},{"start":{"row":66,"column":57},"end":{"row":66,"column":78},"action":"insert","lines":["artworksAndConsigners"]}],[{"start":{"row":66,"column":78},"end":{"row":66,"column":79},"action":"insert","lines":[" "],"id":349},{"start":{"row":66,"column":79},"end":{"row":66,"column":80},"action":"insert","lines":["="]}],[{"start":{"row":66,"column":80},"end":{"row":66,"column":81},"action":"insert","lines":[" "],"id":350},{"start":{"row":66,"column":81},"end":{"row":66,"column":82},"action":"insert","lines":["a"]},{"start":{"row":66,"column":82},"end":{"row":66,"column":83},"action":"insert","lines":["r"]},{"start":{"row":66,"column":83},"end":{"row":66,"column":84},"action":"insert","lines":["t"]},{"start":{"row":66,"column":84},"end":{"row":66,"column":85},"action":"insert","lines":["w"]},{"start":{"row":66,"column":85},"end":{"row":66,"column":86},"action":"insert","lines":["o"]},{"start":{"row":66,"column":86},"end":{"row":66,"column":87},"action":"insert","lines":["r"]},{"start":{"row":66,"column":87},"end":{"row":66,"column":88},"action":"insert","lines":["k"]}],[{"start":{"row":66,"column":88},"end":{"row":66,"column":89},"action":"insert","lines":["s"],"id":351},{"start":{"row":66,"column":89},"end":{"row":66,"column":90},"action":"insert","lines":["s"]}],[{"start":{"row":66,"column":89},"end":{"row":66,"column":90},"action":"remove","lines":["s"],"id":352}],[{"start":{"row":66,"column":89},"end":{"row":66,"column":90},"action":"insert","lines":["A"],"id":353}],[{"start":{"row":66,"column":81},"end":{"row":66,"column":90},"action":"remove","lines":["artworksA"],"id":354},{"start":{"row":66,"column":81},"end":{"row":66,"column":102},"action":"insert","lines":["artworksAndConsigners"]}],[{"start":{"row":82,"column":14},"end":{"row":82,"column":15},"action":"insert","lines":[" "],"id":355},{"start":{"row":82,"column":15},"end":{"row":82,"column":16},"action":"insert","lines":["'"]}],[{"start":{"row":82,"column":36},"end":{"row":82,"column":37},"action":"insert","lines":["'"],"id":356}],[{"start":{"row":63,"column":15},"end":{"row":63,"column":16},"action":"insert","lines":["'"],"id":357}],[{"start":{"row":63,"column":36},"end":{"row":63,"column":37},"action":"insert","lines":["'"],"id":358}],[{"start":{"row":66,"column":78},"end":{"row":66,"column":79},"action":"remove","lines":[" "],"id":359}],[{"start":{"row":66,"column":79},"end":{"row":66,"column":80},"action":"remove","lines":[" "],"id":360}],[{"start":{"row":66,"column":65},"end":{"row":66,"column":100},"action":"remove","lines":["AndConsigners=artworksAndConsigners"],"id":361}],[{"start":{"row":66,"column":65},"end":{"row":66,"column":66},"action":"insert","lines":["="],"id":362},{"start":{"row":66,"column":66},"end":{"row":66,"column":67},"action":"insert","lines":["a"]},{"start":{"row":66,"column":67},"end":{"row":66,"column":68},"action":"insert","lines":["r"]},{"start":{"row":66,"column":68},"end":{"row":66,"column":69},"action":"insert","lines":["t"]},{"start":{"row":66,"column":69},"end":{"row":66,"column":70},"action":"insert","lines":["w"]},{"start":{"row":66,"column":70},"end":{"row":66,"column":71},"action":"insert","lines":["o"]},{"start":{"row":66,"column":71},"end":{"row":66,"column":72},"action":"insert","lines":["r"]},{"start":{"row":66,"column":72},"end":{"row":66,"column":73},"action":"insert","lines":["k"]},{"start":{"row":66,"column":73},"end":{"row":66,"column":74},"action":"insert","lines":["s"]}],[{"start":{"row":66,"column":65},"end":{"row":66,"column":66},"action":"insert","lines":["A"],"id":363},{"start":{"row":66,"column":66},"end":{"row":66,"column":67},"action":"insert","lines":["n"]},{"start":{"row":66,"column":67},"end":{"row":66,"column":68},"action":"insert","lines":["d"]},{"start":{"row":66,"column":68},"end":{"row":66,"column":69},"action":"insert","lines":["C"]},{"start":{"row":66,"column":69},"end":{"row":66,"column":70},"action":"insert","lines":["o"]},{"start":{"row":66,"column":70},"end":{"row":66,"column":71},"action":"insert","lines":["n"]},{"start":{"row":66,"column":71},"end":{"row":66,"column":72},"action":"insert","lines":["s"]},{"start":{"row":66,"column":72},"end":{"row":66,"column":73},"action":"insert","lines":["i"]},{"start":{"row":66,"column":73},"end":{"row":66,"column":74},"action":"insert","lines":["g"]},{"start":{"row":66,"column":74},"end":{"row":66,"column":75},"action":"insert","lines":["n"]}],[{"start":{"row":66,"column":75},"end":{"row":66,"column":76},"action":"insert","lines":["e"],"id":364},{"start":{"row":66,"column":76},"end":{"row":66,"column":77},"action":"insert","lines":["r"]},{"start":{"row":66,"column":77},"end":{"row":66,"column":78},"action":"insert","lines":["s"]}],[{"start":{"row":66,"column":79},"end":{"row":66,"column":87},"action":"remove","lines":["artworks"],"id":365},{"start":{"row":66,"column":79},"end":{"row":66,"column":80},"action":"insert","lines":["a"]},{"start":{"row":66,"column":80},"end":{"row":66,"column":81},"action":"insert","lines":["r"]}],[{"start":{"row":66,"column":79},"end":{"row":66,"column":81},"action":"remove","lines":["ar"],"id":366},{"start":{"row":66,"column":79},"end":{"row":66,"column":100},"action":"insert","lines":["artworksAndConsigners"]}],[{"start":{"row":58,"column":8},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":367}],[{"start":{"row":79,"column":11},"end":{"row":79,"column":23},"action":"remove","lines":["request.form"],"id":368},{"start":{"row":79,"column":11},"end":{"row":79,"column":31},"action":"insert","lines":["request.form.getlist"]}],[{"start":{"row":67,"column":79},"end":{"row":67,"column":100},"action":"remove","lines":["artworksAndConsigners"],"id":369},{"start":{"row":67,"column":79},"end":{"row":67,"column":86},"action":"insert","lines":["artwork"]}],[{"start":{"row":39,"column":11},"end":{"row":39,"column":31},"action":"remove","lines":["request.form['type']"],"id":370},{"start":{"row":39,"column":11},"end":{"row":39,"column":39},"action":"insert","lines":["request.form.getlist['type']"]}],[{"start":{"row":39,"column":31},"end":{"row":39,"column":32},"action":"remove","lines":["["],"id":371}],[{"start":{"row":39,"column":31},"end":{"row":39,"column":32},"action":"insert","lines":["("],"id":372}],[{"start":{"row":39,"column":38},"end":{"row":39,"column":39},"action":"remove","lines":["]"],"id":373}],[{"start":{"row":39,"column":38},"end":{"row":39,"column":39},"action":"insert","lines":[")"],"id":374}],[{"start":{"row":79,"column":38},"end":{"row":79,"column":39},"action":"remove","lines":["]"],"id":375}],[{"start":{"row":79,"column":38},"end":{"row":79,"column":39},"action":"insert","lines":[")"],"id":376}],[{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"remove","lines":["["],"id":377}],[{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"insert","lines":["("],"id":378}],[{"start":{"row":64,"column":15},"end":{"row":64,"column":16},"action":"remove","lines":["'"],"id":379}],[{"start":{"row":64,"column":35},"end":{"row":64,"column":36},"action":"remove","lines":["'"],"id":380}],[{"start":{"row":1,"column":9},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":381}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":25},"action":"insert","lines":["from bson import ObjectId"],"id":382}],[{"start":{"row":66,"column":6},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":383},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]},{"start":{"row":67,"column":4},"end":{"row":68,"column":0},"action":"insert","lines":["",""]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":68,"column":4},"end":{"row":68,"column":5},"action":"insert","lines":["r"],"id":384},{"start":{"row":68,"column":5},"end":{"row":68,"column":6},"action":"insert","lines":["e"]},{"start":{"row":68,"column":6},"end":{"row":68,"column":7},"action":"insert","lines":["s"]},{"start":{"row":68,"column":7},"end":{"row":68,"column":8},"action":"insert","lines":["u"]},{"start":{"row":68,"column":8},"end":{"row":68,"column":9},"action":"insert","lines":["l"]},{"start":{"row":68,"column":9},"end":{"row":68,"column":10},"action":"insert","lines":["t"]},{"start":{"row":68,"column":10},"end":{"row":68,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":68,"column":11},"end":{"row":68,"column":12},"action":"insert","lines":[" "],"id":385},{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":[" "],"id":386}],[{"start":{"row":68,"column":14},"end":{"row":70,"column":6},"action":"insert","lines":["conn[DATABASE_NAME]['artworksAndConsigners'].find_one({","        '_id': ObjectId(artwork_id)","    })"],"id":387}],[{"start":{"row":68,"column":0},"end":{"row":70,"column":6},"action":"remove","lines":["    results = conn[DATABASE_NAME]['artworksAndConsigners'].find_one({","        '_id': ObjectId(artwork_id)","    })"],"id":388},{"start":{"row":67,"column":4},"end":{"row":68,"column":0},"action":"remove","lines":["",""]},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"remove","lines":["    "]},{"start":{"row":66,"column":6},"end":{"row":67,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":66,"column":6},"end":{"row":67,"column":0},"action":"insert","lines":["",""],"id":389},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]},{"start":{"row":67,"column":4},"end":{"row":68,"column":0},"action":"insert","lines":["",""]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":68,"column":4},"end":{"row":68,"column":5},"action":"insert","lines":["r"],"id":390},{"start":{"row":68,"column":5},"end":{"row":68,"column":6},"action":"insert","lines":["e"]},{"start":{"row":68,"column":6},"end":{"row":68,"column":7},"action":"insert","lines":["s"]}],[{"start":{"row":68,"column":4},"end":{"row":68,"column":7},"action":"remove","lines":["res"],"id":391},{"start":{"row":68,"column":4},"end":{"row":68,"column":11},"action":"insert","lines":["results"]}],[{"start":{"row":68,"column":11},"end":{"row":68,"column":12},"action":"insert","lines":[" "],"id":392},{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":[" "],"id":393}],[{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"insert","lines":["a"],"id":394},{"start":{"row":68,"column":15},"end":{"row":68,"column":16},"action":"insert","lines":["r"]},{"start":{"row":68,"column":16},"end":{"row":68,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":68,"column":14},"end":{"row":68,"column":17},"action":"remove","lines":["art"],"id":395},{"start":{"row":68,"column":14},"end":{"row":68,"column":21},"action":"insert","lines":["artwork"]}],[{"start":{"row":68,"column":21},"end":{"row":68,"column":23},"action":"insert","lines":["[]"],"id":396}],[{"start":{"row":68,"column":22},"end":{"row":68,"column":24},"action":"insert","lines":["''"],"id":397}],[{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["t"],"id":398},{"start":{"row":68,"column":24},"end":{"row":68,"column":25},"action":"insert","lines":["y"]},{"start":{"row":68,"column":25},"end":{"row":68,"column":26},"action":"insert","lines":["p"]},{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":86},"end":{"row":70,"column":87},"action":"insert","lines":[","],"id":399}],[{"start":{"row":70,"column":87},"end":{"row":70,"column":88},"action":"insert","lines":[" "],"id":400}],[{"start":{"row":70,"column":88},"end":{"row":70,"column":89},"action":"insert","lines":["t"],"id":401},{"start":{"row":70,"column":89},"end":{"row":70,"column":90},"action":"insert","lines":["y"]},{"start":{"row":70,"column":90},"end":{"row":70,"column":91},"action":"insert","lines":["p"]},{"start":{"row":70,"column":91},"end":{"row":70,"column":92},"action":"insert","lines":["e"]},{"start":{"row":70,"column":92},"end":{"row":70,"column":93},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":93},"end":{"row":70,"column":94},"action":"insert","lines":[" "],"id":402},{"start":{"row":70,"column":94},"end":{"row":70,"column":95},"action":"insert","lines":["="]}],[{"start":{"row":70,"column":95},"end":{"row":70,"column":96},"action":"insert","lines":[" "],"id":403},{"start":{"row":70,"column":96},"end":{"row":70,"column":97},"action":"insert","lines":["r"]},{"start":{"row":70,"column":97},"end":{"row":70,"column":98},"action":"insert","lines":["e"]},{"start":{"row":70,"column":98},"end":{"row":70,"column":99},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":96},"end":{"row":70,"column":99},"action":"remove","lines":["res"],"id":404},{"start":{"row":70,"column":96},"end":{"row":70,"column":103},"action":"insert","lines":["results"]}]]},"ace":{"folds":[],"scrolltop":253,"scrollleft":0,"selection":{"start":{"row":71,"column":4},"end":{"row":71,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":49,"state":"start","mode":"ace/mode/python"}},"timestamp":1572340132677,"hash":"3fcc15f19d0a1266c1bcc8c705d12df60541937f"}