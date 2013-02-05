<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <!-- interface-requires gtk+ 3.0 -->
  <object class="GtkWindow" id="mainWindow">
    <property name="can_focus">False</property>
    <child>
      <object class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <child>
          <object class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkMenuItem" id="menuitem1">
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_File</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="fileNew">
                        <property name="label">gtk-new</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="fileOpen">
                        <property name="label">gtk-open</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="fileSave">
                        <property name="label">gtk-save</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="fileSaveAs">
                        <property name="label">gtk-save-as</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkSeparatorMenuItem" id="separatormenuitem1">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem5">
                        <property name="label">gtk-quit</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem2">
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_Action</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkMenuItem" id="actionLevelUp">
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">Level Up</property>
                        <property name="use_underline">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem4">
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_Help</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem10">
                        <property name="label">gtk-about</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkNotebook" id="mainTabs">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <child>
              <object class="GtkHBox" id="hbox3">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkVBox" id="vbox3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkFrame" id="frame8">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment8">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkTable" id="table2">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="n_rows">7</property>
                                <property name="n_columns">2</property>
                                <property name="row_spacing">3</property>
                                <child>
                                  <object class="GtkEntry" id="characterName">
                                    <property name="visible">True</property>
                                    <property name="can_focus">True</property>
                                    <property name="invisible_char">●</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="top_attach">1</property>
                                    <property name="bottom_attach">2</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkEntry" id="playerName">
                                    <property name="visible">True</property>
                                    <property name="can_focus">True</property>
                                    <property name="invisible_char">●</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label52">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Player Name:</property>
                                  </object>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label51">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Character Name:</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">1</property>
                                    <property name="bottom_attach">2</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkEntry" id="experience">
                                    <property name="visible">True</property>
                                    <property name="can_focus">True</property>
                                    <property name="invisible_char">●</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="top_attach">6</property>
                                    <property name="bottom_attach">7</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label53">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Experience:</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">6</property>
                                    <property name="bottom_attach">7</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label54">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Level:</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">5</property>
                                    <property name="bottom_attach">6</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="charLevel">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">0</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="top_attach">5</property>
                                    <property name="bottom_attach">6</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label91">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Profession:</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">2</property>
                                    <property name="bottom_attach">3</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label92">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Race:</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">3</property>
                                    <property name="bottom_attach">4</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label93">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="xpad">10</property>
                                    <property name="label" translatable="yes">Background Culture:</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">4</property>
                                    <property name="bottom_attach">5</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="profName">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="top_attach">2</property>
                                    <property name="bottom_attach">3</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="raceName">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="top_attach">3</property>
                                    <property name="bottom_attach">4</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="cultureName">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="top_attach">4</property>
                                    <property name="bottom_attach">5</property>
                                  </packing>
                                </child>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label10">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Character&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkFrame" id="frame7">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment7">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="top_padding">10</property>
                            <property name="bottom_padding">10</property>
                            <property name="left_padding">10</property>
                            <property name="right_padding">10</property>
                            <child>
                              <object class="GtkTable" id="table1">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="n_rows">15</property>
                                <property name="n_columns">5</property>
                                <child>
                                  <object class="GtkVSeparator" id="vseparator1">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">1</property>
                                    <property name="right_attach">2</property>
                                    <property name="bottom_attach">15</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkVSeparator" id="vseparator2">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">3</property>
                                    <property name="right_attach">4</property>
                                    <property name="bottom_attach">15</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkHSeparator" id="hseparator1">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                  </object>
                                  <packing>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">1</property>
                                    <property name="bottom_attach">2</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkHSeparator" id="hseparator2">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                  </object>
                                  <packing>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">7</property>
                                    <property name="bottom_attach">8</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkHSeparator" id="hseparator3">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                  </object>
                                  <packing>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">13</property>
                                    <property name="bottom_attach">14</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label12">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Agility</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">2</property>
                                    <property name="bottom_attach">3</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label13">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Constitution</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">3</property>
                                    <property name="bottom_attach">4</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label14">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Memory</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">4</property>
                                    <property name="bottom_attach">5</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label15">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Reasoning</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">5</property>
                                    <property name="bottom_attach">6</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label16">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Self Discipline</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">6</property>
                                    <property name="bottom_attach">7</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label17">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Empathy</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">8</property>
                                    <property name="bottom_attach">9</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label18">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Intuition</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">9</property>
                                    <property name="bottom_attach">10</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label19">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Presence</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">10</property>
                                    <property name="bottom_attach">11</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label20">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Quickness</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">11</property>
                                    <property name="bottom_attach">12</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label21">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Appearance</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">14</property>
                                    <property name="bottom_attach">15</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label22">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="xalign">1</property>
                                    <property name="label" translatable="yes">Strength</property>
                                  </object>
                                  <packing>
                                    <property name="top_attach">12</property>
                                    <property name="bottom_attach">13</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label23">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Temp</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="label24">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Bonus</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="AgilityTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">2</property>
                                    <property name="bottom_attach">3</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="ConstitutionTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">3</property>
                                    <property name="bottom_attach">4</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="MemoryTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">4</property>
                                    <property name="bottom_attach">5</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="ReasoningTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">5</property>
                                    <property name="bottom_attach">6</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="Self DisciplineTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">6</property>
                                    <property name="bottom_attach">7</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="EmpathyTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">8</property>
                                    <property name="bottom_attach">9</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="IntuitionTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">9</property>
                                    <property name="bottom_attach">10</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="QuicknessTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">11</property>
                                    <property name="bottom_attach">12</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="PresenceTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">10</property>
                                    <property name="bottom_attach">11</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="StrengthTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">12</property>
                                    <property name="bottom_attach">13</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="AppearanceTemp">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">2</property>
                                    <property name="right_attach">3</property>
                                    <property name="top_attach">14</property>
                                    <property name="bottom_attach">15</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="AppearanceBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">14</property>
                                    <property name="bottom_attach">15</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="StrengthBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">12</property>
                                    <property name="bottom_attach">13</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="QuicknessBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">11</property>
                                    <property name="bottom_attach">12</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="PresenceBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">10</property>
                                    <property name="bottom_attach">11</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="IntuitionBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">9</property>
                                    <property name="bottom_attach">10</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="EmpathyBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">8</property>
                                    <property name="bottom_attach">9</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="Self DisciplineBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">6</property>
                                    <property name="bottom_attach">7</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="ReasoningBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">5</property>
                                    <property name="bottom_attach">6</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="MemoryBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">4</property>
                                    <property name="bottom_attach">5</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="ConstitutionBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">3</property>
                                    <property name="bottom_attach">4</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="AgilityBonus">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">0</property>
                                  </object>
                                  <packing>
                                    <property name="left_attach">4</property>
                                    <property name="right_attach">5</property>
                                    <property name="top_attach">2</property>
                                    <property name="bottom_attach">3</property>
                                  </packing>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label11">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Stats&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkFrame" id="frame9">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment9">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkTable" id="resistanceTable">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="n_rows">12</property>
                                <property name="n_columns">2</property>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                                <child>
                                  <placeholder/>
                                </child>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label25">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Resistances&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">2</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkVPaned" id="vpaned1">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="position">350</property>
                    <property name="position_set">True</property>
                    <child>
                      <object class="GtkFrame" id="frame14">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment14">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkScrolledWindow" id="scrolledwindow2">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="hscrollbar_policy">never</property>
                                <child>
                                  <object class="GtkTreeView" id="commonSkillView">
                                    <property name="visible">True</property>
                                    <property name="can_focus">True</property>
                                    <child internal-child="selection">
                                      <object class="GtkTreeSelection" id="treeview-selection1"/>
                                    </child>
                                  </object>
                                </child>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label6">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Commonly Used Skills&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="resize">False</property>
                        <property name="shrink">False</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkFrame" id="frame15">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment15">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkLabel" id="label90">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Not implemented yet.</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label89">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Commonly Used Items&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="resize">True</property>
                        <property name="shrink">True</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">350</property>
                  </packing>
                </child>
              </object>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="label1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Overview</property>
              </object>
              <packing>
                <property name="tab_fill">False</property>
              </packing>
            </child>
            <child>
              <object class="GtkHBox" id="hbox1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="spacing">10</property>
                <child>
                  <object class="GtkFrame" id="frame1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment1">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="left_padding">12</property>
                        <child>
                          <object class="GtkTreeView" id="statView">
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="enable_grid_lines">vertical</property>
                            <child internal-child="selection">
                              <object class="GtkTreeSelection" id="treeview-selection2"/>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label4">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Stat&lt;/b&gt;</property>
                        <property name="use_markup">True</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkVBox" id="vbox2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="spacing">10</property>
                    <child>
                      <object class="GtkFrame" id="frame2">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment2">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkLabel" id="statDescription">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">0</property>
                                <property name="yalign">0</property>
                                <property name="xpad">10</property>
                                <property name="ypad">9</property>
                                <property name="wrap">True</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label5">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Description&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">False</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkFrame" id="frame3">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment3">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkLabel" id="label9">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">0</property>
                                <property name="yalign">0</property>
                                <property name="xpad">10</property>
                                <property name="ypad">10</property>
                                <property name="label" translatable="yes">	This area to contain information on the stat bonuses that the character currently has.</property>
                                <property name="wrap">True</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label8">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Bonuses&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">1</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="label2">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Stats</property>
              </object>
              <packing>
                <property name="position">1</property>
                <property name="tab_fill">False</property>
              </packing>
            </child>
            <child>
              <object class="GtkHBox" id="hbox2">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="spacing">10</property>
                <child>
                  <object class="GtkFrame" id="frame6">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment6">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="left_padding">12</property>
                        <child>
                          <object class="GtkScrolledWindow" id="scrolledwindow1">
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="hscrollbar_policy">never</property>
                            <child>
                              <object class="GtkTreeView" id="skillView">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="enable_grid_lines">vertical</property>
                                <property name="enable_tree_lines">True</property>
                                <child internal-child="selection">
                                  <object class="GtkTreeSelection" id="treeview-selection3"/>
                                </child>
                              </object>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label62">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Skills&lt;/b&gt;</property>
                        <property name="use_markup">True</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkVBox" id="vbox4">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="spacing">10</property>
                    <child>
                      <object class="GtkFrame" id="frame4">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment4">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="top_padding">10</property>
                            <property name="bottom_padding">10</property>
                            <property name="left_padding">10</property>
                            <property name="right_padding">10</property>
                            <child>
                              <object class="GtkLabel" id="skillDescription">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">0</property>
                                <property name="yalign">0</property>
                                <property name="label" translatable="yes">Description of skills goes here.</property>
                                <property name="wrap">True</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label7">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Description&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkFrame" id="frame5">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment5">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkLabel" id="label61">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Placeholder for information on the skill bonuses.</property>
                                <property name="wrap">True</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label31">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Bonuses&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">2</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="label3">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Skills</property>
              </object>
              <packing>
                <property name="position">2</property>
                <property name="tab_fill">False</property>
              </packing>
            </child>
            <child>
              <object class="GtkTable" id="table4">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="n_rows">2</property>
                <property name="n_columns">2</property>
                <child>
                  <object class="GtkFrame" id="frame10">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment10">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="top_padding">10</property>
                        <property name="bottom_padding">10</property>
                        <property name="left_padding">10</property>
                        <property name="right_padding">10</property>
                        <child>
                          <object class="GtkTable" id="table5">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="n_rows">3</property>
                            <property name="n_columns">5</property>
                            <child>
                              <object class="GtkEntry" id="entry2">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label58">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Power Points:</property>
                              </object>
                              <packing>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label60">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Hit Points:</property>
                              </object>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry1">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry3">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label63">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Exhaustion Points:</property>
                              </object>
                              <packing>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkVSeparator" id="vseparator3">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                              </object>
                              <packing>
                                <property name="left_attach">2</property>
                                <property name="right_attach">3</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label83">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Max HP:</property>
                              </object>
                              <packing>
                                <property name="left_attach">3</property>
                                <property name="right_attach">4</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label84">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Max PP:</property>
                              </object>
                              <packing>
                                <property name="left_attach">3</property>
                                <property name="right_attach">4</property>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label85">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Max EP:</property>
                              </object>
                              <packing>
                                <property name="left_attach">3</property>
                                <property name="right_attach">4</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label86">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">0</property>
                              </object>
                              <packing>
                                <property name="left_attach">4</property>
                                <property name="right_attach">5</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label87">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">0</property>
                              </object>
                              <packing>
                                <property name="left_attach">4</property>
                                <property name="right_attach">5</property>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label88">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">0</property>
                              </object>
                              <packing>
                                <property name="left_attach">4</property>
                                <property name="right_attach">5</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label57">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Current Status&lt;/b&gt;</property>
                        <property name="use_markup">True</property>
                      </object>
                    </child>
                  </object>
                </child>
                <child>
                  <object class="GtkFrame" id="frame11">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment11">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="top_padding">10</property>
                        <property name="bottom_padding">10</property>
                        <property name="left_padding">10</property>
                        <property name="right_padding">10</property>
                        <child>
                          <object class="GtkTable" id="table6">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="n_rows">3</property>
                            <property name="n_columns">2</property>
                            <child>
                              <object class="GtkLabel" id="label64">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Bleeding (HP/round):</property>
                              </object>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label65">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Rounds of Stun:</property>
                              </object>
                              <packing>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry4">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry5">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkButton" id="button1">
                                <property name="label" translatable="yes">Next round</property>
                                <property name="use_action_appearance">False</property>
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="receives_default">True</property>
                                <property name="use_action_appearance">False</property>
                              </object>
                              <packing>
                                <property name="right_attach">2</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                                <property name="x_options"></property>
                                <property name="y_options"></property>
                              </packing>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label59">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Per-Round Items&lt;/b&gt;</property>
                        <property name="use_markup">True</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFrame" id="frame12">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment12">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="top_padding">10</property>
                        <property name="bottom_padding">10</property>
                        <property name="left_padding">10</property>
                        <property name="right_padding">10</property>
                        <child>
                          <object class="GtkTable" id="table7">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="n_rows">4</property>
                            <property name="n_columns">2</property>
                            <child>
                              <object class="GtkLabel" id="label67">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">HP Loss:</property>
                              </object>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label68">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Extra Bleeding:</property>
                              </object>
                              <packing>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label69">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Extra Rounds of Stun:</property>
                              </object>
                              <packing>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry6">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry7">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkEntry" id="entry8">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkButton" id="button2">
                                <property name="label" translatable="yes">Apply</property>
                                <property name="use_action_appearance">False</property>
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="receives_default">True</property>
                                <property name="use_action_appearance">False</property>
                              </object>
                              <packing>
                                <property name="right_attach">2</property>
                                <property name="top_attach">3</property>
                                <property name="bottom_attach">4</property>
                                <property name="x_options"></property>
                                <property name="y_options"></property>
                              </packing>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label66">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Taking Damage&lt;/b&gt;</property>
                        <property name="use_markup">True</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFrame" id="frame13">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment13">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="top_padding">10</property>
                        <property name="bottom_padding">10</property>
                        <property name="left_padding">10</property>
                        <property name="right_padding">10</property>
                        <child>
                          <object class="GtkTable" id="table8">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="n_rows">10</property>
                            <property name="n_columns">4</property>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label71">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">1</property>
                                <property name="xpad">10</property>
                                <property name="label" translatable="yes">Base Rate (ft/rnd):</property>
                              </object>
                              <packing>
                                <property name="right_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label72">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="xalign">0</property>
                                <property name="label" translatable="yes">0</property>
                              </object>
                              <packing>
                                <property name="left_attach">2</property>
                                <property name="right_attach">4</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkHSeparator" id="hseparator4">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                              </object>
                              <packing>
                                <property name="right_attach">4</property>
                                <property name="top_attach">1</property>
                                <property name="bottom_attach">2</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label73">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Pace</property>
                              </object>
                              <packing>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkHSeparator" id="hseparator5">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                              </object>
                              <packing>
                                <property name="right_attach">4</property>
                                <property name="top_attach">3</property>
                                <property name="bottom_attach">4</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label74">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Speed (ft/rnd)</property>
                              </object>
                              <packing>
                                <property name="left_attach">1</property>
                                <property name="right_attach">2</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label75">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Exh. Point
