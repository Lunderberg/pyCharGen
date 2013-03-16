<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <!-- interface-requires gtk+ 3.0 -->
  <!-- interface-naming-policy toplevel-contextual -->
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
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="use_action_appearance">False</property>
                <property name="label" translatable="yes">_File</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="fileNew">
                        <property name="label">gtk-new</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="fileOpen">
                        <property name="label">gtk-open</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="fileSave">
                        <property name="label">gtk-save</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="fileSaveAs">
                        <property name="label">gtk-save-as</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
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
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
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
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="use_action_appearance">False</property>
                <property name="label" translatable="yes">_Action</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkMenuItem" id="actionLevelUp">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
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
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="use_action_appearance">False</property>
                <property name="label" translatable="yes">_Help</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem10">
                        <property name="label">gtk-about</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_action_appearance">False</property>
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
                                    <property name="primary_icon_activatable">False</property>
                                    <property name="secondary_icon_activatable">False</property>
                                    <property name="primary_icon_sensitive">True</property>
                                    <property name="secondary_icon_sensitive">True</property>
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
                                    <property name="primary_icon_activatable">False</property>
                                    <property name="secondary_icon_activatable">False</property>
                                    <property name="primary_icon_sensitive">True</property>
                                    <property name="secondary_icon_sensitive">True</property>
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
                                    <property name="primary_icon_activatable">False</property>
                                    <property name="secondary_icon_activatable">False</property>
                                    <property name="primary_icon_sensitive">True</property>
                                    <property name="secondary_icon_sensitive">True</property>
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
                              <object class="GtkTable" id="statTable">
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
                        <property name="height_request">100</property>
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
                  <object class="GtkFrame" id="frame14">
                    <property name="width_request">500</property>
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
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
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
              <object class="GtkHBox" id="hbox4">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkFrame" id="frame16">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label_xalign">0</property>
                    <child>
                      <object class="GtkAlignment" id="alignment16">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="left_padding">12</property>
                        <child>
                          <object class="GtkTreeView" id="itemView">
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                          </object>
                        </child>
                      </object>
                    </child>
                    <child type="label">
                      <object class="GtkLabel" id="label27">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label" translatable="yes">&lt;b&gt;Items&lt;/b&gt;</property>
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
                  <object class="GtkVBox" id="vbox5">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkFrame" id="frame17">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment17">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkEntry" id="itemNameBox">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                                <property name="primary_icon_activatable">False</property>
                                <property name="secondary_icon_activatable">False</property>
                                <property name="primary_icon_sensitive">True</property>
                                <property name="secondary_icon_sensitive">True</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label28">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Item Name&lt;/b&gt;</property>
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
                      <object class="GtkFrame" id="frame18">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment18">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkEntry" id="itemBonusBox">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="invisible_char">●</property>
                                <property name="primary_icon_activatable">False</property>
                                <property name="secondary_icon_activatable">False</property>
                                <property name="primary_icon_sensitive">True</property>
                                <property name="secondary_icon_sensitive">True</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label29">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Bonuses&lt;/b&gt;</property>
                            <property name="use_markup">True</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">False</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkFrame" id="frame19">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="label_xalign">0</property>
                        <child>
                          <object class="GtkAlignment" id="alignment19">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="left_padding">12</property>
                            <child>
                              <object class="GtkTextView" id="itemDescriptionBox">
                                <property name="visible">True</property>
                                <property name="can_focus">True</property>
                                <property name="wrap_mode">word</property>
                              </object>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="label30">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">&lt;b&gt;Description&lt;/b&gt;</property>
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
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">3</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="label26">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Inventory</property>
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
  <object class="GtkMenu" id="rcItemMenu">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="ubuntu_local">True</property>
    <child>
      <object class="GtkMenuItem" id="rcAddItem">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="use_action_appearance">False</property>
        <property name="label" translatable="yes">Add Item</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="rcDeleteItem">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="use_action_appearance">False</property>
        <property name="label" translatable="yes">Delete Item</property>
      </object>
    </child>
  </object>
  <object class="GtkMenu" id="rcSkillMenu">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkMenuItem" id="rcAddChildSkill">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="use_action_appearance">False</property>
        <property name="label" translatable="yes">Add Child Skill</property>
        <property name="use_underline">True</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="rcAddSiblingSkill">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="use_action_appearance">False</property>
        <property name="label" translatable="yes">Add Sibling Skill</property>
        <property name="use_underline">True</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="rcDeleteSkill">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="use_action_appearance">False</property>
        <property name="label" translatable="yes">Delete Skill</property>
        <property name="use_underline">True</property>
      </object>
    </child>
  </object>
</interface>