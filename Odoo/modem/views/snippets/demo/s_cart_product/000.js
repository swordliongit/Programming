const publicWidget = require('web.public.widget');
const DynamicSnippetCarousel = requre('website.s_dynamic_snippet_carousel');

publicWidget.registry.dynamic_snippet_products = DynamicSnippetCarousel.extend({
    selector: '.s_cart_products',
    _fetchData: async function(){
        const cards = await this._rpc({
            route: '/transfer/card_content',
        });
        this.data = [...$(cards)]
            .filter(node => node.nodeType === 1)
            .map(el => el.outerHTML);
    },
});