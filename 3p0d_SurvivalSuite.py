bl_info = {
    "name": "3P0D's Survival Suite",
    "author": "3P0D ON/OFF",
    "version": (0, 0, 1),
    "blender": (3, 6, 0),
    "location": "View3D > Tool",
    "description": "Lots of repetitive commands because I'm lazy.",
    "warning": "",
    "doc_url": "",
    "category": "View 3D",
}


import bpy

# ----------------------------------------------------------------



# ----------------------------------------------------------------

class LAZYSUITE_PT_main_panel(bpy.types.Panel):

    bl_label = "3P0D's Survival Suite 0.0.1"
    bl_idname = "LAZYSUITE_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Because I'm lazy.")
        
        
class LAZYSUITE_PT_panelA(bpy.types.Panel):
    
    bl_label = "Apply changes on objects"
    bl_idname = "LAZYSUITE_PT_panelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
#    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Transforms:")
        row = layout.row()
        row.operator("lazysuite.applyrotation_rig", icon = 'TRACKING_REFINE_FORWARDS')
        row = layout.row()
        row.operator("lazysuite.applytransform", icon = 'CURVE_NCIRCLE')
        row = layout.row()
        row.operator("lazysuite.cleartransform", icon='TRASH')
        row = layout.row()
        row.label(text="Geometry:")
        row = layout.row()
        row.operator("lazysuite.fixnormals", icon='ORIENTATION_NORMAL')
        row = layout.row()
        row.operator("lazysuite.origintoselect", icon='PIVOT_CURSOR')
        row = layout.row()
        row.label(text="Parents:")
        row = layout.row()
        row.operator("lazysuite.makesingle", icon='HEART')
        row = layout.row()
        
class LAZYSUITE_PT_panelB(bpy.types.Panel):
    
    bl_label = "Add modifiers and objects"
    bl_idname = "LAZYSUITE_PT_panelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
#    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add objects:")
        row = layout.row()
        row.operator("lazysuite.createempty", icon='EMPTY_AXIS')
        row = layout.row()
        row.operator("lazysuite.createsuzanne", icon='MONKEY')
        row = layout.row()
        row.separator()
        row = layout.row()
        row.label(text="Add modifiers:")
        row = layout.row()
        row.operator("lazysuite.addmodifier_mirror", icon='MOD_MIRROR')
        row = layout.row()
        row.operator("lazysuite.addmodifier_bevel", icon='MOD_BEVEL')
        row = layout.row()
        row.operator("lazysuite.addmodifier_shrinkwrap", icon='MOD_SHRINKWRAP')
        row = layout.row()
        
class LAZYSUITE_PT_panelC(bpy.types.Panel):
    
    bl_label = "Add textures and materials"
    bl_idname = "LAZYSUITE_PT_panelC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
#    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add checker texture:")
        row = layout.row()
        row.operator("lazysuite.addchecker_512")
        row.operator("lazysuite.addchecker_1024")
        row.operator("lazysuite.addchecker_2048")
        row.operator("lazysuite.addchecker_4096")
        row = layout.row()
        
class LAZYSUITE_PT_panelD(bpy.types.Panel):
    
    bl_label = "Set objects names"
    bl_idname = "LAZYSUITE_PT_panelD"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Set prefix:")
        row = layout.row()
        row.operator("lazysuite.applyname_mesh")
        row.operator("lazysuite.applyname_geo")
        row = layout.row()
        row.operator("lazysuite.applyname_rig")
        row.operator("lazysuite.applyname_empty")
    
        
# --------------------------------------------------------------------------------

class LAZYSUITE_OT_applyrotation_rig(bpy.types.Operator):
    
    bl_label = "Apply -90 Rotation (Rig)"
    bl_idname = "lazysuite.applyrotation_rig"
    def execute(self, context):
        if bpy.context.object.rotation_euler[0] != -1.570796:
            bpy.context.object.rotation_euler[0] = 0
            bpy.context.object.rotation_euler[1] = 0
            bpy.context.object.rotation_euler[2] = 0
            bpy.context.object.rotation_euler[0] = 1.5708
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.context.object.rotation_euler[0] = -1.5708
        elif bpy.context.object.rotation_euler[0] == -1.5708:
            pass
        return {'FINISHED'}
    
