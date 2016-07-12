function ConfirmDelete(elem) {
    localStorage.setItem('deleteId', jQuery(elem).attr('data-id'));
    jQuery('#deleteModal').modal();
}