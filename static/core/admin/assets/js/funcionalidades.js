function confirmarDelete(id) {
    Swal.fire({
        title: "Esta seguro que desea eliminarlo?",
        text: "Este cambio no se podra revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminalo!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                
                text: "El mecánico ha sido eliminado",
                icon: "success"
            }).then(function() {
                window.location.href = "/mecanicos/delete/" + id + "/";
            });
        }
    });
}