class LAZYSUITE_OT_applytransform(bpy.types.Operator):
    
    bl_label = "Apply all (Transforms)"
    bl_idname = "lazysuite.applytransform"
    def execute(self, context):
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        return {'FINISHED'}

    
class LAZYSUITE_OT_cleartransform(bpy.types.Operator):
    
    bl_label = "Clear all (Transforms)"
    bl_idname = "lazysuite.cleartransform"
    def execute(self, context):
        bpy.ops.object.location_clear(clear_delta=False)
        bpy.ops.object.rotation_clear(clear_delta=False)
        bpy.ops.object.scale_clear(clear_delta=False)
        return {'FINISHED'}
    
class LAZYSUITE_OT_fixnormals(bpy.types.Operator):
    
    bl_label = "Fix normals (Obj.Mode)"
    bl_idname = "lazysuite.fixnormals"
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class LAZYSUITE_OT_origintoselect(bpy.types.Operator):
    
    bl_label = "Set Origin to selected"
    bl_idname = "lazysuite.origintoselect"
    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        return {'FINISHED'}
    
    
class LAZYSUITE_OT_makesingle(bpy.types.Operator):
    
    bl_label = "Make single (Userdata)"
    bl_idname = "lazysuite.makesingle"
    def execute(self, context):
        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False, obdata_animation=False)

        return {'FINISHED'}
    
# --------------------------------------------------------------------------------

class LAZYSUITE_OT_createempty(bpy.types.Operator):
    
    bl_label = "Create Empty (0,0,0)"
    bl_idname = "lazysuite.createempty"
    def execute(self, context):
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "_EMPTY"
        return {'FINISHED'}

class LAZYSUITE_OT_createsuzanne(bpy.types.Operator):
    
    bl_label = "Create Suzanne (0,0,0)"
    bl_idname = "lazysuite.createsuzanne"
    def execute(self, context):
        bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        return {'FINISHED'}

class LAZYSUITE_OT_addmodifier_mirror(bpy.types.Operator):
    
    bl_label = "Mirror (X + Clipping)"
    bl_idname = "lazysuite.addmodifier_mirror"
    def execute(self, context):
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        bpy.context.object.modifiers["Mirror"].show_on_cage = True
        bpy.context.object.modifiers["Mirror"].show_in_editmode = True
        return {'FINISHED'}

class LAZYSUITE_OT_addmodifier_bevel(bpy.types.Operator):
    
    bl_label = "Bevel (Weight)"
    bl_idname = "lazysuite.addmodifier_bevel"
    def execute(self, context):
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].limit_method = 'WEIGHT'
        return {'FINISHED'}

class LAZYSUITE_OT_addmodifier_shrinkwrap(bpy.types.Operator):
    bl_label = "Shrinkwrap (Select.)"
    bl_idname = "lazysuite.addmodifier_shrinkwrap"
    def execute(self, context):
        bpy.ops.object.modifier_add(type='SHRINKWRAP')
        bpy.context.object.modifiers["Shrinkwrap"].target = bpy.context.selected_objects[0]
        bpy.ops.object.modifier_add(type='DISPLACE')
        bpy.context.object.modifiers["Displace"].strength = 0.01
        bpy.context.object.modifiers["Displace"].show_on_cage = True
        bpy.context.object.modifiers["Displace"].show_in_editmode = True
        return {'FINISHED'}

    
# --------------------------------------------------------------------------------

class LAZYSUITE_OT_addchecker_512(bpy.types.Operator):
    
    bl_label = "512"
    bl_idname = "lazysuite.addchecker_512"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_512', width=512, height=512, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_512")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_512")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}
    
