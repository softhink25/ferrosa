odoo.define('ferrosa.models', function (require) {

var models = require('point_of_sale.models');

models.load_fields('product.product', ['precio_minimo']);

});
