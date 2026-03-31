/** @odoo-module **/

import { SearchModel } from "@web/search/search_model";
import { Domain } from "@web/core/domain";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(SearchModel.prototype, {
    _getFacets() {
        const facets = super._getFacets();
        
        for (const facet of facets) {
            if (facet.type === "field" || facet.type === "filter") {
                facet.separator = _t("and");
            }
        }
        return facets;
    },
    
    _getFieldDomain(field, autocompleteValues) {
        const domains = autocompleteValues.map(({ label, value, operator }) => {
            let domain;
            if (field.filterDomain) {
                domain = new Domain(field.filterDomain).toList({
                    self: label.trim(),
                    raw_value: value,
                });
            } else {
                domain = [[field.fieldName, operator, value]];
            }
            return new Domain(domain);
        });

        return Domain.and(domains);
    }
});