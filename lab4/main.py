import builder_file
import mod_double_link_list

driver_name = input("Введите название драйвера > ")
driver_builder = builder_file.SDFabric.get_sd_driver(driver_name)

our_list = mod_double_link_list.DLL()
our_list.set_structure_driver(driver_builder.build())
our_list.add_node('Hi')
our_list.add_node('Hey')
our_list.add_node('Ciao')
print(our_list)
our_list.delete_node('Hey')
print(our_list)

print("Создадим новый LinkedList из файла")
l2 = mod_double_link_list.DLL()
l2.set_structure_driver(builder_file.JSONFileDriver('g.json'))
l2.load()
print(l2)
#our_list.save()
