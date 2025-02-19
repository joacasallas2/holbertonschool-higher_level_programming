#!/usr/bin/node
exports.callMeMoby = function (x, thefunction) {
    for (let i = 0; i < parseInt(x); i++) {
        thefunction();
    }
}