class LAZYSUITE_OT_addchecker_1024(bpy.types.Operator):
    
    bl_label = "1024"
    bl_idname = "lazysuite.addchecker_1024"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_1024', width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_1024")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_1024")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}
    
class LAZYSUITE_OT_addchecker_2048(bpy.types.Operator):
    bl_label = "2048"
    bl_idname = "lazysuite.addchecker_2048"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_2048', width=2048, height=2048, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_2048")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_2048")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}

class LAZYSUITE_OT_addchecker_4096(bpy.types.Operator):
    bl_label = "4096"
    bl_idname = "lazysuite.addchecker_4096"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_4096', width=4096, height=4096, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_4096")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_4096")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}



# --------------------------------------------------------------------------------

class LAZYSUITE_OT_applyname_mesh(bpy.types.Operator):
    
    bl_label = "3d_"
    bl_idname = "lazysuite.applyname_mesh"
    def execute(self, context):
        sel_obj = bpy.context.selected_objects
        for i, val in enumerate(sel_obj):
            obj_name = str(sel_obj[i].name)
            if obj_name[:3] != "3d_":
                sel_obj[i].name = str("3d_" + sel_obj[i].name)
            else:
                pass
        return {'FINISHED'}

class LAZYSUITE_OT_applyname_geo(bpy.types.Operator):
    
    bl_label = "GEO_"
    bl_idname = "lazysuite.applyname_geo"
    def execute(self, context):
        sel_obj = bpy.context.selected_objects
        for i, val in enumerate(sel_obj):
            obj_name = str(sel_obj[i].name)
            if obj_name[:4] != "GEO_":
                sel_obj[i].name = str("GEO_" + sel_obj[i].name)
            else:
                pass
        return {'FINISHED'}
    
class LAZYSUITE_OT_applyname_rig(bpy.types.Operator):
    
    bl_label = "RIG_"
    bl_idname = "lazysuite.applyname_rig"

    def execute(self, context):
        sel_obj = bpy.context.selected_objects
        for i, val in enumerate(sel_obj):
            obj_name = str(sel_obj[i].name)
            if obj_name[:4] != "RIG_":
                sel_obj[i].name = str("RIG_" + sel_obj[i].name)
            else:
                pass
        return {'FINISHED'}

class LAZYSUITE_OT_applyname_empty(bpy.types.Operator):
    
    bl_label = "EMPT_"
    bl_idname = "lazysuite.applyname_empty"

    def execute(self, context):
        sel_obj = bpy.context.selected_objects
        for i, val in enumerate(sel_obj):
            obj_name = str(sel_obj[i].name)
            if obj_name[:5] != "EMPT_":
                sel_obj[i].name = str("EMPT_" + sel_obj[i].name)
            else:
                pass
        return {'FINISHED'}
    
# -------------------------------------------------------------------------------------
    
classes = [LAZYSUITE_PT_main_panel, LAZYSUITE_PT_panelA, LAZYSUITE_PT_panelB, LAZYSUITE_PT_panelC, LAZYSUITE_PT_panelD, LAZYSUITE_OT_applyrotation_rig, LAZYSUITE_OT_applytransform, LAZYSUITE_OT_cleartransform, LAZYSUITE_OT_fixnormals, LAZYSUITE_OT_origintoselect, LAZYSUITE_OT_makesingle, LAZYSUITE_OT_createempty, LAZYSUITE_OT_createsuzanne, LAZYSUITE_OT_addmodifier_mirror, LAZYSUITE_OT_addmodifier_bevel, LAZYSUITE_OT_addmodifier_shrinkwrap, LAZYSUITE_OT_addchecker_512, LAZYSUITE_OT_addchecker_1024, LAZYSUITE_OT_addchecker_2048, LAZYSUITE_OT_addchecker_4096, LAZYSUITE_OT_applyname_mesh, LAZYSUITE_OT_applyname_geo, LAZYSUITE_OT_applyname_rig, LAZYSUITE_OT_applyname_empty]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