(Click to Apply)</property>
                                <property name="justify">center</property>
                              </object>
                              <packing>
                                <property name="left_attach">2</property>
                                <property name="right_attach">3</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label76">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Maneuver</property>
                              </object>
                              <packing>
                                <property name="left_attach">3</property>
                                <property name="right_attach">4</property>
                                <property name="top_attach">2</property>
                                <property name="bottom_attach">3</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label77">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Walk</property>
                              </object>
                              <packing>
                                <property name="top_attach">4</property>
                                <property name="bottom_attach">5</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label78">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Fast Walk</property>
                              </object>
                              <packing>
                                <property name="top_attach">5</property>
                                <property name="bottom_attach">6</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label79">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Run</property>
                              </object>
                              <packing>
                                <property name="top_attach">6</property>
                                <property name="bottom_attach">7</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label80">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Sprint</property>
                              </object>
                              <packing>
                                <property name="top_attach">7</property>
                                <property name="bottom_attach">8</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label81">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Fast Sprint</property>
                              </object>
                              <packing>
                                <property name="top_attach">8</property>
                                <property name="bottom_attach">9</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkLabel" id="label82">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label" translatable="yes">Dash</property>
                              </object>
                              <packing>
                                <property name="top_attach">9</property>
                                <property name="bottom_attach">10</property>
                              </packing>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label70">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Movement&lt;/b&gt;</property>
                        <property name="use_markup">True</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">3</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="label56">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Combat (not implemented)</property>
              </object>
              <packing>
                <property name="position">3</property>
                <property name="tab_fill">False</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkMenu" id="rcSkillMenu">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkMenuItem" id="rcAddChildSkill">
        <property name="use_action_appearance">False</property>
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">Add Child Skill</property>
        <property name="use_underline">True</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="rcAddSiblingSkill">
        <property name="use_action_appearance">False</property>
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">Add Sibling Skill</property>
        <property name="use_underline">True</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="rcDeleteSkill">
        <property name="use_action_appearance">False</property>
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">Delete Skill</property>
        <property name="use_underline">True</property>
      </object>
    </child>
  </object>
</interface>
