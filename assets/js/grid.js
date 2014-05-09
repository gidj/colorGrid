function octal2hexstring(octstring) {
    arr = [];
    for(i = 0; i < 3; i++) {
        // for each three-digit triplet in octstring, treat as an octal
        // number, parse to an Integer, and place in arr
        arr[i] = parseInt(octstring.slice(3*i, 3*(i+1)), 8);

        // Each octal triplet can hold values in the range 0 - 511; we only
        // want values in the range 0 - 255; so if the converted octal 
        // integer is between 256 and 511, subtract 256 to give an integer 
        // in the desired range.
        if(arr[i] > 255) { arr[i] -= 256; }
    }

    // Convert and concantenate the integers in the array to a valid RGB
    // hex string
    rgb = arr[0].toString(16) + arr[1].toString(16) + arr[2].toString(16);

    return rgb;
}


function print_arr(a) {
    body = document.body;
    para = document.createElement('p');
    for(i = 0; i < a.length; i++) {
        para.appendChild(document.createElement('p'));
        para.appendChild(document.createTextNode(a[i]));
    }

    body.appendChild(para);
}
