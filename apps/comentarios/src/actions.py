def reprova_comentarios(modeladmin, request, query_set):
    query_set.update(aprovado=False)


def aprova_comentarios(modeladmin, request, query_set):
    query_set.update(aprovado=True)


reprova_comentarios.short_description = 'Reprovar Comentários'
aprova_comentarios.short_description = 'Aprovar Comentários'
