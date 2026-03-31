/** @odoo-module **/

import { SearchModel } from "@web/search/search_model";
import { Domain } from "@web/core/domain";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(SearchModel.prototype, {
    /**
     * Updates the UI separator to show "and" instead of "or"
     * for all multi-value field searches globally.
     */
    _getFacets() {
        const facets = super._getFacets();
        
        for (const facet of facets) {
            // Apply "and" separator to all field and filter facets globally
            if (facet.type === "field" || facet.type === "filter") {
                facet.separator = _t("and");
            }
        }
        return facets;
    },
    
    /**
     * Changes the underlying search logic from OR to AND 
     * for all models in the system.
     */
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

        // Use Domain.and to force all selected values to match
        return Domain.and(domains);
    }
});