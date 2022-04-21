odoo.define('ferrosa.ProductScreen', function(require) {
    "use strict";

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');



    const PosDeProductScreen = ProductScreen => class extends ProductScreen {
        //@Override
        async _clickProduct(event) {
            console.log("............");
            console.log(arguments[0]);
            var atributos = arguments[0];
            if(atributos.detail.precio_minimo > atributos.detail.lst_price){
                const title = this.env._t('Error de precio');
                const body = this.env._t('Actualice el precio de venta del producto '+atributos.detail.display_name+', no cumple con el margen necesario.')
                await this.showPopup('ErrorPopup', { title, body });
                return;
            }

            await super._clickProduct(...arguments)
        }
    }
    Registries.Component.extend(ProductScreen, PosDeProductScreen);

    return ProductScreen;




})