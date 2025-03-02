from maya import cmds

class ribbon_tool(object):

    #constructor
    def __init__(self):

        self.window = "ribbon_tool"
        self.title = "Ribbon Tool"
        winWidth = 600
        winHeight = 600

        # close old window if open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)

        #create new window
        self.window = cmds.window(self.window, title=self.title, width=winWidth, height=winHeight)

################################################################### UI LAYOUT

        mainCL = cmds.columnLayout()

        #TITLE
        cmds.setParent(mainCL)
        cmds.separator(h=10, w=winWidth)
        TitleRowWidth = [50, 200, 50]
        cmds.rowLayout(numberOfColumns=3, columnWidth3=TitleRowWidth)
        cmds.text(label="", w=TitleRowWidth[0])
        cmds.text(self.title, h=30, font="boldLabelFont", w=TitleRowWidth[1])
        cmds.text(label="", w=TitleRowWidth[2])

        cmds.setParent("..")
        
        cmds.separator(h=10, w=winWidth)

################################################################### DEFULT RIBBON

        cmds.setParent(mainCL)

        cmds.text(label="Quick Ribbon")
        self.CreateDefRib = cmds.button(label="Create", command=self.CreateDefRib)
        cmds.text(label="Defult Ribbon is a 5 by 1, with 5 joints, and a NURBS surface with 6 segments")
        cmds.text(label="")
        cmds.text(label="Rename?")
        self.CreateDefRibNewName = cmds.button(label="Rename and Create", command=self.CreateDefRibNewName)
        self.NewDefName = cmds.textFieldGrp(label="New name:", columnWidth=(2, 200))

################################################################### RIBBON CUSTOMIZATION

        cmds.setParent(mainCL)

        cmds.text(label="Customized Ribbon")
        cmds.text(label="How many segments needed?")

################################################################### UI CONTENT

        #display new window
        cmds.showWindow()

################################################################### CREATE

    def CreateDefRib(self, *arg):

            # Set the follicle properties
            cmds.setAttr("follicle_Shape{0}.simulationMethod".format(n), 0)
            cmds.setAttr("follicle_Shape{0}.startDirection".format(n), 0)
            cmds.setAttr("follicle_Shape{0}.restPose".format(n), 0)
            cmds.setAttr("follicle_Shape{0}.pointLock".format(n), 1)
            cmds.setAttr("follicle_Shape{0}.parameterU".format(n), n/5.0)
            cmds.setAttr("follicle_Shape{0}.parameterV".format(n), 0.5)
            cmds.setAttr("follicle_{0}.rotateX".format(n), -90)

            cmds.connectAttr("Main_SRFShape.local", "follicle_Shape{0}.inputSurface".format(n))
            cmds.connectAttr("Main_SRFShape.worldMatrix[0]", "follicle_Shape{0}.inputWorldMatrix".format(n))
            cmds.connectAttr("follicle_Shape{0}.outTranslate".format(n), "follicle_{0}.translate".format(n))
            cmds.connectAttr("follicle_Shape{0}.outRotate".format(n), "follicle_{0}.rotate".format(n))

            #Create Joints
            cmds.joint(n="joint_{0}".format(n), rad=0.5)
            cmds.parent("joint_{0}".format(n), w=True)
            cmds.parent("joint_{0}".format(n), "follicle_{0}".format(n))
            #Organizing the outliner
            cmds.parent("follicle_{0}".format(n), "follicle_GRP")
            n+=1

        #Create binding joints
        cmds.joint(p=(0, 0, 0), n="Bind_JNT_A", rad=0.75)
        cmds.parent("Bind_JNT_A", w=True)
        
        cmds.joint(p=(2.5, 0, 0), n="Bind_JNT_B", rad=0.75)
        cmds.parent("Bind_JNT_B", w=True)

        cmds.joint(p=(5, 0, 0), n="Bind_JNT_C", rad=0.75)
        cmds.parent("Bind_JNT_C", w=True)

        #Bind skin
        joints = ["Bind_JNT_A", "Bind_JNT_B", "Bind_JNT_C"]
        cmds.skinCluster(joints, "Main_SRF", dr=4)


    def CreateDefRibNewName(self, *arg):

        new_name = cmds.textFieldGrp(self.CTRLsName, query=True, text=True)

#IN Maya
#ribbon_tool_UI.ribbon_tool()
