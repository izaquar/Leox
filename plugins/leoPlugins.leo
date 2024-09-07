<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet ekr_test?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.291666666667">
	<global_window_position top="60" left="10" height="773" width="1536"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="ekr.20041211035618"><vh>Scripts, buttons &amp; settings</vh>
<v t="ekr.20050217093214"><vh>@settings</vh>
<v t="ekr.20050328101812"><vh>@page http plugin</vh>
<v t="ekr.20050328101812.1"><vh>@bool http_active = False</vh></v>
<v t="ekr.20050328101812.2"><vh>@int  port = 8080</vh></v>
<v t="ekr.20050328101812.3"><vh>@string rst_http_attributename = rst_http_attribute</vh></v>
</v>
</v>
<v t="EKR.20040517075110"><vh>replaceLeoGlobals</vh>
<v t="EKR.20040517075110.1"><vh>&lt;&lt; set nameList to the list of functions in leoGlobals.py &gt;&gt;</vh></v>
<v t="EKR.20040517075110.2"><vh>findFunctionsInTree</vh></v>
<v t="EKR.20040517075110.3"><vh>findDefs</vh></v>
<v t="EKR.20040517075110.4"><vh>prependNamesInTree</vh>
<v t="EKR.20040517075110.5"><vh>&lt;&lt; look for name followed by '(' &gt;&gt;</vh></v>
<v t="EKR.20040517075110.6"><vh>&lt;&lt; print before and after &gt;&gt;</vh></v>
</v>
</v>
<v t="ekr.20041103052443"><vh>Script to find and replace all functions in leoGlobals.py</vh>
<v t="ekr.20041103052443.1"><vh>findFunctionsInTree</vh></v>
<v t="ekr.20041103052443.2"><vh>findDefs</vh></v>
<v t="ekr.20041103052443.3"><vh>prependNamesInTree</vh>
<v t="ekr.20041103052443.4"><vh>&lt;&lt; look for name followed by '(' &gt;&gt;</vh></v>
<v t="ekr.20041103052443.5"><vh>&lt;&lt; print before and after &gt;&gt;</vh></v>
</v>
<v t="ekr.20041103052443.6"><vh>&lt;&lt; set nameList to the list of functions in leoGlobals.py &gt;&gt;</vh></v>
</v>
<v t="ekr.20060924180348"><vh>buttons</vh>
<v t="ekr.20060109114710"><vh>@@button settings.leo</vh></v>
<v t="ekr.20060827163237"><vh>@@button scripts.leo</vh></v>
<v t="ekr.20050724100334"><vh>@@button Beautify</vh></v>
<v t="ekr.20051025144116"><vh>@@button Spell</vh></v>
<v t="ekr.20050819055746"><vh>@@button Save</vh></v>
</v>
</v>
<v t="edream.110203113231.618" a="E"><vh>Plugins</vh>
<v t="EKR.20040517090508" a="E"><vh>  Enable plugins by changing pluginsManager.txt or using plugin_manager plugin</vh>
<v t="edream.120603093808" tnodeList="edream.120603093808"><vh>@nosent pluginsManager.txt</vh></v>
</v>
<v t="ekr.20050303051035"><vh> Templates: these show recommended ways of defining plugins.</vh>
<v t="ekr.20041114102139"><vh>Notes</vh>
<v t="ekr.20041114103913"><vh>About comments in the style guide</vh></v>
<v t="ekr.20041114102139.1"><vh>About the root node</vh></v>
<v t="ekr.20041114103913.1"><vh>About defining functions in separate nodes</vh></v>
<v t="ekr.20041114102139.2"><vh>About the &lt;&lt; imports &gt;&gt; section</vh></v>
<v t="ekr.20050306072156"><vh>About exceptions</vh></v>
</v>
<v t="ekr.20050306071629"><vh>Template for plugin that overrides commander methods</vh>
<v t="ekr.20050306071629.1"><vh>&lt;&lt; docstring &gt;&gt;</vh></v>
<v t="ekr.20050306071629.2"><vh>&lt;&lt; version history &gt;&gt;</vh></v>
<v t="ekr.20050306071629.3"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="ekr.20050306071629.4"><vh>init</vh></v>
<v t="ekr.20050306071540"><vh>onStart2</vh></v>
</v>
<v t="ekr.20050303051035.2"><vh>Template for Tk plugin with per-commander controller class</vh>
<v t="ekr.20050303051035.3"><vh>&lt;&lt; docstring &gt;&gt;</vh></v>
<v t="ekr.20050303051035.4"><vh>&lt;&lt; version history &gt;&gt;</vh></v>
<v t="ekr.20050303051035.5"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="ekr.20050303051101"><vh>init</vh></v>
<v t="ekr.20050303051150"><vh>onCreate</vh></v>
<v t="ekr.20050303051222"><vh>class pluginController</vh>
<v t="ekr.20050303051222.1"><vh>__init__</vh></v>
</v>
</v>
</v>
<v t="ekr.20040722135402.1"><vh>Body pane</vh>
<v t="ekr.20060506070443.1"><vh>@thin detect_urls.py</vh></v>
<v t="edream.110203113231.753" a="M"><vh>@thin image.py</vh></v>
<v t="ekr.20040422072343"><vh>thin rClick.py</vh>
<v t="ekr.20040422081253"><vh>&lt;&lt; version history &gt;&gt;</vh></v>
<v t="ekr.20050101090207.2"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="ekr.20060108122501"><vh>Module-level</vh>
<v t="ekr.20060108122501.1"><vh>init</vh></v>
<v t="ekr.20040422072343.5"><vh>rClickbinder</vh></v>
<v t="ekr.20040422072343.6"><vh>rClicker</vh>
<v t="ekr.20060110123700"><vh>&lt;&lt; define callbacks &gt;&gt;</vh></v>
<v t="ekr.20040422072343.7"><vh>&lt;&lt; define commandList for body &gt;&gt;</vh></v>
<v t="ekr.20040422072343.8"><vh>&lt;&lt; add entries for context sensitive commands in body &gt;&gt;</vh>
<v t="ekr.20040422073911"><vh>&lt;&lt; get text and word from the body text &gt;&gt;</vh></v>
<v t="ekr.20040422072343.13"><vh>&lt;&lt; add entry for open url &gt;&gt;</vh></v>
<v t="ekr.20040422072343.14"><vh>&lt;&lt; add entry for jump to section &gt;&gt;</vh></v>
<v t="ekr.20040422072343.15"><vh>&lt;&lt; add epydoc help &gt;&gt;</vh></v>
</v>
<v t="ekr.20040422072343.16"><vh>&lt;&lt; define commandList for log pane &gt;&gt;</vh></v>
</v>
</v>
<v t="ekr.20040422072343.1"><vh>rc_help</vh></v>
<v t="ekr.20040422072343.2"><vh>rc_dbody</vh></v>
<v t="ekr.20040422072343.3"><vh>rc_nl</vh></v>
<v t="ekr.20040422072343.4"><vh>rc_selectAll</vh></v>
<v t="ekr.20040422072343.9"><vh>Utils for context sensitive commands</vh>
<v t="ekr.20040422072343.10"><vh>crop</vh></v>
<v t="ekr.20040422072343.11"><vh>getword</vh></v>
<v t="ekr.20040422072343.12"><vh>getdoc</vh></v>
</v>
</v>
<v t="edream.110203113231.925"><vh>@thin script_io_to_body.py</vh></v>
<v t="edream.110403140857"><vh>color_markup.py (requires add-directives plugin)</vh>
<v t="edream.110403140857.1"><vh>Plugin documentation</vh>
<v t="edream.110403140857.2"><vh>Installation</vh></v>
<v t="edream.110403140857.3"><vh>Use</vh>
<v t="edream.110403140857.4"><vh>Supported markups</vh></v>
<v t="edream.110403140857.5"><vh>Example</vh>
<v t="edream.110403140857.6"><vh>a subnode</vh></v>
</v>
</v>
<v t="edream.110403140857.7"><vh>Release notes</vh></v>
</v>
<v t="edream.110403140857.8"><vh>@thin color_markup.py</vh></v>
</v>
</v>
<v t="edream.110203113231.667"><vh>Commands &amp; directives</vh>
<v t="edream.110203113231.668"><vh> Importing Cisco configuration files</vh>
<v t="edream.110203113231.669"><vh>@thin import_cisco_config.py</vh></v>
</v>
<v t="edream.110203113231.741"><vh>@thin add_directives.py</vh></v>
<v t="timo.20050213160555"><vh>@thin bibtex.py</vh></v>
<v t="ekr.20040916073636"><vh>@thin ConceptualSort.py</vh></v>
<v t="ekr.20040915105758.13"><vh>@thin FileActions.py</vh></v>
<v t="mork.20041018131258.1"><vh>@thin groupOperations.py</vh></v>
<v t="ekr.20050328092641.4"><vh>@thin Library.py</vh></v>
<v t="ekr.20040916084945"><vh>@thin macros.py</vh></v>
<v t="ekr.20050301083306"><vh>@thin mod_read_dir_outline.py</vh></v>
<v t="edream.110203113231.727"><vh>@thin mod_timestamp.py</vh></v>
<v t="edream.110203113231.720"><vh>@thin outline_export.py</vh></v>
<v t="danr7.20060912105041.1"><vh>@thin paste_as_headlines.py</vh></v>
<v t="ekr.20041021120118"><vh>@thin pretty_print.py</vh></v>
<v t="ekr.20040331153923"><vh>@thin scheduler.py</vh></v>
<v t="mork.20041022090036.1"><vh>@thin templates.py</vh></v>
<v t="danr7.20061010105952.1"><vh>@thin word_count.py</vh></v>
<v t="edream.110203113231.722"><vh>mod_autosave</vh>
<v t="edream.110203113231.723" tnodeList="edream.110203113231.723"><vh>@file-nosent mod_autosave.ini</vh></v>
<v t="edream.110203113231.724"><vh>@thin mod_autosave.py</vh></v>
</v>
<v t="ekr.20041110104350"><vh>table plugin: requires tktable</vh>
<v t="ekr.20041017035937"><vh>@thin table.py</vh></v>
</v>
</v>
<v t="edream.110203113231.729"><vh>Debugging &amp;  testing</vh>
<v t="edream.110203113231.730"><vh>@thin dump_globals.py</vh></v>
<v t="edream.110203113231.732"><vh>@thin enable_gc.py</vh></v>
<v t="ekr.20050130120433"><vh>@thin failed_import.py</vh></v>
<v t="edream.110203113231.734"><vh>@thin quit_leo.py</vh></v>
<v t="ekr.20051016160700"><vh>@thin testRegisterCommand.py</vh></v>
<v t="edream.110203113231.735"><vh>@thin trace_gc_plugin.py</vh></v>
<v t="edream.110203113231.736"><vh>@thin trace_keys.py</vh></v>
<v t="edream.110203113231.738"><vh>@thin trace_tags.py</vh></v>
<v t="ekr.20040205071616"><vh>mnplugins.py</vh>
<v t="ekr.20050101090717"><vh>&lt;&lt; docstring &gt;&gt;</vh></v>
<v t="ekr.20050101090717.1"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="ekr.20040205071616.1"><vh>mnstamp</vh></v>
<v t="ekr.20040205071616.2"><vh>mnOKstamp</vh></v>
<v t="ekr.20040205071616.3"><vh>onStart</vh></v>
<v t="ekr.20040205071616.4"><vh>setHeadOK</vh></v>
<v t="ekr.20040205071616.5"><vh>insertBodystamp</vh></v>
<v t="ekr.20040205071616.6"><vh>is_subnodesOK</vh></v>
<v t="ekr.20040205071616.7"><vh>onRclick</vh></v>
<v t="ekr.20040205071616.8"><vh>insertOKcmd</vh></v>
<v t="ekr.20040205071616.9"><vh>insertUser</vh></v>
<v t="ekr.20040205071616.10"><vh>create_UserMenu</vh></v>
</v>
<v t="ekr.20060513122613"><vh>xcc plugin</vh>
<v t="ekr.20060513122613.1"><vh>Examples</vh>
<v t="ekr.20060513122613.2" xcc_cfg="7d710028550a45786563757461626c6571017d710228550a446c6c2063616c6c65727103550071045513457865637574696f6e20617267756d656e747371056804755504436f64657106680455074144445f4c4f477107680455055469746c65710868045508446562756767657271097d710a28550e4964656e7469667920627265616b710b6804550f54617267657420706964207461736b710c680455085069706520656f6c710d68045509417267756d656e7473710e6804550e50726f6d7074207061747465726e710f6804550e5175657279206c6f636174696f6e71106804550846696e642070696471116804550b436c65617220627265616b7112680455084576616c7561746571136804550453746f707114680455045374657071156804550b4c69737420627265616b737116680455045461736b71176804550f427265616b20646574656374696f6e71186804550853746570206f757471196804550953657420627265616b711a6804550d46696e64206c6f636174696f6e711b680455075374657020696e711c6804680968045512526567756c61722065787072657373696f6e711d68045508436f6e74696e7565711e68045502476f711f6804550c53746172747570207461736b71206804550953746570206f766572712155046e65787471227555075345545f4c4f47712368045506494e495445447124550454727565712555074f7074696f6e7371267d712728550b58636320766572626f73657128550546616c73657129550745786563757465712a550546616c7365712b550c4372656174652066696c6573712c550454727565712d55105365656b20627265616b706f696e7473712e550546616c7365712f550f436f6e6e65637420746f20706970657130550546616c736571315507436f6d70696c657132550546616c73657133550d46696c746572206f75747075747134550546616c7365713555134175746f20696e636c756465206865616465727136550546616c73657137550544656275677138550546616c7365713955105365656b206669727374206572726f72713a550546616c7365713b550c436f6c6f72697a65206c6f67713c550546616c7365713d755508436f6d70696c6572713e7d713f285514496e636c7564652073656172636820706174687371406804550f4572726f7220646574656374696f6e71416804550b557365206c69627261727971426804550e55736564206c696272617269657371436804550f446562756720617267756d656e747371446804550d436865636b2073796e7461786571456804550c4c696272617279207061746871466804680e680455094275696c6420646c6c714768045507557365207063687148680455094275696c64206578657149680455144c69627261727920736561726368207061746873714a6804550c496e636c7564652070617468714b6804550b436f6d70696c6520706368714c6804683e680475752e"><vh>@xcc OpenGl.h</vh>
<v t="ekr.20060513122613.3" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>USE_OPENGL</vh></v>
<v t="ekr.20060513122613.4" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>Data Types</vh></v>
<v t="ekr.20060513122613.5" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>1.1</vh>
<v t="ekr.20060513122613.6" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>Defs</vh></v>
<v t="ekr.20060513122613.7" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>Procs</vh></v>
</v>
<v t="ekr.20060513122613.8" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>1.2</vh>
<v t="ekr.20060513122613.9"><vh>Defs</vh></v>
<v t="ekr.20060513122613.10"><vh>Procs</vh></v>
</v>
<v t="ekr.20060513122613.11"><vh>1.3</vh>
<v t="ekr.20060513122613.12"><vh>Defs</vh></v>
<v t="ekr.20060513122613.13"><vh>Procs</vh></v>
</v>
<v t="ekr.20060513122613.14"><vh>1.4</vh>
<v t="ekr.20060513122613.15"><vh>Defs</vh></v>
<v t="ekr.20060513122613.16"><vh>Procs</vh></v>
</v>
<v t="ekr.20060513122613.17" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>1.5</vh>
<v t="ekr.20060513122613.18" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>Defs</vh></v>
<v t="ekr.20060513122613.19" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>Procs</vh></v>
</v>
<v t="ekr.20060513122613.20" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>WGL</vh></v>
</v>
<v t="ekr.20060513122613.21" xcc_cfg="7d710028550a45786563757461626c6571017d710228550a446c6c2063616c6c65727103550071045513457865637574696f6e20617267756d656e747371056804755504436f64657106680455074144445f4c4f477107680455055469746c6571085510636c5f6364625f77696e33325f657865710955055761746368710a5d710b550161710c61550b427265616b706f696e7473710d7d710e2855056370703a38710f5507456e61626c6564711055066370703a3138711168107555075345545f4c4f47711268045506494e4954454471135504547275657114550b427265616b506f696e747371157d71162855066370703a313571175507456e61626c6564711855066370703a313371195507456e61626c6564711a7555074f7074696f6e73711b7d711c28550b58636320766572626f7365711d550454727565711e550745786563757465711f550546616c73657120550c4372656174652066696c65737121550454727565712255105365656b20627265616b706f696e747371235504547275657124550f436f6e6e65637420746f2070697065712568045507436f6d70696c6571265504547275657127550d46696c746572206f75747075747128550546616c7365712955134175746f20696e636c75646520686561646572712a550454727565712b55054465627567712c550454727565712d55105365656b206669727374206572726f72712e550546616c7365712f755508446562756767657271307d713128550e4964656e7469667920627265616b7132552720283f503c49443e5b302d395d2b29202e2b5f46494c455f282040207c3a295f4c494e455f2e2b7133550f54617267657420706964207461736b713455092e746c697374202d63713555085069706520656f6c713655045c6e5c7271375509417267756d656e74737138555c2d6c696e6573202d47202d320a2d7372637061746820225f414253504154485f220a2d7920227372762a5f414253504154485f220a2d6920225f414253504154485f220a225f414253504154485f5c5c5f4e414d455f2e657865220a7139550e50726f6d7074207061747465726e713a55013e713b550e5175657279206c6f636174696f6e713c55096c732e203b206c7363713d550846696e6420706964713e5521306e283f503c5049443e5b302d395d2b29202e2a5f4e414d455f5c2e5f4558545f713f550b436c65617220627265616b714055076263205f49445f714155084576616c75617465714255023f3f7143550453746f707144550171714555045374657071465501707147550b4c69737420627265616b7371485502626c714955045461736b714a6804550f427265616b20646574656374696f6e714b5516427265616b706f696e74205b302d395d2b206869740a714c550853746570206f7574714d55026775714e550953657420627265616b714f5512627020605f46494c455f3a5f4c494e455f607150550d46696e64206c6f636174696f6e7151553243757272656e743a202e2a5f4e414d455f5c2e283f503c4558543e2e2b295c28283f503c4c494e453e5b302d395d2b295c29715255075374657020696e715355017471546830551e433a5c53444b5c437573746f6d33325c77696e6462675c6364622e65786571555512526567756c61722065787072657373696f6e7156550c507265737320454e5445520a71575508436f6e74696e7565715855016771595502476f715a6859550c53746172747570207461736b715b552b7371653b6c2b2a3b206c7370202d61203120303b206c737020303b2062702077696e6d61696e3b2020670a715c550953746570206f766572715d55046e657874715e755508436f6d70696c6572715f7d7160285514496e636c7564652073656172636820706174687371615532433a5c53444b5c437573746f6d33325c696e636c7564650a433a5c53444b5c437573746f6d33325c696e636c75646533320a7162550f4572726f7220646574656374696f6e71635549283f503c46494c453e5b5e5c5c5d2b295c28283f503c4c494e453e5b302d395d2b295c29203a206572726f7220283f503c49443e435b302d395d2b293a20283f503c4445463e2e2b297164550b557365206c6962726172797165550c2f44454641554c544c49423a7166550e55736564206c69627261726965737167550b7573657233322e6c69620a7168550f446562756720617267756d656e7473716955a5225f414253504154485f5c5f4e414d455f2e5f5352434558545f220a2f4665225f414253504154485f5c5f4e414d455f2e5f4558545f220a2f466f225f414253504154485f5c5f4e414d455f2e6f626a220a2f4664225f414253504154485f5c5f4e414d455f220a5f494e4350415448535f0a5f4255494c445f640a2f6e6f6c6f676f0a2f5a690a2f6c696e6b0a5f4c494250415448535f0a5f4c49425241524945535f0a716a550d436865636b2073796e74617865716b55032f5a73716c550c4c6962726172792070617468716d55092f4c4942504154483a716e6838558a225f414253504154485f5c5f4e414d455f2e5f5352434558545f220a2f4665225f414253504154485f5c5f4e414d455f2e5f4558545f220a2f466f225f414253504154485f5c5f4e414d455f2e6f626a220a5f494e4350415448535f0a5f4255494c445f0a2f6e6f6c6f676f0a2f6c696e6b0a5f4c494250415448535f0a5f4c49425241524945535f0a716f55094275696c6420646c6c717055032f4c447171550755736520706368717255032f5975717355094275696c6420657865717455032f4d4c717555144c696272617279207365617263682070617468737176552a433a5c53444b5c437573746f6d33325c6c69620a433a5c53444b5c437573746f6d33325c6c696233320a7177550c496e636c7564652070617468717855022f497179550b436f6d70696c6520706368717a55032f5963717b685f5516433a5c53444b5c437573746f6d33325c636c2e657865717c75752e"><vh>@xcc cltest\testprog</vh>
<v t="ekr.20060513122613.22" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>program</vh>
<v t="ekr.20060513122613.23" xcc_child_cfg="7d71002855104865616465724c696e654e756d626572710155013071025510536f757263654c696e654e756d62657271036802550b427265616b506f696e747371047d7105752e"><vh>Header Directives</vh></v>
<v t="ekr.20060513122613.24" xcc_child_cfg="7d71002855104865616465724c696e654e756d626572710155013571025510536f757263654c696e654e756d62657271035501347104550b427265616b506f696e747371057d71062855013171075507456e61626c65647108550231317109680875752e"><vh>int WINAPI WinMain(HINSTANCE hinstance,HINSTANCE hprevinstance,LPSTR lpcmdline,int ncmdshow);!</vh></v>
</v>
</v>
<v t="ekr.20060513122613.25" xcc_cfg="7d710028550a45786563757461626c6571017d710228550a446c6c2063616c6c65727103550071045513457865637574696f6e20617267756d656e747371056804755504436f64657106680455074144445f4c4f477107680455055469746c657108550b6763635f6764625f657865710955055761746368710a5d710b550161710c61550b427265616b706f696e7473710d7d710e2855056370703a38710f5507456e61626c6564711055066370703a3138711168107555075345545f4c4f4771125511406c616e677561676520632b2b0a20430a71135506494e4954454471145504547275657115550b427265616b506f696e747371167d71172855056370703a3871185507456e61626c6564711955066370703a3135711a5507456e61626c6564711b55066370703a3132711c5507456e61626c6564711d7555074f7074696f6e73711e7d711f28550b58636320766572626f7365712055045472756571215507457865637574657122550546616c73657123550c4372656174652066696c65737124550454727565712555105365656b20627265616b706f696e747371265504547275657127550f436f6e6e65637420746f2070697065712868045507436f6d70696c657129550454727565712a550d46696c746572206f7574707574712b550546616c7365712c55134175746f20696e636c75646520686561646572712d550454727565712e55054465627567712f550454727565713055105365656b206669727374206572726f7271315504547275657132755508446562756767657271337d713428550e4964656e7469667920627265616b71356804550f54617267657420706964207461736b713655327368656c6c207461736b6c697374202f6e68202f66692022494d4147454e414d45206571205f4e414d455f2e5f4558545f22713755085069706520656f6c713855025c6e71395509417267756d656e7473713a5519225f414253504154485f5c5c5f4e414d455f2e65786522200a713b550e50726f6d7074207061747465726e713c55035b295d713d550e5175657279206c6f636174696f6e713e550166713f550846696e6420706964714055215f4e414d455f5c2e5f4558545f202b283f503c5049443e5b302d395d2b29202e2b7141550b436c65617220627265616b71425513636c656172205f46494c455f3a5f4c494e455f714355084576616c75617465714455067072696e74207145550453746f707146550171714755045374657071485504737465707149550b4c69737420627265616b73714a680455045461736b714b5502710a714c550f427265616b20646574656374696f6e714d5516427265616b706f696e74205b302d395d2b2c202e2b0a714e550853746570206f7574714f550666696e6973687150550953657420627265616b71515513627265616b205f46494c455f3a5f4c494e455f7152550d46696e64206c6f636174696f6e7153552861742e2b5f4e414d455f5c2e283f503c4558543e2e2b293a283f503c4c494e453e5b302d395d2b29715455075374657020696e7155550473746570715668335518433a5c53444b5c4d696e47575c62696e5c6764622e65786571575512526567756c61722065787072657373696f6e7158550f50726f6772616d206578697465640a71595508436f6e74696e7565715a5508636f6e74696e7565715b5502476f715c550372756e715d550c53746172747570207461736b715e552e627265616b206d61696e0a736574206c69737473697a6520310a73657420636f6e6669726d206f66660a72756e0a715f550953746570206f766572716055046e6578747161755508436f6d70696c657271627d7163285514496e636c7564652073656172636820706174687371645515433a5c53444b5c4d696e47575c696e636c7564650a7165550f4572726f7220646574656374696f6e71665549283f503c46494c453e5b5e5c5c5d2b295c28283f503c4c494e453e5b302d395d2b295c29203a206572726f7220283f503c49443e435b302d395d2b293a20283f503c4445463e2e2b297167550b557365206c696272617279716855022d6c7169550e55736564206c6962726172696573716a6804550f446562756720617267756d656e7473716b555c225f414253504154485f5c5f4e414d455f2e5f5352434558545f220a2d6f225f414253504154485f5c5f4e414d455f2e5f4558545f220a5f494e4350415448535f0a2d670a5f4c494250415448535f0a5f4c49425241524945535f0a716c550d436865636b2073796e74617865716d55032f5a73716e550c4c6962726172792070617468716f55022d4c7170683a5559225f414253504154485f5c5f4e414d455f2e5f5352434558545f220a2d6f225f414253504154485f5c5f4e414d455f2e5f4558545f220a5f494e4350415448535f0a5f4c494250415448535f0a5f4c49425241524945535f0a717155094275696c6420646c6c717255032f4c447173550755736520706368717455032f5975717555094275696c6420657865717655032f4d4c717755144c6962726172792073656172636820706174687371785511433a5c53444b5c4d696e47575c6c69620a7179550c496e636c7564652070617468717a55022d49717b550b436f6d70696c6520706368717c55032f5963717d68625518433a5c53444b5c4d696e47575c62696e5c6763632e657865717e75752e"><vh>@xcc gcctest\testprog</vh>
<v t="ekr.20060513122613.22" xcc_child_cfg="7d7100550b427265616b506f696e747371017d7102732e"><vh>program</vh>
<v t="ekr.20060513122613.23" xcc_child_cfg="7d71002855104865616465724c696e654e756d626572710155013071025510536f757263654c696e654e756d62657271036802550b427265616b506f696e747371047d7105752e"><vh>Header Directives</vh></v>
<v t="ekr.20060513122613.24" xcc_child_cfg="7d71002855104865616465724c696e654e756d626572710155013571025510536f757263654c696e654e756d62657271035501347104550b427265616b506f696e747371057d71062855013171075507456e61626c65647108550231317109680875752e"><vh>int WINAPI WinMain(HINSTANCE hinstance,HINSTANCE hprevinstance,LPSTR lpcmdline,int ncmdshow);!</vh></v>
</v>
</v>
</v>
<v t="ekr.20060514125256"><vh>Recent</vh>
<v t="ekr.20060513122450.295"><vh>Selected Node Funcs</vh>
<v t="ekr.20060513122450.296"><vh>sGatherInfo NOT CALLED</vh>
<v t="ekr.20060513122450.297"><vh>Head</vh></v>
<v t="ekr.20060513122450.298"><vh>Dicts</vh></v>
<v t="ekr.20060513122450.299"><vh>File Creation</vh></v>
<v t="ekr.20060513122450.300"><vh>Compilation</vh></v>
<v t="ekr.20060513122450.301"><vh>Execution</vh></v>
<v t="ekr.20060513122450.302"><vh>Debugging</vh></v>
</v>
<v t="ekr.20060513122450.303" a="M"><vh>sExtractHeadInfo</vh></v>
<v t="ekr.20060513122450.304" a="M"><vh>sGetBrowseInfo</vh></v>
<v t="ekr.20060513122450.305" a="M"><vh>sGetWriteInfo</vh></v>
<v t="ekr.20060513122450.306" a="M"><vh>sGetCompileInfo</vh></v>
<v t="ekr.20060513122450.307" a="M"><vh>sGetDebugInfo</vh></v>
<v t="ekr.20060513122450.308" a="M"><vh>sGetExecInfo</vh></v>
<v t="ekr.20060513122450.309" a="M"><vh>sGoToError</vh></v>
<v t="ekr.20060513122450.310" a="M"><vh>sGo</vh></v>
<v t="ekr.20060513122450.311"><vh>sSet</vh></v>
<v t="ekr.20060513122450.312"><vh>sGet</vh></v>
<v t="ekr.20060513122450.313"><vh>sIsDict</vh></v>
<v t="ekr.20060513122450.314"><vh>sGetDict</vh></v>
<v t="ekr.20060513122450.315"><vh>sInitDict</vh></v>
<v t="ekr.20060513122450.316" a="M"><vh>sSelect</vh></v>
<v t="ekr.20060513122450.317"><vh>sSync</vh></v>
<v t="ekr.20060513122450.318" a="M"><vh>sShow</vh></v>
<v t="ekr.20060513122450.319" a="M"><vh>sHide</vh></v>
<v t="ekr.20060513122450.320" a="M"><vh>sSetText</vh></v>
<v t="ekr.20060513122450.321" a="M"><vh>sAddText</vh></v>
</v>
<v t="ekr.20060513122450.53"><vh>class ConfigClass</vh>
<v t="ekr.20060513122450.82" a="M"><vh>  __init__</vh></v>
<v t="ekr.20060513122450.54"><vh>  class PageClass</vh>
<v t="ekr.20060513122450.55"><vh>class CHECK</vh>
<v t="ekr.20060513122450.56" a="M"><vh>__init__</vh></v>
<v t="ekr.20060513122450.57"><vh>Get</vh></v>
<v t="ekr.20060513122450.58" a="M"><vh>Set</vh></v>
<v t="agp.20060728213822"><vh>UpdDpd</vh></v>
</v>
<v t="ekr.20060513122450.59"><vh>class ENTRY</vh>
<v t="ekr.20060513122450.60"><vh>__init__</vh></v>
<v t="ekr.20060513122450.61"><vh>Get</vh></v>
<v t="ekr.20060513122450.62"><vh>Set</vh></v>
</v>
<v t="ekr.20060513122450.63"><vh>class TEXT</vh>
<v t="ekr.20060513122450.64"><vh>__init__</vh></v>
<v t="ekr.20060513122450.65"><vh>Get</vh></v>
<v t="ekr.20060513122450.66"><vh>Set</vh></v>
</v>
<v t="ekr.20060513122450.67"><vh>class LABEL</vh>
<v t="ekr.20060513122450.68"><vh>__init__</vh></v>
</v>
<v t="ekr.20060513122450.69"><vh>class HELP</vh>
<v t="ekr.20060513122450.70"><vh>__init__</vh></v>
<v t="ekr.20060513122450.71"><vh>Help</vh></v>
</v>
<v t="ekr.20060513122450.72" a="M"><vh>__init__</vh></v>
<v t="ekr.20060513122450.73"><vh>AddObject</vh></v>
<v t="ekr.20060513122450.74"><vh>BBox</vh></v>
<v t="ekr.20060513122450.75"><vh>AddSep</vh></v>
<v t="ekr.20060513122450.76"><vh>CreateObjects</vh></v>
<v t="ekr.20060513122450.77"><vh>SaveObjects</vh></v>
<v t="ekr.20060513122450.78" a="M"><vh>LoadObjects</vh></v>
<v t="ekr.20060513122450.79" a="M"><vh>ClearObjects</vh></v>
<v t="ekr.20060513122450.80"><vh>Hide</vh></v>
<v t="ekr.20060513122450.81"><vh>Show</vh></v>
</v>
<v t="ekr.20060513122450.126"><vh> class CodePageClass</vh>
<v t="ekr.20060513122450.127"><vh>__init__</vh></v>
<v t="ekr.20060513122450.128"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.129"><vh>Entries</vh></v>
</v>
</v>
<v t="ekr.20060513122450.99"><vh> class CplPageClass</vh>
<v t="ekr.20060513122450.100"><vh>__init__</vh></v>
<v t="ekr.20060513122450.101" a="M"><vh>Browse</vh></v>
<v t="ekr.20060513122450.102" a="M"><vh>AddPath</vh></v>
<v t="ekr.20060513122450.103"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.104"><vh>Executable</vh></v>
<v t="ekr.20060513122450.105"><vh>Arguments</vh></v>
<v t="ekr.20060513122450.106" a="M"><vh>Paths</vh></v>
<v t="ekr.20060513122450.107" a="M"><vh>Symbols</vh></v>
<v t="ekr.20060513122450.108"><vh>Error Detection</vh></v>
</v>
</v>
<v t="ekr.20060513122450.109"><vh> class DbgPageClass</vh>
<v t="ekr.20060513122450.110"><vh>__init__</vh></v>
<v t="ekr.20060513122450.111" a="M"><vh>Browse</vh></v>
<v t="ekr.20060513122450.112"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.113"><vh>Executable</vh></v>
<v t="ekr.20060513122450.114"><vh>Arguments</vh></v>
<v t="ekr.20060513122450.115"><vh>Piping</vh></v>
<v t="ekr.20060513122450.116" a="M"><vh>Symbols</vh></v>
<v t="ekr.20060513122450.117"><vh>Startup Task</vh></v>
<v t="ekr.20060513122450.118"><vh>Target PID</vh></v>
<v t="ekr.20060513122450.119"><vh>Break info</vh></v>
<v t="ekr.20060513122450.120"><vh>Misc RE</vh></v>
</v>
</v>
<v t="ekr.20060513122450.121"><vh> class ExePageClass</vh>
<v t="ekr.20060513122450.122"><vh>__init__</vh></v>
<v t="ekr.20060513122450.123"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.124" a="M"><vh>Args</vh></v>
<v t="ekr.20060513122450.125" a="M"><vh>Dll Caller</vh></v>
<v t="agp.20070413002425"><vh>Piping</vh></v>
</v>
</v>
<v t="ekr.20060513122450.94"><vh> class OptPageClass</vh>
<v t="ekr.20060513122450.95" a="M"><vh>__init__</vh></v>
<v t="ekr.20060513122450.96"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.97" a="M"><vh>Actions Switches</vh></v>
<v t="ekr.20060513122450.98"><vh>Import</vh></v>
<v t="agp.20061016183631"><vh>Build</vh></v>
<v t="agp.20061016183631.1"><vh>Execution</vh></v>
<v t="agp.20061016183631.2"><vh>Output opts</vh></v>
<v t="agp.20070413150640"><vh>Load/Save</vh></v>
</v>
</v>
<v t="ekr.20060513122450.93" a="M"><vh>AddPages</vh></v>
<v t="ekr.20060513122450.92"><vh>Apply</vh></v>
<v t="ekr.20060513122450.87" a="M"><vh>ClearConfig</vh></v>
<v t="ekr.20060513122450.84"><vh>GetButton</vh></v>
<v t="ekr.20060513122450.83"><vh>GetPage</vh></v>
<v t="ekr.20060513122450.85" a="M"><vh>Hide</vh></v>
<v t="ekr.20060513122450.90"><vh>LoadFromFile</vh></v>
<v t="ekr.20060513122450.88"><vh>LoadFromNode</vh></v>
<v t="ekr.20060513122450.91"><vh>SaveToFile</vh></v>
<v t="ekr.20060513122450.89"><vh>SaveToNode</vh></v>
<v t="ekr.20060513122450.86" a="M"><vh>Show</vh></v>
<v t="agp.20061016193833"><vh> class LkrPageClass</vh>
<v t="agp.20061016193833.1"><vh>__init__</vh></v>
<v t="agp.20061016193833.2"><vh>Browse</vh></v>
<v t="agp.20061016193833.3"><vh>AddPath</vh></v>
<v t="agp.20061016193833.4"><vh>CreateObjects</vh>
<v t="agp.20061016193833.5"><vh>Executable</vh></v>
<v t="agp.20061016193833.6"><vh>Arguments</vh></v>
<v t="agp.20061016193833.7"><vh>Paths</vh></v>
<v t="agp.20061016193833.8"><vh>Symbols</vh></v>
<v t="agp.20061016193833.9"><vh>Error Detection</vh></v>
</v>
</v>
<v t="agp.20061016223957"><vh> class LangPageClass</vh>
<v t="agp.20061016223957.1"><vh>__init__</vh></v>
<v t="agp.20061016223957.2"><vh>CreateObjects</vh>
<v t="agp.20061016223957.3"><vh>Language</vh></v>
</v>
</v>
<v t="agp.20070506114337"><vh>WrapToPython</vh></v>
</v>
</v>
<v t="agp.20070109212533"><vh>thin xcc_nodes.py</vh>
<v t="ekr.20060513153648"><vh>Documentation</vh>
<v t="ekr.20060513122450.1"><vh>&lt;&lt; About this plugin &gt;&gt;</vh></v>
<v t="ekr.20060513183934"><vh>&lt;&lt; version history &gt;&gt;</vh></v>
<v t="ekr.20060514121335"><vh>&lt;&lt; what I did &gt;&gt;</vh></v>
<v t="agp.20070505102536"><vh>&lt;&lt; what was redid/undid &gt;&gt;</vh></v>
<v t="ekr.20060513122450.2"><vh>Known Flaws</vh></v>
<v t="ekr.20060513122450.3"><vh>Future Features</vh></v>
<v t="agp.20060520123624"><vh>Tracing Problems</vh></v>
<v t="agp.20061018012249"><vh>XCC Explanation</vh>
<v t="agp.20061018014003"><vh>The Three Distinctive Nodes</vh></v>
<v t="agp.20061018014003.1"><vh>The Parser</vh></v>
</v>
</v>
<v t="ekr.20060513122450.4"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="ekr.20060513122450.5"><vh>&lt;&lt; globals &gt;&gt;</vh>
<v t="ekr.20060513122450.16"><vh>Icons</vh>
<v t="ekr.20060513122450.17"><vh>Go</vh></v>
<v t="ekr.20060513122450.18"><vh>StepIn</vh></v>
<v t="ekr.20060513122450.19"><vh>StepOver</vh></v>
<v t="ekr.20060513122450.20"><vh>StepOut</vh></v>
<v t="ekr.20060513122450.21"><vh>Pause</vh></v>
<v t="ekr.20060513122450.22"><vh>Stop</vh></v>
<v t="agp.20060818192551"><vh>Doc</vh></v>
<v t="ekr.20060513122450.23"><vh>Watch</vh></v>
<v t="ekr.20060513122450.24"><vh>Config</vh></v>
<v t="ekr.20060513122450.25"><vh>Prompt</vh></v>
<v t="agp.20070505122726"><vh>Xcmd</vh></v>
</v>
<v t="ekr.20060513122450.26"><vh>Colors</vh></v>
</v>
<v t="ekr.20060513142641"><vh>Module level</vh>
<v t="ekr.20060513123144"><vh>init</vh></v>
<v t="ekr.20060513122450.395"><vh>Module-level event handlers</vh>
<v t="ekr.20060513122450.397"><vh>OnCreate</vh></v>
<v t="ekr.20060513122450.396"><vh>OnStart2 (No longer used)</vh></v>
<v t="ekr.20060513122450.398"><vh>OnSelect2</vh></v>
<v t="ekr.20060513122450.399"><vh>OnIdle</vh></v>
<v t="ekr.20060513122450.400"><vh>OnCommand2</vh></v>
<v t="ekr.20060513122450.401"><vh>OnBodyDoubleClick</vh></v>
<v t="ekr.20060513122450.402"><vh>OnBodyKey2</vh></v>
<v t="ekr.20060513122450.403"><vh>OnHeadKey2</vh></v>
<v t="ekr.20060513122450.404"><vh>OnQuit</vh></v>
</v>
<v t="ekr.20060513160819"><vh>pause &amp; helpers</vh>
<v t="ekr.20060513122450.28"><vh>winPause</vh></v>
<v t="ekr.20060513122450.29"><vh>linPause</vh></v>
</v>
<v t="ekr.20060513142641.1"><vh>Helpers</vh>
<v t="agp.20070207022338"><vh>StrToBool</vh></v>
<v t="ekr.20060513122450.33"><vh>AddText</vh></v>
<v t="ekr.20060513122450.41"><vh>CompressIcon</vh></v>
<v t="ekr.20060513122450.40"><vh>DecompressIcon</vh></v>
<v t="ekr.20060513122450.34"><vh>Error</vh></v>
<v t="ekr.20060513122450.38"><vh>GetDictKey</vh></v>
<v t="ekr.20060513122450.32"><vh>GetNodePath</vh></v>
<v t="ekr.20060513122450.389"><vh>GetXccNode</vh></v>
<v t="ekr.20060513122450.394"><vh>ImportFiles</vh></v>
<v t="ekr.20060513122450.390"><vh>IsXcc</vh></v>
<v t="agp.20060520121647"><vh>HasXccDict</vh></v>
<v t="ekr.20060513122450.36"><vh>Message</vh></v>
<v t="ekr.20060513122450.39"><vh>TraceBack</vh></v>
<v t="ekr.20060513122450.35"><vh>Warning</vh></v>
<v t="agp.20060817135048"><vh>C++ parsing</vh>
<v t="agp.20060817135048.1"><vh>SplitFunc</vh></v>
<v t="agp.20060818115955"><vh>SplitParams</vh></v>
</v>
</v>
</v>
<v t="ekr.20060513122450.42"><vh>Classes</vh>
<v t="ekr.20060513141418"><vh>class controllerClass</vh>
<v t="ekr.20060513142641.2"><vh>__init__</vh>
<v t="ekr.20060513122450.7"><vh>Xcc Core</vh></v>
<v t="ekr.20060513122450.8"><vh>Browse Info</vh></v>
<v t="agp.20060727203322"><vh>Write Info</vh></v>
<v t="ekr.20060513122450.10"><vh>Compile Info</vh></v>
<v t="ekr.20060513122450.11"><vh>Debug Info</vh></v>
<v t="ekr.20060513122450.12"><vh>Execute Info</vh></v>
<v t="ekr.20060513122450.13"><vh>Options</vh></v>
<v t="agp.20060521091102"><vh>Code Decorations</vh></v>
<v t="agp.20060520150529"><vh>Leo's Controls shortcut</vh></v>
<v t="ekr.20060513122450.14"><vh>Widgets</vh></v>
</v>
<v t="ekr.20060513152023"><vh>Event handlers</vh>
<v t="ekr.20060513152032.3"><vh>onSelect</vh></v>
<v t="ekr.20060513152032.4"><vh>onIdle</vh></v>
<v t="ekr.20060513152032.5"><vh>onCommand2</vh></v>
<v t="ekr.20060513152032.6"><vh>onBodyDoubleClick</vh></v>
<v t="ekr.20060513152032.7"><vh>onBodyKey2</vh></v>
<v t="ekr.20060513152032.8"><vh>onHeadKey2</vh></v>
<v t="ekr.20060513152032.9"><vh>onQuit</vh></v>
</v>
<v t="ekr.20060514122829"><vh>Utility</vh>
<v t="ekr.20060513122450.31"><vh>GoToNode</vh></v>
<v t="ekr.20060513122450.392"><vh>UpdateProcess</vh></v>
<v t="agp.20060520141401"><vh>ReplaceVars</vh></v>
<v t="agp.20060521153231"><vh>GetUnknownAttributes</vh></v>
<v t="agp.20070413213649"><vh>HideWidgets</vh></v>
</v>
<v t="ekr.20060513122450.322"><vh>Child Node Funcs</vh>
<v t="ekr.20060513122450.323"><vh>cIs</vh></v>
<v t="ekr.20060513122450.324"><vh>cSet</vh></v>
<v t="ekr.20060513122450.325"><vh>cGet</vh></v>
<v t="ekr.20060513122450.326"><vh>cSelect</vh></v>
<v t="ekr.20060513122450.327"><vh>cGetDict</vh></v>
</v>
<v t="ekr.20060513122450.295"><vh>Selected Node Funcs</vh>
<v t="ekr.20060513122450.296"><vh>sGatherInfo NOT CALLED</vh>
<v t="ekr.20060513122450.297"><vh>Head</vh></v>
<v t="ekr.20060513122450.298"><vh>Dicts</vh></v>
<v t="ekr.20060513122450.299"><vh>File Creation</vh></v>
<v t="ekr.20060513122450.300"><vh>Compilation</vh></v>
<v t="ekr.20060513122450.301"><vh>Execution</vh></v>
<v t="ekr.20060513122450.302"><vh>Debugging</vh></v>
</v>
<v t="ekr.20060513122450.303" a="M"><vh>sExtractHeadInfo</vh></v>
<v t="ekr.20060513122450.304" a="M"><vh>sGetBrowseInfo</vh></v>
<v t="ekr.20060513122450.305" a="M"><vh>sGetWriteInfo</vh></v>
<v t="ekr.20060513122450.306" a="M"><vh>sGetCompileInfo</vh></v>
<v t="ekr.20060513122450.307" a="M"><vh>sGetDebugInfo</vh></v>
<v t="ekr.20060513122450.308" a="M"><vh>sGetExecInfo</vh></v>
<v t="ekr.20060513122450.309" a="M"><vh>sGoToError</vh></v>
<v t="ekr.20060513122450.310" a="M"><vh>sGo</vh></v>
<v t="ekr.20060513122450.311"><vh>sSet</vh></v>
<v t="ekr.20060513122450.312"><vh>sGet</vh></v>
<v t="ekr.20060513122450.313"><vh>sIsDict</vh></v>
<v t="ekr.20060513122450.314"><vh>sGetDict</vh></v>
<v t="ekr.20060513122450.315"><vh>sInitDict</vh></v>
<v t="ekr.20060513122450.316" a="M"><vh>sSelect</vh></v>
<v t="ekr.20060513122450.317"><vh>sSync</vh></v>
<v t="ekr.20060513122450.318" a="M"><vh>sShow</vh></v>
<v t="ekr.20060513122450.319" a="M"><vh>sHide</vh></v>
<v t="ekr.20060513122450.320" a="M"><vh>sSetText</vh></v>
<v t="ekr.20060513122450.321" a="M"><vh>sAddText</vh></v>
</v>
<v t="ekr.20060513122450.281"><vh>Active Node Funcs</vh>
<v t="ekr.20060513122450.282"><vh>aSet</vh></v>
<v t="ekr.20060513122450.283"><vh>aGet</vh></v>
<v t="ekr.20060513122450.284"><vh>aGetDict</vh></v>
<v t="ekr.20060513122450.285"><vh>aGo</vh></v>
<v t="ekr.20060513122450.286"><vh>aStop</vh></v>
<v t="ekr.20060513122450.287"><vh>aStepIn</vh></v>
<v t="ekr.20060513122450.288"><vh>aStepOver</vh></v>
<v t="ekr.20060513122450.289"><vh>aStepOut</vh></v>
<v t="ekr.20060513122450.290"><vh>aPause</vh></v>
<v t="ekr.20060513122450.291"><vh>aWrite</vh></v>
<v t="ekr.20060513122450.292"><vh>aSelect</vh></v>
<v t="ekr.20060513122450.293"><vh>aSetText</vh></v>
<v t="ekr.20060513122450.294"><vh>aAddText</vh></v>
</v>
<v t="ekr.20060513122450.328"><vh>Action Funcs</vh>
<v t="agp.20070206130657"><vh>ParseTree</vh></v>
<v t="ekr.20060513122450.329"><vh>CreateFiles</vh></v>
<v t="ekr.20060513122450.330"><vh>Compile</vh></v>
<v t="ekr.20060513122450.331"><vh>CplCmd</vh>
<v t="ekr.20060513122450.332"><vh>_INCPATHS_</vh></v>
<v t="ekr.20060513122450.333"><vh>_LIBPATHS_</vh></v>
<v t="ekr.20060513122450.334"><vh>_LIBRARIES_</vh></v>
<v t="ekr.20060513122450.335"><vh>_BUILD_</vh></v>
</v>
<v t="agp.20061016210621"><vh>Link</vh></v>
<v t="agp.20061016211035"><vh>LkrCmd</vh>
<v t="agp.20061016211035.1"><vh>_LIBPATHS_</vh></v>
<v t="agp.20061016211035.2"><vh>_LIBRARIES_</vh></v>
<v t="agp.20061016211035.3"><vh>_BUILD_</vh></v>
</v>
<v t="ekr.20060513122450.336"><vh>Debug</vh></v>
<v t="ekr.20060513122450.337"><vh>DbgCmd</vh></v>
<v t="ekr.20060513122450.338"><vh>Execute</vh></v>
<v t="agp.20061016210621.1"><vh>RunTool</vh></v>
</v>
<v t="ekr.20060513122450.339"><vh>Compiler Events</vh>
<v t="ekr.20060513122450.340"><vh>CplStart</vh></v>
<v t="ekr.20060513122450.341"><vh>CplOut</vh></v>
<v t="ekr.20060513122450.342"><vh>CplErr</vh></v>
<v t="ekr.20060513122450.343"><vh>CplEnd</vh></v>
</v>
<v t="agp.20070205104231"><vh>Linker Events</vh>
<v t="agp.20070205104231.1"><vh>LkrStart</vh></v>
<v t="agp.20070205104231.2"><vh>LkrOut</vh></v>
<v t="agp.20070205104231.3"><vh>LkrErr</vh></v>
<v t="agp.20070205104231.4"><vh>LkrEnd</vh></v>
</v>
<v t="ekr.20060513122450.344"><vh>Debugger Events</vh>
<v t="ekr.20060513122450.379"><vh>DbgStart</vh></v>
<v t="ekr.20060513122450.380"><vh>DbgOut</vh></v>
<v t="ekr.20060513122450.381"><vh>DbgErr</vh></v>
<v t="ekr.20060513122450.382"><vh>DbgEnd</vh></v>
</v>
<v t="ekr.20060513122450.383"><vh>Program Events</vh>
<v t="ekr.20060513122450.384"><vh>ProgStart</vh></v>
<v t="ekr.20060513122450.385"><vh>ProgOut</vh></v>
<v t="ekr.20060513122450.386"><vh>ProgErr</vh></v>
<v t="ekr.20060513122450.387"><vh>ProgEnd</vh></v>
</v>
</v>
<v t="ekr.20060513122450.345"><vh>Debugger task classes</vh>
<v t="ekr.20060513122450.346"><vh>DbgTaskClass</vh>
<v t="ekr.20060513122450.347"><vh>__init__</vh></v>
<v t="ekr.20060513122450.348"><vh>Send</vh></v>
</v>
<v t="ekr.20060513122450.349"><vh>OutputTaskClass</vh>
<v t="ekr.20060513122450.350"><vh>__init__</vh></v>
<v t="ekr.20060513122450.351"><vh>Send</vh></v>
<v t="ekr.20060513122450.352"><vh>Receive</vh></v>
</v>
<v t="ekr.20060513122450.353"><vh>TargetPidTaskClass</vh>
<v t="ekr.20060513122450.354"><vh>__init__</vh></v>
<v t="ekr.20060513122450.355"><vh>Send</vh></v>
<v t="ekr.20060513122450.356"><vh>Receive</vh></v>
</v>
<v t="ekr.20060513122450.357"><vh>BreakTaskClass</vh>
<v t="ekr.20060513122450.358"><vh>__init__</vh></v>
<v t="ekr.20060513122450.359"><vh>Send</vh></v>
<v t="ekr.20060513122450.360"><vh>Receive</vh></v>
</v>
<v t="ekr.20060513122450.361"><vh>RegExpTaskClass</vh>
<v t="ekr.20060513122450.362"><vh>__init__</vh></v>
<v t="ekr.20060513122450.363"><vh>Send</vh></v>
<v t="ekr.20060513122450.364"><vh>Receive</vh></v>
</v>
<v t="ekr.20060513122450.365"><vh>WatchTaskClass</vh>
<v t="ekr.20060513122450.366"><vh>__init__</vh></v>
<v t="ekr.20060513122450.367"><vh>Cancel</vh></v>
<v t="ekr.20060513122450.368"><vh>Send</vh></v>
<v t="ekr.20060513122450.369"><vh>Receive</vh></v>
<v t="ekr.20060513122450.370"><vh>OnPrompt</vh></v>
</v>
<v t="agp.20070413223141"><vh>DasmTaskClass</vh>
<v t="agp.20070413223141.1"><vh>__init__</vh></v>
<v t="agp.20070413223141.2"><vh>Cancel</vh></v>
<v t="agp.20070413223141.3"><vh>Send</vh></v>
<v t="agp.20070413223141.4"><vh>Receive</vh></v>
<v t="agp.20070413224924"><vh>OnPrompt</vh></v>
</v>
<v t="ekr.20060513122450.371"><vh>QueryGoTaskClass</vh>
<v t="ekr.20060513122450.372"><vh>__init__</vh></v>
<v t="ekr.20060513122450.373"><vh>Send</vh></v>
<v t="ekr.20060513122450.374"><vh>Receive</vh></v>
</v>
<v t="ekr.20060513122450.375"><vh>BreakIdTaskClass</vh>
<v t="ekr.20060513122450.376"><vh>__init__</vh></v>
<v t="ekr.20060513122450.377"><vh>Send</vh></v>
<v t="ekr.20060513122450.378"><vh>Receive</vh></v>
</v>
</v>
<v t="ekr.20060513122450.43"><vh>class ProcessClass</vh>
<v t="ekr.20060513122450.44"><vh>class ReadingThreadClass</vh>
<v t="ekr.20060513122450.45"><vh>__init__</vh></v>
<v t="ekr.20060513122450.46"><vh>run</vh></v>
<v t="ekr.20060513122450.47"><vh>Update</vh></v>
</v>
<v t="ekr.20060513122450.48"><vh>__init__</vh></v>
<v t="ekr.20060513122450.49"><vh>Open</vh></v>
<v t="ekr.20060513122450.50"><vh>Close</vh></v>
<v t="ekr.20060513122450.51"><vh>Update</vh></v>
<v t="agp.20061016193303"><vh>QueueProcess</vh></v>
</v>
<v t="ekr.20060513122450.52"><vh>Widget classes</vh>
<v t="ekr.20060513122450.53"><vh>class ConfigClass</vh>
<v t="ekr.20060513122450.82" a="M"><vh>  __init__</vh></v>
<v t="ekr.20060513122450.54"><vh>  class PageClass</vh>
<v t="ekr.20060513122450.55"><vh>class CHECK</vh>
<v t="ekr.20060513122450.56" a="M"><vh>__init__</vh></v>
<v t="ekr.20060513122450.57"><vh>Get</vh></v>
<v t="ekr.20060513122450.58" a="M"><vh>Set</vh></v>
<v t="agp.20060728213822"><vh>UpdDpd</vh></v>
</v>
<v t="ekr.20060513122450.59"><vh>class ENTRY</vh>
<v t="ekr.20060513122450.60"><vh>__init__</vh></v>
<v t="ekr.20060513122450.61"><vh>Get</vh></v>
<v t="ekr.20060513122450.62"><vh>Set</vh></v>
</v>
<v t="ekr.20060513122450.63"><vh>class TEXT</vh>
<v t="ekr.20060513122450.64"><vh>__init__</vh></v>
<v t="ekr.20060513122450.65"><vh>Get</vh></v>
<v t="ekr.20060513122450.66"><vh>Set</vh></v>
</v>
<v t="ekr.20060513122450.67"><vh>class LABEL</vh>
<v t="ekr.20060513122450.68"><vh>__init__</vh></v>
</v>
<v t="ekr.20060513122450.69"><vh>class HELP</vh>
<v t="ekr.20060513122450.70"><vh>__init__</vh></v>
<v t="ekr.20060513122450.71"><vh>Help</vh></v>
</v>
<v t="ekr.20060513122450.72" a="M"><vh>__init__</vh></v>
<v t="ekr.20060513122450.73"><vh>AddObject</vh></v>
<v t="ekr.20060513122450.74"><vh>BBox</vh></v>
<v t="ekr.20060513122450.75"><vh>AddSep</vh></v>
<v t="ekr.20060513122450.76"><vh>CreateObjects</vh></v>
<v t="ekr.20060513122450.77"><vh>SaveObjects</vh></v>
<v t="ekr.20060513122450.78" a="M"><vh>LoadObjects</vh></v>
<v t="ekr.20060513122450.79" a="M"><vh>ClearObjects</vh></v>
<v t="ekr.20060513122450.80"><vh>Hide</vh></v>
<v t="ekr.20060513122450.81"><vh>Show</vh></v>
</v>
<v t="ekr.20060513122450.126"><vh> class CodePageClass</vh>
<v t="ekr.20060513122450.127"><vh>__init__</vh></v>
<v t="ekr.20060513122450.128"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.129"><vh>Entries</vh></v>
</v>
</v>
<v t="ekr.20060513122450.99"><vh> class CplPageClass</vh>
<v t="ekr.20060513122450.100"><vh>__init__</vh></v>
<v t="ekr.20060513122450.101" a="M"><vh>Browse</vh></v>
<v t="ekr.20060513122450.102" a="M"><vh>AddPath</vh></v>
<v t="ekr.20060513122450.103"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.104"><vh>Executable</vh></v>
<v t="ekr.20060513122450.105"><vh>Arguments</vh></v>
<v t="ekr.20060513122450.106" a="M"><vh>Paths</vh></v>
<v t="ekr.20060513122450.107" a="M"><vh>Symbols</vh></v>
<v t="ekr.20060513122450.108"><vh>Error Detection</vh></v>
</v>
</v>
<v t="ekr.20060513122450.109"><vh> class DbgPageClass</vh>
<v t="ekr.20060513122450.110"><vh>__init__</vh></v>
<v t="ekr.20060513122450.111" a="M"><vh>Browse</vh></v>
<v t="ekr.20060513122450.112"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.113"><vh>Executable</vh></v>
<v t="ekr.20060513122450.114"><vh>Arguments</vh></v>
<v t="ekr.20060513122450.115"><vh>Piping</vh></v>
<v t="ekr.20060513122450.116" a="M"><vh>Symbols</vh></v>
<v t="ekr.20060513122450.117"><vh>Startup Task</vh></v>
<v t="ekr.20060513122450.118"><vh>Target PID</vh></v>
<v t="ekr.20060513122450.119"><vh>Break info</vh></v>
<v t="ekr.20060513122450.120"><vh>Misc RE</vh></v>
</v>
</v>
<v t="ekr.20060513122450.121"><vh> class ExePageClass</vh>
<v t="ekr.20060513122450.122"><vh>__init__</vh></v>
<v t="ekr.20060513122450.123"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.124" a="M"><vh>Args</vh></v>
<v t="ekr.20060513122450.125" a="M"><vh>Dll Caller</vh></v>
<v t="agp.20070413002425"><vh>Piping</vh></v>
</v>
</v>
<v t="ekr.20060513122450.94"><vh> class OptPageClass</vh>
<v t="ekr.20060513122450.95" a="M"><vh>__init__</vh></v>
<v t="ekr.20060513122450.96"><vh>CreateObjects</vh>
<v t="ekr.20060513122450.97" a="M"><vh>Actions Switches</vh></v>
<v t="ekr.20060513122450.98"><vh>Import</vh></v>
<v t="agp.20061016183631"><vh>Build</vh></v>
<v t="agp.20061016183631.1"><vh>Execution</vh></v>
<v t="agp.20061016183631.2"><vh>Output opts</vh></v>
<v t="agp.20070413150640"><vh>Load/Save</vh></v>
</v>
</v>
<v t="ekr.20060513122450.93" a="M"><vh>AddPages</vh></v>
<v t="ekr.20060513122450.92"><vh>Apply</vh></v>
<v t="ekr.20060513122450.87" a="M"><vh>ClearConfig</vh></v>
<v t="ekr.20060513122450.84"><vh>GetButton</vh></v>
<v t="ekr.20060513122450.83"><vh>GetPage</vh></v>
<v t="ekr.20060513122450.85" a="M"><vh>Hide</vh></v>
<v t="ekr.20060513122450.90"><vh>LoadFromFile</vh></v>
<v t="ekr.20060513122450.88"><vh>LoadFromNode</vh></v>
<v t="ekr.20060513122450.91"><vh>SaveToFile</vh></v>
<v t="ekr.20060513122450.89"><vh>SaveToNode</vh></v>
<v t="ekr.20060513122450.86" a="M"><vh>Show</vh></v>
<v t="agp.20061016193833"><vh> class LkrPageClass</vh>
<v t="agp.20061016193833.1"><vh>__init__</vh></v>
<v t="agp.20061016193833.2"><vh>Browse</vh></v>
<v t="agp.20061016193833.3"><vh>AddPath</vh></v>
<v t="agp.20061016193833.4"><vh>CreateObjects</vh>
<v t="agp.20061016193833.5"><vh>Executable</vh></v>
<v t="agp.20061016193833.6"><vh>Arguments</vh></v>
<v t="agp.20061016193833.7"><vh>Paths</vh></v>
<v t="agp.20061016193833.8"><vh>Symbols</vh></v>
<v t="agp.20061016193833.9"><vh>Error Detection</vh></v>
</v>
</v>
<v t="agp.20061016223957"><vh> class LangPageClass</vh>
<v t="agp.20061016223957.1"><vh>__init__</vh></v>
<v t="agp.20061016223957.2"><vh>CreateObjects</vh>
<v t="agp.20061016223957.3"><vh>Language</vh></v>
</v>
</v>
<v t="agp.20070506114337"><vh>WrapToPython</vh></v>
</v>
<v t="ekr.20060513122450.151"><vh>class ToolbarClass</vh>
<v t="ekr.20060513122450.152"><vh>__init__</vh></v>
<v t="ekr.20060513122450.153"><vh>Go</vh></v>
<v t="ekr.20060513122450.154"><vh>Hide</vh></v>
<v t="ekr.20060513122450.155"><vh>Show</vh></v>
<v t="ekr.20060513122450.156"><vh>OnKey</vh></v>
<v t="ekr.20060513122450.157"><vh>EnableStep</vh></v>
<v t="ekr.20060513122450.158"><vh>DisableStep</vh></v>
<v t="ekr.20060513122450.159"><vh>SyncDisplayToChild</vh></v>
<v t="ekr.20060513122450.160"><vh>SyncDisplayToError</vh></v>
<v t="ekr.20060513122450.161"><vh>SetError</vh></v>
<v t="ekr.20060513122450.162"><vh>OnErrorLeftClick</vh></v>
<v t="ekr.20060513122450.163"><vh>HideInput</vh></v>
<v t="ekr.20060513122450.164"><vh>ShowInput</vh></v>
<v t="ekr.20060513122450.165"><vh>Refresh</vh></v>
</v>
<v t="ekr.20060513122450.166"><vh>class WatcherClass</vh>
<v t="ekr.20060513122450.167"><vh>__init__</vh></v>
<v t="ekr.20060513122450.168"><vh>OnEditKey</vh></v>
<v t="ekr.20060513122450.169"><vh>OnLeftClick</vh></v>
<v t="ekr.20060513122450.170"><vh>OnDelete</vh></v>
<v t="ekr.20060513122450.171"><vh>yview</vh></v>
<v t="ekr.20060513122450.172"><vh>Hide</vh></v>
<v t="ekr.20060513122450.173"><vh>Show</vh></v>
<v t="ekr.20060513122450.174"><vh>Sync</vh></v>
</v>
<v t="agp.20070413211057"><vh>class DasmClass</vh>
<v t="agp.20070413211057.1"><vh>__init__</vh></v>
<v t="agp.20070413211057.6"><vh>Hide</vh></v>
<v t="agp.20070413211057.7"><vh>Show</vh></v>
<v t="agp.20070413211057.8"><vh>Sync</vh></v>
</v>
<v t="ekr.20060513122450.175"><vh>class BreakbarClass</vh>
<v t="ekr.20060513122450.176"><vh>__init__</vh></v>
<v t="ekr.20060513122450.177"><vh>Scrollbar funcs</vh>
<v t="ekr.20060513122450.178"><vh>yview</vh></v>
<v t="ekr.20060513122450.179"><vh>setForBody</vh></v>
<v t="ekr.20060513122450.180"><vh>setForBar</vh></v>
<v t="ekr.20060513122450.181"><vh>Plug</vh></v>
<v t="ekr.20060513122450.182"><vh>UnPlug</vh></v>
</v>
<v t="ekr.20060513122450.183"><vh>Events</vh>
<v t="ekr.20060513122450.186"><vh>OnRightClick</vh></v>
<v t="ekr.20060513122450.187"><vh>OnLeftClick</vh></v>
<v t="ekr.20060513122450.209"><vh>IdleUpdate</vh></v>
</v>
<v t="ekr.20060513122450.188"><vh>Node breaks</vh>
<v t="ekr.20060513122450.189"><vh>AddNodeBreak</vh></v>
<v t="ekr.20060513122450.190"><vh>DeleteNodeBreak</vh></v>
<v t="ekr.20060513122450.191"><vh>ClearNodeBreaks</vh></v>
<v t="ekr.20060513122450.192"><vh>BreaksFromNode</vh></v>
</v>
<v t="ekr.20060513122450.193"><vh>Bar Breaks</vh>
<v t="ekr.20060513122450.194"><vh>AddBarBreak</vh></v>
<v t="ekr.20060513122450.195"><vh>DeleteBarBreak</vh></v>
<v t="ekr.20060513122450.196"><vh>ClearBarBreaks</vh></v>
</v>
<v t="ekr.20060513122450.197"><vh>tag breaks</vh>
<v t="ekr.20060513122450.198"><vh>AddBreakTag</vh></v>
<v t="ekr.20060513122450.199"><vh>DeleteBreakTag</vh></v>
<v t="ekr.20060513122450.200"><vh>ClearBreakTags</vh></v>
<v t="ekr.20060513122450.201"><vh>BreaksFromTags</vh></v>
</v>
<v t="ekr.20060513122450.202"><vh>AddBreak</vh></v>
<v t="ekr.20060513122450.203"><vh>DeleteBreak</vh></v>
<v t="ekr.20060513122450.204"><vh>DeleteNodeBreaks</vh></v>
<v t="ekr.20060513122450.205"><vh>DeleteProjectBreaks</vh></v>
<v t="ekr.20060513122450.206"><vh>Hide</vh></v>
<v t="ekr.20060513122450.207"><vh>Show</vh></v>
<v t="ekr.20060513122450.208"><vh>Sync</vh></v>
<v t="ekr.20060513122450.210"><vh>Cancel</vh></v>
</v>
<v t="agp.20060729210351"><vh>class DocEditClass</vh>
<v t="agp.20060729210351.1"><vh>__init__</vh>
<v t="agp.20060730222036"><vh>TopBar</vh></v>
<v t="agp.20060730222036.1"><vh>New Topic</vh></v>
<v t="agp.20060730222036.2"><vh>Use Head</vh></v>
<v t="agp.20070519110410"><vh>Pre Format</vh></v>
</v>
<v t="agp.20060729210351.2"><vh>Show</vh></v>
<v t="agp.20060729210351.3"><vh>Hide</vh></v>
<v t="agp.20060729215923"><vh>LoadFromNode</vh></v>
<v t="agp.20060729215923.1"><vh>SaveToNode</vh></v>
<v t="agp.20060729230915"><vh>OnKeyRelease</vh></v>
</v>
<v t="agp.20061016184055"><vh>HELP</vh>
<v t="agp.20061014201056"><vh>Options</vh>
<v t="agp.20061014201056.1"><vh>BuildSequence</vh></v>
</v>
<v t="ekr.20060513122450.140"><vh>Compiler</vh>
<v t="ekr.20060513122450.141"><vh>CplArgumentsHelp</vh></v>
<v t="ekr.20060513122450.142"><vh>CplDebugArgumentsHelp</vh></v>
<v t="ekr.20060513122450.143"><vh>IncludeSearchPathsHelp</vh></v>
<v t="ekr.20060513122450.144"><vh>LibrarySearchPathsHelp</vh></v>
<v t="ekr.20060513122450.145"><vh>UsedLibrariesHelp</vh></v>
<v t="ekr.20060513122450.146"><vh>IncludePathAndLibraryPathHelp</vh></v>
<v t="ekr.20060513122450.147"><vh>UseLibraryAndCheckSyntaxeHelp</vh></v>
<v t="ekr.20060513122450.148"><vh>BuildExeAndBuildDllHelp</vh></v>
<v t="ekr.20060513122450.149"><vh>CompilePchAndUsePchHelp</vh></v>
<v t="ekr.20060513122450.150"><vh>ErrorDetectionHelp</vh></v>
</v>
<v t="ekr.20060513122450.130"><vh>Debugger</vh>
<v t="ekr.20060513122450.131"><vh>DbgArgumentsHelp</vh></v>
<v t="ekr.20060513122450.132"><vh>DbgPipingHelp</vh></v>
<v t="ekr.20060513122450.133"><vh>DbgStartupTaskHelp</vh></v>
<v t="ekr.20060513122450.134"><vh>DbgTargetPidHelp</vh></v>
<v t="ekr.20060513122450.135"><vh>DbgBreakDetectionHelp</vh></v>
<v t="ekr.20060513122450.136"><vh>DbgSetClearBreakHelp</vh></v>
<v t="ekr.20060513122450.137"><vh>DbgBreakIdHelp</vh></v>
<v t="ekr.20060513122450.138"><vh>DbgLocationHelp</vh></v>
<v t="ekr.20060513122450.139"><vh>DbgMiscExpHelp</vh></v>
</v>
</v>
</v>
<v t="ekr.20060513122450.211"><vh>Parsing classes</vh>
<v t="ekr.20060513122450.212"><vh>ParserClass</vh>
<v t="ekr.20060513122450.213"><vh>Rules</vh>
<v t="ekr.20060513122450.214"><vh>LoadCppRules</vh></v>
<v t="agp.20060821215115"><vh>ATRULE</vh>
<v t="agp.20060821215115.2"><vh>Match</vh></v>
<v t="agp.20060821215115.3"><vh>OnMatch</vh></v>
</v>
<v t="ekr.20060513122450.218"><vh>COMMENTRULE</vh>
<v t="ekr.20060513225814"><vh>ctor</vh></v>
<v t="ekr.20060513122450.219"><vh>Match</vh></v>
<v t="ekr.20060513122450.220"><vh>OnMatch</vh></v>
</v>
<v t="ekr.20060513122450.221"><vh>FUNCRULE</vh>
<v t="ekr.20060513225814.1"><vh>ctor</vh></v>
<v t="ekr.20060513122450.222"><vh>Match</vh></v>
<v t="ekr.20060513122450.223"><vh>OnMatch</vh></v>
<v t="ekr.20060513122450.224"><vh>DeclareFunc</vh></v>
<v t="agp.20060817145617"><vh>DefineFunc</vh>
<v t="agp.20060817171700"><vh>doc</vh>
<v t="agp.20060817171112"><vh>core</vh></v>
</v>
</v>
</v>
<v t="ekr.20060513122450.226"><vh>CLASSRULE</vh>
<v t="ekr.20060513225814.2"><vh>ctor</vh></v>
<v t="ekr.20060513122450.227"><vh>Match</vh></v>
<v t="ekr.20060513122450.228"><vh>OnMatch</vh></v>
</v>
<v t="ekr.20060513122450.229"><vh>DEFAULTRULE</vh>
<v t="ekr.20060513122450.230"><vh>__init__</vh></v>
<v t="ekr.20060513122450.231"><vh>Match</vh></v>
<v t="ekr.20060513122450.232"><vh>OnMatch</vh></v>
</v>
<v t="ekr.20060513122450.233"><vh>FUNCCOMMENTRULE</vh>
<v t="ekr.20060513122450.234"><vh>__init__</vh></v>
<v t="ekr.20060513122450.235"><vh>Match</vh></v>
<v t="ekr.20060513122450.236"><vh>OnMatch</vh></v>
</v>
<v t="AGP.20201210160828"><vh>FUNCASMRULE</vh>
<v t="AGP.20201210160828.1"><vh>__init__</vh></v>
<v t="AGP.20201210160828.2"><vh>Match</vh></v>
<v t="AGP.20201210160828.3"><vh>OnMatch</vh></v>
</v>
<v t="ekr.20060513122450.237"><vh>FUNCDEFAULTRULE</vh>
<v t="ekr.20060513122450.238"><vh>__init__</vh></v>
<v t="ekr.20060513122450.239"><vh>Match</vh></v>
<v t="ekr.20060513122450.240"><vh>OnMatch</vh></v>
</v>
</v>
<v t="ekr.20060513122450.241"><vh>__init__</vh></v>
<v t="ekr.20060513122450.242"><vh>Declare</vh></v>
<v t="ekr.20060513122450.243"><vh>Define</vh></v>
<v t="ekr.20060513122450.254"><vh>WriteOthers</vh></v>
<v t="AGP.20201210161232"><vh>WriteOthers_asm</vh></v>
<v t="ekr.20060513122450.245"><vh>PushBodyLine</vh></v>
<v t="ekr.20060513122450.246"><vh>PopBodyLine</vh></v>
<v t="ekr.20060513122450.255"><vh>Parse</vh></v>
<v t="ekr.20060513122450.257"><vh>ParseNode</vh></v>
<v t="ekr.20060513122450.256"><vh>OnParseNode</vh></v>
<v t="agp.20070506104706"><vh>OnFunc</vh></v>
<v t="ekr.20060513122450.248"><vh>Tabing</vh>
<v t="ekr.20060513122450.249"><vh>Tab</vh></v>
<v t="ekr.20060513122450.250"><vh>UnTab</vh></v>
<v t="ekr.20060513122450.251"><vh>PushTab</vh></v>
<v t="ekr.20060513122450.252"><vh>PopTab</vh></v>
<v t="ekr.20060513122450.253"><vh>TabWrite</vh></v>
<v t="AGP.20201210161442"><vh>TabWrite_asm</vh></v>
</v>
<v t="agp.20070206234855"><vh>Documentation</vh>
<v t="ekr.20060513122450.244"><vh>Docum</vh></v>
<v t="agp.20060724212618"><vh>PushDoc</vh></v>
<v t="agp.20060724213508"><vh>PopDoc</vh></v>
<v t="agp.20060724215513"><vh>DocName</vh></v>
<v t="agp.20070206234855.1"><vh>StartDoc</vh></v>
<v t="agp.20070206234855.2"><vh>EndDoc</vh></v>
</v>
</v>
<v t="ekr.20060513122450.259"><vh>WriterClass</vh>
<v t="ekr.20060513122450.260"><vh>__init__</vh></v>
<v t="agp.20060724215520"><vh>PushDoc</vh></v>
<v t="agp.20060724221801"><vh>PopDoc</vh></v>
<v t="agp.20060724215513.1"><vh>WriteDoc</vh></v>
<v t="agp.20060730234939"><vh>WriteMenu</vh></v>
<v t="ekr.20060513122450.261"><vh>OnWriteStart</vh></v>
<v t="ekr.20060513122450.262"><vh>OnWriteEnd</vh></v>
<v t="agp.20060726210108"><vh>CreateBaseDoc</vh></v>
</v>
<v t="ekr.20060513122450.263"><vh>BreakFinderClass</vh>
<v t="ekr.20060513122450.264"><vh>__init__</vh></v>
<v t="ekr.20060513122450.265"><vh>OnFindStart</vh></v>
<v t="ekr.20060513122450.267"><vh>BreakDec</vh></v>
<v t="ekr.20060513122450.268"><vh>BreakDef</vh></v>
<v t="ekr.20060513122450.269"><vh>BreakOPN</vh></v>
</v>
<v t="ekr.20060513122450.270"><vh>SeekErrorClass</vh>
<v t="ekr.20060513122450.271"><vh>__init__</vh></v>
<v t="ekr.20060513122450.272"><vh>OnStartSeek</vh></v>
<v t="ekr.20060513122450.273"><vh>SeekDec</vh></v>
<v t="ekr.20060513122450.274"><vh>SeekDef</vh></v>
</v>
<v t="ekr.20060513122450.275"><vh>LocatorClass</vh>
<v t="ekr.20060513122450.276"><vh>__init__</vh></v>
<v t="ekr.20060513122450.277"><vh>OnStartLocate</vh></v>
<v t="ekr.20060513122450.278"><vh>LocateDec</vh></v>
<v t="agp.20060725012944"><vh>LocateDef</vh></v>
<v t="ekr.20060513122450.279"><vh>LocateDoc</vh></v>
</v>
<v t="agp.20070506104706.1"><vh>PyWrapperClass</vh>
<v t="agp.20070506104706.2"><vh>__init__</vh></v>
<v t="agp.20070506104706.7"><vh>OnWrapStart</vh></v>
<v t="agp.20070506104706.8"><vh>OnWrapEnd</vh></v>
<v t="agp.20070506114337.1"><vh>OnFunc</vh></v>
</v>
</v>
</v>
</v>
</v>
</v>
<v t="ekr.20060703162826"><vh>Dialogs</vh>
<v t="ekr.20060703162506"><vh>@thin keybindings.py</vh></v>
</v>
<v t="ekr.20041030092101"><vh>Dyna plugins by e</vh>
<v t="ekr.20060110125615"><vh>@url http://rclick.netfirms.com/dyna_menu.py.html  (dyna plugin)</vh></v>
</v>
<v t="ekr.20040722141148"><vh>Example code</vh>
<v t="edream.110203113231.916"><vh>@thin __overrideClasses.py</vh></v>
<v t="edream.110203113231.919"><vh>@thin override_commands.py</vh></v>
<v t="edream.110203113231.921"><vh>@thin redefine_put.py</vh></v>
<v t="ekr.20060621123339"><vh>@thin print_cp.py</vh></v>
</v>
<v t="ekr.20040722134535"><vh>Experimental/unfinished/abandoned</vh>
<v t="ekr.20040918165427.4"><vh>Autocompletion dictionary files</vh></v>
<v t="edream.110203113231.233"><vh>wxPython plugin (pre-alpha quality)</vh>
<v t="ekr.20060629124102"><vh>To do</vh>
<v t="edream.111303184347"><vh>(delete_range) doesn't work</vh>
<v t="edream.111303103141.3"><vh>delete_range</vh></v>
</v>
<v t="edream.111303100039"><vh>Gui-dependent commands (to do)</vh>
<v t="edream.111303100039.1"><vh>Edit Menu...</vh>
<v t="edream.111303101257"><vh>abortEditLabelCommand</vh></v>
<v t="edream.111303101257.1"><vh>endEditLabelCommand</vh></v>
<v t="edream.111303100039.6"><vh>insertHeadlineTime</vh></v>
</v>
<v t="edream.111303100039.7"><vh>Window Menu</vh>
<v t="edream.111303100039.8"><vh>cascade</vh></v>
<v t="edream.111303100039.9"><vh>equalSizedPanes</vh></v>
<v t="edream.111303100039.10"><vh>hideLogWindow</vh></v>
<v t="edream.111303100039.11"><vh>minimizeAll</vh></v>
<v t="edream.111303101709"><vh>toggleActivePane</vh></v>
<v t="edream.111303100039.12"><vh>toggleSplitDirection</vh></v>
</v>
<v t="edream.111703103908"><vh>Help Menu...</vh>
<v t="edream.111703103908.2"><vh>leoHelp</vh>
<v t="edream.111703103908.3"><vh>showProgressBar</vh>
<v t="edream.111703103908.4"><vh>&lt;&lt; create the scale widget &gt;&gt;</vh></v>
</v>
</v>
</v>
</v>
<v t="edream.111303205442"><vh>(colorizing) (demo only)</vh>
<v t="edream.111303204025"><vh>Indices (wxLeoBody)</vh>
<v t="edream.111303204025.1"><vh>adjustIndex</vh></v>
<v t="edream.111303204025.2"><vh>compareIndices</vh></v>
<v t="edream.111303204025.3"><vh>convertRowColumnToIndex</vh></v>
<v t="edream.111303204025.4"><vh>convertIndexToRowColumn</vh></v>
<v t="edream.111303204025.5"><vh>getImageIndex</vh></v>
<v t="edream.111403080609"><vh>maxWxIndex (internal use)</vh></v>
</v>
<v t="edream.111303204517"><vh>Color tags (hacks for styles)</vh>
<v t="edream.111403082513"><vh>tkColorToWxColor (internal use)</vh></v>
<v t="edream.111303205611"><vh>tag_add</vh></v>
<v t="edream.111303205611.1"><vh>tag_bind</vh></v>
<v t="edream.111303205611.2"><vh>tag_configure (hack for wxStyles)</vh></v>
<v t="edream.111303205611.3"><vh>tag_delete</vh></v>
<v t="edream.111303205611.4"><vh>tag_remove</vh></v>
</v>
</v>
</v>
<v t="edream.110203113231.302"><vh>@thin __wx_gui.py</vh></v>
</v>
</v>
<v t="EKR.20040517075715"><vh>External editors &amp; Open With</vh>
<v t="EKR.20040517075715.1"><vh>@thin mod_tempfname.py</vh></v>
<v t="EKR.20040517080049.4"><vh>@thin open_shell.py</vh></v>
<v t="EKR.20040517075715.4"><vh>@thin open_with.py</vh></v>
<v t="EKR.20040517075715.10"><vh>@thin vim.py</vh></v>
<v t="EKR.20040517075715.12"><vh>@thin xemacs.py</vh></v>
<v t="EKR.20040517075715.13"><vh>Word export</vh>
<v t="EKR.20040517075715.14"><vh>@thin word_export.py</vh></v>
<v t="EKR.20040517075715.20" tnodeList="EKR.20040517075715.20"><vh>@file-nosent word_export.ini</vh></v>
</v>
</v>
<v t="EKR.20040517080049"><vh>Files</vh>
<v t="EKR.20040517080049.1"><vh>@thin empty_leo_file.py</vh></v>
<v t="danr7.20060902215215.1"><vh>@thin leo_to_html.py</vh></v>
<v t="danr7.20060902083957"><vh>@thin leo_to_rtf.py</vh></v>
<v t="ekr.20040419105219"><vh>@thin lineNumbers.py</vh></v>
<v t="mork.20041018204908.1"><vh>@thin multifile.py</vh></v>
<v t="ekr.20040331151007"><vh>@thin niceNosent.py</vh></v>
</v>
<v t="ekr.20040722135402"><vh>Icon and status areas</vh>
<v t="ekr.20060328125925"><vh>@thin chapter_hoist.py</vh></v>
<v t="ekr.20040331072607"><vh>@thin hoist.py</vh></v>
<v t="edream.110203113231.758"><vh>@thin nav_buttons.py</vh></v>
<v t="pap.20051010170720"><vh>@thin newButtons.py</vh></v>
<v t="ekr.20040108062655"><vh>@thin nodenavigator.py</vh></v>
<v t="ekr.20040108095351"><vh>@thin rowcol.py</vh></v>
<v t="ekr.20040107092135.2"><vh>@thin searchbox.py</vh></v>
<v t="ekr.20060601151845"><vh>@thin shortcut_button.py</vh></v>
</v>
<v t="ekr.20050402080206"><vh>LeoN</vh>
<v t="ekr.20050402080206.1"><vh>Readme file.</vh></v>
<v t="ekr.20050402080206.2"><vh>Overview</vh>
<v t="ekr.20050402080206.3"><vh>&lt;&lt; Step four, Realtime interaction &gt;&gt;</vh>
<v t="ekr.20050402080206.4"><vh>Design notes</vh>
<v t="ekr.20050402080206.5"><vh>LeoN devellopment status III</vh></v>
<v t="ekr.20050402080206.6"><vh>LeoN devellopment status IV</vh></v>
</v>
<v t="ekr.20050402080206.7"><vh>Notes</vh></v>
</v>
</v>
<v t="ekr.20050402080206.8"><vh>@thin LeoN.py</vh></v>
</v>
<v t="EKR.20040517080555"><vh>Menus &amp; translations</vh>
<v t="ekr.20041019072632"><vh>Chinese:  Must use @file due to problems with cvs</vh>
<v t="ekr.20040828105233" tnodeList="ekr.20040828105233,ekr.20040828105233.1,ekr.20040828105233.2,ekr.20040828105233.3,ekr.20040828105233.4,ekr.20040828105233.5,ekr.20040828105233.6,ekr.20040828105233.7"><vh>@file chinese_menu.py</vh>
<v t="ekr.20040828105233.1"><vh>onMenu</vh>
<v t="ekr.20040828105233.2"><vh>file menu</vh></v>
<v t="ekr.20040828105233.3"><vh>edit menu</vh></v>
<v t="ekr.20040828105233.4"><vh>outline menu</vh></v>
<v t="ekr.20040828105233.5"><vh>plugins menu</vh></v>
<v t="ekr.20040828105233.6"><vh>window menu</vh></v>
<v t="ekr.20040828105233.7"><vh>help menu</vh></v>
</v>
</v>
</v>
<v t="EKR.20040517080202.3"><vh>@thin french_fm.py</vh></v>
<v t="EKR.20040517080555.36"><vh>@thin scripts_menu.py</vh></v>
<v t="ekr.20040828122150"><vh>@thin pie_menus.py</vh></v>
</v>
<v t="ekr.20060530091119"><vh>New colorizer</vh>
<v t="ekr.20060623075925.1"><vh>To do</vh></v>
<v t="ekr.20060530091119.2"><vh>@url http://www.jedit.org/42docs/users-guide/writing-modes-part.html</vh></v>
<v t="ekr.20060530091119.20"><vh>@thin __jEdit_colorizer__.py</vh></v>
</v>
<v t="edream.110203113231.872" a="E"><vh>Nodes...</vh>
<v t="edream.110203113231.873"><vh>@thin at_folder.py</vh></v>
<v t="ekr.20040915085351"><vh>@thin at_produce.py</vh></v>
<v t="ktenney.20041211072654.1"><vh>@thin at_view.py</vh></v>
<v t="mork.20041020082242.1"><vh>@thin base64Packager.py</vh></v>
<v t="ekr.20060807103814.1"><vh>@thin datenodes.py</vh></v>
<v t="mork.20041018091414.1"><vh>@thin fastGotoNode.py</vh></v>
<v t="ekr.20050301095332"><vh>@thin mod_labels.py</vh></v>
<v t="edream.110203113231.876" a="E"><vh>@thin read_nodes.py</vh></v>
<v t="ekr.20040910070811.1"><vh>@thin run_nodes.py</vh></v>
<v t="ekr.20060831165821"><vh>@thin slideshow.py</vh></v>
<v t="ekr.20040828103325"><vh>@thin startfile.py</vh></v>
<v t="ekr.20050329082101"><vh>AutoTrees</vh>
<v t="ekr.20050329082101.1"><vh>AutoTrees plugin</vh>
<v t="ekr.20050329082101.2"><vh>Introduction</vh></v>
<v t="ekr.20050329082101.3"><vh>Why use this?</vh></v>
<v t="ekr.20050329082101.4"><vh>Details</vh></v>
<v t="ekr.20050329082101.5"><vh>How do I create my own handlers?</vh></v>
</v>
<v t="ekr.20050329082101.6" annotate="7d71002e"><vh>Example handlers</vh>
<v t="ekr.20050329082101.7"><vh>Testing</vh>
<v t="ekr.20050329082101.8" annotate="7d71002e"><vh>@auto-test something</vh>
<v t="ekr.20050329082101.9"><vh>one</vh></v>
<v t="ekr.20050329082101.10"><vh>two</vh></v>
<v t="ekr.20050329082101.11"><vh>three</vh>
<v t="ekr.20050329082101.12"><vh>three-one</vh></v>
<v t="ekr.20050329082101.13"><vh>three-two</vh></v>
<v t="ekr.20050329082101.14"><vh>three-three</vh></v>
</v>
</v>
</v>
<v t="ekr.20050329082101.15"><vh>RSS</vh>
<v t="ekr.20050329082101.16"><vh>@auto-rss http://news.bbc.co.uk/rss/newsonline_uk_edition/world/rss091.xml</vh>
<v t="ekr.20050329092553"><vh>Hundreds die in Indonesia quake</vh></v>
<v t="ekr.20050329092553.1"><vh>Ousted Kyrgyz president defiant</vh></v>
<v t="ekr.20050329092553.2"><vh>Hair 'good source of stem cells'</vh></v>
<v t="ekr.20050329092553.3"><vh>Ashdown sacks top Bosnian Croat</vh></v>
<v t="ekr.20050329092553.4"><vh>Splits paralyse Iraqi parliament</vh></v>
<v t="ekr.20050329092553.5"><vh>Mongolians protest for new poll</vh></v>
<v t="ekr.20050329092553.6"><vh>Libya's Bulgarian medics appeal</vh></v>
<v t="ekr.20050329092553.7"><vh>Schiavo rivals 'agree to autopsy'</vh></v>
<v t="ekr.20050329092553.8"><vh>Would-be sex tourist, 87, jailed</vh></v>
<v t="ekr.20050329092553.9"><vh>Golf: Funk claims Players title</vh></v>
<v t="ekr.20050329092553.10"><vh>Cricket: Series win for Aussies</vh></v>
<v t="ekr.20050329092553.11"><vh>Angola says virus 'under control'</vh></v>
<v t="ekr.20050329092553.12"><vh>Mugabe criticises MDC 'traitors'</vh></v>
<v t="ekr.20050329092553.13"><vh>Ex-US diplomats round on Bolton</vh></v>
<v t="ekr.20050329092553.14"><vh>Brazil quits loan accord with IMF</vh></v>
<v t="ekr.20050329092553.15"><vh>Japanese economy hit by weak data</vh></v>
<v t="ekr.20050329092553.16"><vh>Donors pledge $40m for KR trials</vh></v>
<v t="ekr.20050329092553.17"><vh>Three Romanians missing in Iraq</vh></v>
<v t="ekr.20050329092553.18"><vh>Wolfowitz 'to meet EU officials'</vh></v>
<v t="ekr.20050329092553.19"><vh>Knesset rejects Gaza referendum</vh></v>
<v t="ekr.20050329092553.20"><vh>Militants to attend PLO meeting</vh></v>
<v t="ekr.20050329092553.21"><vh>South Asia cancels tsunami alerts</vh></v>
<v t="ekr.20050329092553.22"><vh>Devastation as Afghan dam bursts</vh></v>
<v t="ekr.20050329092553.23"><vh>Kyrgyzstan's friendly revolution</vh></v>
</v>
<v t="ekr.20050329082101.40" annotate="7d71002e"><vh>@auto-rss http://slashdot.org/index.rss</vh>
<v t="ekr.20050329092553.24"><vh>Followup on MS and Brazil in NY Times</vh></v>
<v t="ekr.20050329092553.25"><vh>A9.com with Syndicated Search</vh></v>
<v t="ekr.20050329092553.26"><vh>What's Next At Apple</vh></v>
<v t="ekr.20050329092553.27"><vh>Berkeley Grads' Identity Data Stolen</vh></v>
<v t="ekr.20050329092553.28"><vh>South Korean Gov't. Advocates Linux</vh></v>
<v t="ekr.20050329092553.29"><vh>MS, EU Agree on Name for Windows Sans Media Player</vh></v>
<v t="ekr.20050329092553.30"><vh>Blackbox (Finally) Updated</vh></v>
<v t="ekr.20050329092553.31"><vh>Your Face On the Big Screen</vh></v>
<v t="ekr.20050329092553.32"><vh>Ars Technica Builds Make Magazine's Steadicam</vh></v>
<v t="ekr.20050329092553.33"><vh>New Photovoltaics Made with Titanium Foil</vh></v>
</v>
<v t="ekr.20050329082101.51"><vh>@auto-rss http://www.python.org/channews.rdf</vh>
<v t="ekr.20050329082101.52"><vh>Python 2.4.1 (release candidate 1)</vh></v>
<v t="ekr.20050329082101.53"><vh>Greg Stein, of Google and Apache Software Foundation, to deliver keynote at PyCon</vh></v>
<v t="ekr.20050329082101.54"><vh>New RSS feed for python-dev summaries</vh></v>
<v t="ekr.20050329082101.55"><vh>Guido van Rossum speaking in Palo Alto</vh></v>
<v t="ekr.20050329082101.56"><vh>Python 2.3.5 (final)</vh></v>
<v t="ekr.20050329082101.57"><vh>Security advisory for SimpleXMLRPCServer.py.</vh></v>
<v t="ekr.20050329082101.58"><vh>Deadline for OSCON proposals</vh></v>
<v t="ekr.20050329082101.59"><vh>PyCon abstracts now available</vh></v>
<v t="ekr.20050329082101.60"><vh>PyCon preliminary schedule now available</vh></v>
<v t="ekr.20050329082101.61"><vh>PSF has awarded three grants</vh></v>
<v t="ekr.20050329082101.62"><vh>Python for Nokia Series 60 now available</vh></v>
<v t="ekr.20050329082101.63"><vh>Python 2.4 (final)</vh></v>
<v t="ekr.20050329082101.64"><vh>PyZine issue 7</vh></v>
<v t="ekr.20050329082101.65"><vh>PyCon 2005 Call for Proposals</vh></v>
<v t="ekr.20050329082101.66"><vh>Cameron Laird receives the Frank Willison Award</vh></v>
</v>
</v>
<v t="ekr.20050329082101.67"><vh>Remote</vh>
<v t="ekr.20050329082101.68"><vh>@auto-remote http://www.bbc.co.uk/news.html</vh></v>
</v>
<v t="ekr.20050329082101.69"><vh>Documentation</vh>
<v t="ekr.20050329082101.70"><vh>@auto-doc docutils.core</vh>
<v t="ekr.20050329082101.71"><vh>Component</vh>
<v t="ekr.20050329082101.72"><vh>component_type</vh></v>
<v t="ekr.20050329082101.73"><vh>default_transforms</vh></v>
<v t="ekr.20050329082101.74"><vh>supports</vh></v>
</v>
<v t="ekr.20050329082101.75"><vh>ConfigParser</vh>
<v t="ekr.20050329082101.76"><vh>OPTCRE</vh></v>
<v t="ekr.20050329082101.77"><vh>SECTCRE</vh></v>
<v t="ekr.20050329082101.78"><vh>add_section</vh></v>
<v t="ekr.20050329082101.79"><vh>standard_config_files</vh></v>
<v t="ekr.20050329082101.80"><vh>validation</vh></v>
</v>
<v t="ekr.20050329082101.81"><vh>OptionParser</vh>
<v t="ekr.20050329082101.82"><vh>default_error_encoding_error_handler</vh></v>
<v t="ekr.20050329082101.83"><vh>relative_path_settings</vh></v>
<v t="ekr.20050329082101.84"><vh>settings_defaults</vh></v>
<v t="ekr.20050329082101.85"><vh>settings_spec</vh></v>
<v t="ekr.20050329082101.86"><vh>standard_option_list</vh></v>
<v t="ekr.20050329082101.87"><vh>threshold_choices</vh></v>
<v t="ekr.20050329082101.88"><vh>thresholds</vh></v>
<v t="ekr.20050329082101.89"><vh>version_template</vh></v>
</v>
<v t="ekr.20050329082101.90"><vh>Publisher</vh></v>
<v t="ekr.20050329082101.91"><vh>default_description</vh></v>
<v t="ekr.20050329082101.92"><vh>default_usage</vh></v>
<v t="ekr.20050329082101.93"><vh>frontend</vh></v>
<v t="ekr.20050329082101.94"><vh>io</vh></v>
<v t="ekr.20050329082101.95"><vh>parsers</vh></v>
<v t="ekr.20050329082101.96"><vh>publish_cmdline</vh></v>
<v t="ekr.20050329082101.97"><vh>publish_file</vh></v>
<v t="ekr.20050329082101.98"><vh>publish_string</vh></v>
<v t="ekr.20050329082101.99"><vh>readers</vh></v>
<v t="ekr.20050329082101.100"><vh>sys</vh></v>
<v t="ekr.20050329082101.101"><vh>writers</vh></v>
</v>
</v>
<v t="ekr.20050329082101.102"><vh>News Reader</vh>
<v t="ekr.20050329082101.103"><vh>@auto-news news-server.houston.rr.com/comp.lang.python</vh>
<v t="ekr.20050329082101.104"><vh>@auto-newsitem 356970 - Easy way to check modules for python version compatibility?</vh></v>
<v t="ekr.20050329082101.105"><vh>@auto-newsitem 356972 - Q: Module Shared Data</vh></v>
<v t="ekr.20050329082101.106"><vh>@auto-newsitem 356978 - Re: __contains__ inconsistencies between Python 2.2 and 2.3</vh></v>
<v t="ekr.20050329082101.107"><vh>@auto-newsitem 356979 - Re: [Numeric] column vector faster than row vector in mat multiply?</vh></v>
<v t="ekr.20050329082101.108"><vh>@auto-newsitem 356986 - Python 2.4 removes None data type?</vh></v>
<v t="ekr.20050329082101.109"><vh>@auto-newsitem 356987 - Re: Integer From A Float List?!?</vh></v>
<v t="ekr.20050329082101.110"><vh>@auto-newsitem 356988 - Suspicious header</vh></v>
<v t="ekr.20050329082101.111"><vh>@auto-newsitem 356991 - Re: Suspicious header</vh></v>
<v t="ekr.20050329082101.112"><vh>@auto-newsitem 356992 - survey</vh></v>
<v t="ekr.20050329082101.113"><vh>@auto-newsitem 356993 - Re: Python 2.4 removes None data type?</vh></v>
</v>
</v>
</v>
<v t="ekr.20050329082101.114"><vh>AutoTrees Code</vh>
<v t="ekr.20050329082101.115"><vh>@thin autotrees.py</vh></v>
<v t="ekr.20050329082101.145"><vh>@thin trees\pluginsManager.txt</vh></v>
<v t="ekr.20050329082101.146"><vh>Example tree handlers</vh>
<v t="ekr.20050329082101.147"><vh>@thin trees\test.py</vh></v>
<v t="ekr.20050329082101.150"><vh>@thin trees\rss.py</vh></v>
<v t="ekr.20050329082101.153"><vh>@thin trees\news.py</vh></v>
<v t="ekr.20050329082101.162"><vh>@thin trees\remote.py</vh></v>
<v t="ekr.20050329082101.165"><vh>@thin trees\doc.py</vh></v>
</v>
</v>
</v>
</v>
<v t="ekr.20041009112303"><vh>Plugins manager, updater &amp; menu</vh>
<v t="EKR.20040517080555.1"><vh> Plugins menu</vh>
<v t="EKR.20040517080555.2"><vh>@thin plugins_menu.py</vh></v>
<v t="EKR.20040517080555.25"><vh>@thin pluginsTest.py</vh></v>
<v t="EKR.20040517080555.32"><vh>Notes re plugins menu</vh>
<v t="EKR.20040517080555.33"><vh> Changes made by E.K.Ream</vh></v>
<v t="EKR.20040517080555.34"><vh> Design</vh></v>
<v t="EKR.20040517080555.35"><vh> Initial suggestion from Paul Paterson</vh></v>
</v>
</v>
<v t="pap.20041006184225"><vh>@thin plugin_manager.py</vh></v>
<v t="pap.20050605183206"><vh>@thin leoupdate.py</vh></v>
</v>
<v t="ekr.20041001210557"><vh>Scripting</vh>
<v t="ekr.20060328125248"><vh>@thin mod_scripting.py</vh></v>
</v>
<v t="ekr.20050111122605"><vh>Servers</vh>
<v t="EKR.20040517080250.1"><vh>@thin mod_http.py</vh></v>
</v>
<v t="ekr.20060715100156"><vh>Shadow files plugin</vh>
<v t="ekr.20060715100156.1"><vh>test zone</vh>
<v t="ekr.20060715100156.2"><vh>@@button Do @test</vh>
<v t="ekr.20060715100156.3"><vh>test propagate_changes_from_lines_without_sentinels_to_lines_with_sentinels</vh>
<v t="ekr.20060715100156.4"><vh>@test basic replacement test</vh>
<v t="ekr.20060715100156.5"><vh>before with sentinels</vh></v>
<v t="ekr.20060715100156.6"><vh>after with sentinels</vh></v>
<v t="ekr.20060715100156.7"><vh>changed without sentinels</vh></v>
</v>
</v>
</v>
</v>
<v t="ekr.20060816094306"><vh>Note: @button shadow is in leoPy.leo</vh></v>
<v t="ekr.20060715100156.8"><vh>@thin mod_shadow_core.py</vh></v>
<v t="ekr.20060715100156.52"><vh>@thin mod_shadow.py</vh></v>
</v>
<v t="ekr.20050306081349"><vh>Text formatting</vh>
<v t="mork.20041010095009"><vh>@thin xsltWithNodes.py</vh></v>
<v t="ekr.20040331071919"><vh>Leo to AsciiDoc</vh>
<v t="ekr.20050128070307"><vh>@url http://www.marshallresearch.com/michael-dawson/os/leo.html</vh></v>
<v t="ekr.20040331071919.38"><vh>Leo 2 AsciiDoc Users Guide</vh>
<v t="ekr.20040331071919.2"><vh>About this document</vh>
<v t="ekr.20040331071919.3"><vh>License</vh>
<v t="ekr.20040331071919.4"><vh>License document</vh></v>
</v>
</v>
<v t="ekr.20040331071919.39"><vh>Installation</vh></v>
<v t="ekr.20040331071919.40"><vh>Operation</vh>
<v t="ekr.20040331071919.41"><vh>Directives</vh>
<v t="ekr.20040331071919.42"><vh>Configuration</vh></v>
</v>
<v t="ekr.20040331071919.43"><vh>Markup</vh>
<v t="ekr.20040331071919.44"><vh>Standard AsciiDoc Markup</vh>
<v t="ekr.20040331071919.45"><vh>Headings</vh></v>
<v t="ekr.20040331071919.46"><vh>Lists</vh></v>
<v t="ekr.20040331071919.47"><vh>URLs</vh></v>
</v>
</v>
</v>
</v>
<v t="ekr.20040331071919.1"><vh>Leo 2 AsciiDoc Developers Guide</vh>
<v t="ekr.20040331071919.2"><vh>About this document</vh>
<v t="ekr.20040331071919.3"><vh>License</vh>
<v t="ekr.20040331071919.4"><vh>License document</vh></v>
</v>
</v>
<v t="ekr.20040331071919.5"><vh>Version, Requirements</vh></v>
<v t="ekr.20040331071919.6"><vh>The General Approach</vh>
<v t="ekr.20040331071919.7"><vh>Markup Added</vh></v>
</v>
<v t="ekr.20040331071919.8"><vh>&lt;&lt; root of mod_leo2ascd.py &gt;&gt;</vh>
<v t="ekr.20040331071919.9"><vh>&lt;&lt; Key Functions &gt;&gt;</vh></v>
<v t="ekr.20040331071919.10"><vh>&lt;&lt; Declarations and Utilities &gt;&gt;</vh>
<v t="ekr.20040331071919.11"><vh>&lt;&lt; The Code -- Declarations and Utilities &gt;&gt;</vh></v>
</v>
<v t="ekr.20040331071919.12"><vh>&lt;&lt; Write the outline tree as AsciiDoc file &gt;&gt;</vh>
<v t="ekr.20040331071919.13"><vh>&lt;&lt; Write a node &gt;&gt;</vh></v>
</v>
</v>
<v t="ekr.20040331071919.14"><vh>Other programs</vh></v>
<v t="ekr.20040331071919.15"><vh>&lt;&lt;Appendix: AsciiDoc &gt;&gt;</vh>
<v t="ekr.20040331071919.16"><vh>&lt;&lt; Configuration file &gt;&gt;</vh></v>
<v t="ekr.20040331071919.17"><vh>&lt;&lt; Patches &gt;&gt;</vh></v>
</v>
<v t="ekr.20040331071919.18"><vh>&lt;&lt;Appendix: DocBook&gt;&gt;</vh>
<v t="ekr.20040331071919.19"><vh>&lt;&lt; Tool Chain &gt;&gt;</vh></v>
<v t="ekr.20040331071919.20"><vh>&lt;&lt; Make File &gt;&gt;</vh></v>
<v t="ekr.20040331071919.21"><vh>&lt;&lt; Style Sheets &gt;&gt;</vh>
<v t="ekr.20040331071919.22"><vh>&lt;&lt; General &gt;&gt;</vh></v>
<v t="ekr.20040331071919.23"><vh>&lt;&lt; Customize &gt;&gt;</vh></v>
<v t="ekr.20040331071919.24"><vh>&lt;&lt; HTML: One File &gt;&gt;</vh></v>
<v t="ekr.20040331071919.25"><vh>&lt;&lt; HTML: Individual Pages &gt;&gt;</vh></v>
<v t="ekr.20040331071919.26"><vh>&lt;&lt; HTML: base css style sheet &gt;&gt;</vh></v>
<v t="ekr.20040331071919.27"><vh>&lt;&lt; HTML: css style sheet &gt;&gt;</vh></v>
<v t="ekr.20040331071919.28"><vh>&lt;&lt; HTML: common &gt;&gt;</vh></v>
<v t="ekr.20040331071919.29"><vh>&lt;&lt; PDF &gt;&gt;</vh></v>
</v>
</v>
<v t="ekr.20040331071919.30"><vh>&lt;&lt;Appendix: XEmacs Text Editor&gt;&gt;</vh>
<v t="ekr.20040331071919.31"><vh>&lt;&lt; Open_With Plugin &gt;&gt;</vh></v>
<v t="ekr.20040331071919.32"><vh>&lt;&lt; Open_Tree Plugin &gt;&gt;</vh></v>
<v t="ekr.20040331071919.33"><vh>&lt;&lt; Filename modification &gt;&gt;</vh></v>
<v t="ekr.20040331071919.34"><vh>&lt;&lt; Kill Temporary Buffers &gt;&gt;</vh></v>
<v t="ekr.20040331071919.35"><vh>&lt;&lt; MMM-mode &gt;&gt;</vh></v>
<v t="ekr.20040331071919.36"><vh>&lt;&lt; Insert indexterm &gt;&gt;</vh></v>
<v t="ekr.20040331071919.37"><vh>&lt;&lt; Indent Leo comments &gt;&gt;</vh></v>
</v>
</v>
</v>
<v t="ekr.20050817132814"><vh>rst3</vh>
<v t="ekr.20050817120850.1" tnodeList="ekr.20050817120850.1,ekr.20050817122915,ekr.20050822123348,ekr.20050817124859,ekr.20050817165745,ekr.20050822172321,ekr.20050817124859.1,ekr.20050817165745.1,ekr.20050818033610,ekr.20050818095347,ekr.20050819055746.1,ekr.20050820112549,ekr.20050822065754,ekr.20050822125824,ekr.20050822172321.1,ekr.20050825101903,ekr.20050818103031,ekr.20050817115636.2,ekr.20050825101321,ekr.20050818103441,ekr.20050817115636.4,ekr.20050817115636.5,ekr.20050817115636.6,ekr.20050820092312,ekr.20050817115636.8,ekr.20050817115636.9,ekr.20050817115636.7,ekr.20050820100547,ekr.20050820101355,ekr.20050820103029,ekr.20050820101522,ekr.20050820101355.1,ekr.20050820094818,ekr.20050820092312.1,ekr.20050817120850.10,ekr.20050817120850.11,ekr.20050818094118.2,ekr.20050818090152,ekr.20050818090152.1,ekr.20050817120850.98,ekr.20050817120850.99,ekr.20050817120850.94,ekr.20050817120850.95,ekr.20050817120850.96,ekr.20050817120850.108,ekr.20050817142135.1,ekr.20050817120850.143,ekr.20050817120850.144,ekr.20050817120850.141,ekr.20050817135706.1,ekr.20050817120850.157,ekr.20050817120850.158,ekr.20050818105023,ekr.20050817120850.15,ekr.20050817120850.12,ekr.20050817120850.14,ekr.20050818081715,ekr.20050819072001,ekr.20050819072001.1,ekr.20050817120850.13,ekr.20050818083045,ekr.20050821153838,ekr.20050818022030,ekr.20050818084920,ekr.20050818130249,ekr.20050818090907,ekr.20050817120850.32,ekr.20050817120850.34,ekr.20050817120850.39,ekr.20050817120850.42,ekr.20050817120850.44,ekr.20050817120850.46,ekr.20050817120850.48,ekr.20050817120850.62,ekr.20050817120850.64,ekr.20050817120850.74,ekr.20050817120850.78,ekr.20050817120850.86,ekr.20050817120850.92,ekr.20050817120850.162,ekr.20050817120850.102,ekr.20050817120850.106,ekr.20050817120850.110,ekr.20050817120850.122,ekr.20050817120850.124,ekr.20050817120850.126,ekr.20050817120850.130,ekr.20050817120850.132,ekr.20050817120850.138,ekr.20050817120850.28,ekr.20050817120850.147,ekr.20050817120850.18,ekr.20050817120850.20,ekr.20050817120850.40,ekr.20050817120850.54,ekr.20050817120850.82,ekr.20050817120850.100,ekr.20050817120850.105,ekr.20050817120850.120,ekr.20050817120850.36,ekr.20050817120850.58,ekr.20050817120850.60,ekr.20050817120850.66,ekr.20050817120850.24,ekr.20050817120850.22,ekr.20050817120850.50,ekr.20050817120850.52,ekr.20050817120850.56,ekr.20050818094118.1,ekr.20050817120850.68,ekr.20050817120850.134,ekr.20050817120850.145,ekr.20050817120850.151,ekr.20050817120850.26,ekr.20050817120850.76,ekr.20050817120850.80,ekr.20050817120850.88,ekr.20050817120850.112,ekr.20050817120850.128,ekr.20050817142135,ekr.20050817120850.153,ekr.20050817120850.155,ekr.20050817120850.30,ekr.20050817135706,ekr.20050817120850.160,ekr.20050818094954,ekr.20050818105023.1,ekr.20050817120850.84,ekr.20050817120850.90,ekr.20050818094954.1,ekr.20050817120850.165,ekr.20050817120850.116,ekr.20050817120850.70,ekr.20050817120850.72,ekr.20050817120850.164,ekr.20050817120850.114,ekr.20050817120850.118,ekr.20050817120850.149,ekr.20050817120850.159,ekr.20050817120850.140"><vh>@file leo_pdf.py</vh>
<v t="ekr.20050817122915"><vh>&lt;&lt; docstring &gt;&gt;</vh></v>
<v t="ekr.20050817115636.2"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="ekr.20050822123348"><vh>&lt;&lt; about this code &gt;&gt;</vh></v>
<v t="ekr.20050817124859"><vh>&lt;&lt; copyright &gt;&gt;</vh></v>
<v t="ekr.20050817165745"><vh>&lt;&lt; version history &gt;&gt;</vh>
<v t="ekr.20050822172321"><vh>Early versions</vh>
<v t="ekr.20050817124859.1"><vh>Initial conversion</vh></v>
<v t="ekr.20050817165745.1"><vh>0.0.1</vh></v>
<v t="ekr.20050818033610"><vh>0.0.2</vh></v>
<v t="ekr.20050818095347"><vh>0.0.3</vh></v>
<v t="ekr.20050819055746.1"><vh>0.0.4</vh></v>
<v t="ekr.20050820112549"><vh>0.0.5</vh></v>
</v>
<v t="ekr.20050822065754"><vh>0.1</vh></v>
<v t="ekr.20050822125824"><vh>0.2</vh></v>
<v t="ekr.20050822172321.1"><vh>0.3</vh></v>
<v t="ekr.20050825101903"><vh>0.4</vh></v>
</v>
<v t="ekr.20050818103031"><vh>&lt;&lt; to do &gt;&gt;</vh></v>
<v t="ekr.20050825101321"><vh>init</vh></v>
<v t="ekr.20050818103441"><vh>class Bunch (object)</vh></v>
<v t="ekr.20050817115636.4"><vh>class Writer (docutils.writers.Writer)</vh>
<v t="ekr.20050817115636.5"><vh>&lt;&lt; class Writer declarations &gt;&gt;</vh></v>
<v t="ekr.20050817115636.6"><vh>__init__ (Writer)</vh></v>
<v t="ekr.20050820092312"><vh>createParagraphsFromIntermediateFile</vh></v>
<v t="ekr.20050817115636.8"><vh>createPDF_usingPlatypus</vh></v>
<v t="ekr.20050817115636.9"><vh>lower</vh></v>
<v t="ekr.20050817115636.7"><vh>translate</vh></v>
</v>
<v t="ekr.20050820100547"><vh>class dummyPDFTranslator (docutils.nodes.NodeVisitor)</vh>
<v t="ekr.20050820101355"><vh>   __init__ (dummyPDFTranslator)</vh></v>
<v t="ekr.20050820103029"><vh>as_what</vh></v>
<v t="ekr.20050820101522"><vh>encode</vh></v>
<v t="ekr.20050820101355.1"><vh>visit/depart_document</vh></v>
<v t="ekr.20050820094818"><vh>buildFromIntermediateFile</vh></v>
<v t="ekr.20050820092312.1"><vh>putParaFromIntermediateFile</vh></v>
</v>
<v t="ekr.20050817120850.10"><vh>class PDFTranslator (docutils.nodes.NodeVisitor)</vh>
<v t="ekr.20050817120850.11"><vh>   __init__ (PDFTranslator)</vh></v>
<v t="ekr.20050818094118.2"><vh>Complex</vh>
<v t="ekr.20050818090152"><vh>footnotes</vh>
<v t="ekr.20050818090152.1"><vh>footnote_reference</vh>
<v t="ekr.20050817120850.98"><vh>visit_footnote_reference</vh></v>
<v t="ekr.20050817120850.99"><vh>depart_footnote_reference</vh></v>
</v>
<v t="ekr.20050817120850.94"><vh>footnote &amp; helpers</vh>
<v t="ekr.20050817120850.95"><vh>footnote_backrefs</vh></v>
<v t="ekr.20050817120850.96"><vh>footnote_backrefs_depart</vh></v>
</v>
<v t="ekr.20050817120850.108"><vh>label</vh></v>
</v>
<v t="ekr.20050817142135.1"><vh>reference...</vh>
<v t="ekr.20050817120850.143"><vh>visit_reference</vh></v>
<v t="ekr.20050817120850.144"><vh>depart_reference</vh></v>
</v>
<v t="ekr.20050817120850.141"><vh>target</vh></v>
<v t="ekr.20050817135706.1"><vh>title</vh>
<v t="ekr.20050817120850.157"><vh>visit_title</vh></v>
<v t="ekr.20050817120850.158"><vh>depart_title</vh></v>
</v>
</v>
<v t="ekr.20050818105023"><vh>Helpers</vh>
<v t="ekr.20050817120850.15"><vh> starttag</vh></v>
<v t="ekr.20050817120850.12"><vh>as_what</vh></v>
<v t="ekr.20050817120850.14"><vh>createParagraph</vh></v>
<v t="ekr.20050818081715"><vh>dumpContext</vh></v>
<v t="ekr.20050819072001"><vh>dumpNode</vh>
<v t="ekr.20050819072001.1"><vh>&lt;&lt; define keys to be printed &gt;&gt;</vh></v>
</v>
<v t="ekr.20050817120850.13"><vh>encode</vh></v>
<v t="ekr.20050818083045"><vh>inContext</vh></v>
<v t="ekr.20050821153838"><vh>pdfMunge</vh></v>
<v t="ekr.20050818022030"><vh>push, pop, peek</vh></v>
<v t="ekr.20050818084920"><vh>putHead &amp; putTail</vh></v>
</v>
<v t="ekr.20050818130249"><vh>Simple...</vh>
<v t="ekr.20050818090907"><vh> do nothings...</vh>
<v t="ekr.20050817120850.32"><vh>authors</vh></v>
<v t="ekr.20050817120850.34"><vh>block_quote</vh></v>
<v t="ekr.20050817120850.39"><vh>caption</vh></v>
<v t="ekr.20050817120850.42"><vh>citation</vh></v>
<v t="ekr.20050817120850.44"><vh>citation_reference</vh></v>
<v t="ekr.20050817120850.46"><vh>classifier</vh></v>
<v t="ekr.20050817120850.48"><vh>colspec</vh></v>
<v t="ekr.20050817120850.62"><vh>definition_list_item</vh></v>
<v t="ekr.20050817120850.64"><vh>description</vh></v>
<v t="ekr.20050817120850.74"><vh>document</vh></v>
<v t="ekr.20050817120850.78"><vh>entry</vh></v>
<v t="ekr.20050817120850.86"><vh>field_argument</vh></v>
<v t="ekr.20050817120850.92"><vh>field_body</vh></v>
<v t="ekr.20050817120850.162"><vh>generated</vh></v>
<v t="ekr.20050817120850.102"><vh>image</vh></v>
<v t="ekr.20050817120850.106"><vh>interpreted</vh></v>
<v t="ekr.20050817120850.110"><vh>legend</vh></v>
<v t="ekr.20050817120850.122"><vh>option</vh></v>
<v t="ekr.20050817120850.124"><vh>option_argument</vh></v>
<v t="ekr.20050817120850.126"><vh>option_group</vh></v>
<v t="ekr.20050817120850.130"><vh>option_list_item</vh></v>
<v t="ekr.20050817120850.132"><vh>option_string</vh></v>
<v t="ekr.20050817120850.138"><vh>problematic</vh></v>
<v t="ekr.20050817120850.28"><vh>system_message</vh></v>
<v t="ekr.20050817120850.147"><vh>visit_row</vh></v>
</v>
<v t="ekr.20050817120850.18"><vh>admonitions...</vh>
<v t="ekr.20050817120850.20"><vh>attention</vh></v>
<v t="ekr.20050817120850.40"><vh>caution</vh></v>
<v t="ekr.20050817120850.54"><vh>danger</vh></v>
<v t="ekr.20050817120850.82"><vh>error</vh></v>
<v t="ekr.20050817120850.100"><vh>hint</vh></v>
<v t="ekr.20050817120850.105"><vh>important</vh></v>
<v t="ekr.20050817120850.120"><vh>note</vh></v>
</v>
<v t="ekr.20050817120850.36"><vh>bullet_list</vh></v>
<v t="ekr.20050817120850.58"><vh>definition</vh></v>
<v t="ekr.20050817120850.60"><vh>definition_list</vh></v>
<v t="ekr.20050817120850.66"><vh>docinfos...</vh>
<v t="ekr.20050817120850.24"><vh>address</vh></v>
<v t="ekr.20050817120850.22"><vh>author</vh></v>
<v t="ekr.20050817120850.50"><vh>contact</vh></v>
<v t="ekr.20050817120850.52"><vh>copyright</vh></v>
<v t="ekr.20050817120850.56"><vh>date</vh></v>
<v t="ekr.20050818094118.1"><vh>docinfo</vh></v>
<v t="ekr.20050817120850.68"><vh>docinfo_item</vh></v>
<v t="ekr.20050817120850.134"><vh>organization</vh></v>
<v t="ekr.20050817120850.145"><vh>revision</vh></v>
<v t="ekr.20050817120850.151"><vh>status</vh></v>
<v t="ekr.20050817120850.26"><vh>version</vh></v>
</v>
<v t="ekr.20050817120850.76"><vh>emphasis</vh></v>
<v t="ekr.20050817120850.80"><vh>enumerated_list</vh></v>
<v t="ekr.20050817120850.88"><vh>field_list</vh></v>
<v t="ekr.20050817120850.112"><vh>list_item</vh></v>
<v t="ekr.20050817120850.128"><vh>option_list</vh></v>
<v t="ekr.20050817142135"><vh>paragraph...</vh></v>
<v t="ekr.20050817120850.153"><vh>strong</vh></v>
<v t="ekr.20050817120850.155"><vh>subtitle</vh></v>
<v t="ekr.20050817120850.30"><vh>term</vh></v>
<v t="ekr.20050817135706"><vh>Text...</vh></v>
<v t="ekr.20050817120850.160"><vh>topic</vh></v>
</v>
<v t="ekr.20050818094954"><vh>Unusual...</vh>
<v t="ekr.20050818105023.1"><vh> Does not set context</vh>
<v t="ekr.20050817120850.84"><vh>field</vh></v>
<v t="ekr.20050817120850.90"><vh>field_name</vh></v>
</v>
<v t="ekr.20050818094954.1"><vh> Raises SkipNode</vh>
<v t="ekr.20050817120850.165"><vh>comment</vh></v>
<v t="ekr.20050817120850.116"><vh> literal_blocks...</vh>
<v t="ekr.20050817120850.70"><vh>doctest_block</vh></v>
<v t="ekr.20050817120850.72"><vh>line_block</vh></v>
</v>
</v>
<v t="ekr.20050817120850.164"><vh>invisible_visit</vh></v>
<v t="ekr.20050817120850.114"><vh>literal (only changes context)</vh></v>
<v t="ekr.20050817120850.118"><vh>meta (appends to self.head)</vh></v>
<v t="ekr.20050817120850.149"><vh>section</vh></v>
<v t="ekr.20050817120850.159"><vh>unimplemented_visit</vh></v>
<v t="ekr.20050817120850.140"><vh>visit_raw</vh></v>
</v>
</v>
</v>
<v t="ekr.20050805162550"><vh>@thin rst3.py</vh></v>
</v>
</v>
<v t="ekr.20061023142737"><vh>UNL plugin</vh>
<v t="rogererens.20041014110709"><vh>To do</vh></v>
<v t="ekr.20061023142737.1"><vh>Tests</vh>
<v t="rogererens.20041130095659"><vh>@url 'file: ./../../plugins/leoPlugins.leo#Plugins--&gt;UNL plugin--&gt;To do'</vh></v>
<v t="ekr.20061023141638"><vh>@url 'file:./../doc/leoDocs.leo#Users Guide--&gt; Chapter 8: Customizing Leo'</vh></v>
<v t="ekr.20061023141459"><vh>@url 'Plugins--&gt;UNL plugin--&gt;@thin UNL.py'</vh></v>
</v>
<v t="rogererens.20041013082304"><vh>@thin UNL.py</vh></v>
</v>
<v t="ekr.20040915073259"><vh>Windows</vh>
<v t="ekr.20050227071948" annotate="5404010000376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333464306632373632353530343665366636343635373130353238363830323666373130363535303734363635363137343735373236353731303736323535303236323637373130383238363830323666373130393535303037313061363235353039363137323633363836353734373937303635373130623238363830323666373130633638306136323535303236363637373130643238363830323666373130653638306136323735326571002e"><vh> cleo</vh>
<v t="ekr.20050227072121"><vh>Notes</vh>
<v t="ekr.20050227071948.1" annotate="7d71002e"><vh>TODO</vh>
<v t="ekr.20050227071948.2" annotate="7d71002e"><vh>pixmap icons</vh></v>
<v t="ekr.20050227071948.3" annotate="7d71002e"><vh>colour selector</vh></v>
<v t="ekr.20050227071948.4" annotate="55f037643731303032383535303837303732363936663732363937343739373130313238363336313665366536663734363137343635306135343662353036393633366236633635353636313732306137313032366637313033346236343632353530343665366636343635373130353238363830323666373130363535303037313037363235353032363236373731303832383638303236663731303936383037363235353039363137323633363836353734373937303635373130613238363830323666373130623638303736323535303236363637373130633238363830323666373130643638303736323735326571002e"><vh>popup location</vh></v>
<v t="ekr.20050227071948.5" annotate="5592376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333462303136323535303936313732363336383635373437393730363537313035323836383032366637313036353530303731303736323735326571002e"><vh>EKR's intentions on @thin nodes</vh>
<v t="ekr.20050227071948.6" annotate="5592376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333462303136323535303936313732363336383635373437393730363537313035323836383032366637313036353530303731303736323735326571002e"><vh>No attributes for @thin nodes</vh></v>
</v>
<v t="ekr.20050227071948.7" annotate="7d71002e"><vh>group annotations</vh></v>
<v t="ekr.20050227071948.8" annotate="7d71002e"><vh>archetype based search,navigation</vh></v>
<v t="ekr.20050227071948.9" annotate="7d71002e"><vh>sort by type</vh></v>
<v t="ekr.20050227071948.10" annotate="7d71002e"><vh>fonts</vh></v>
<v t="ekr.20050227071948.11" annotate="55f037643731303032383535303837303732363936663732363937343739373130313238363336313665366536663734363137343635306135343662353036393633366236633635353636313732306137313032366637313033346230323632353530343665366636343635373130353238363830323666373130363535303037313037363235353032363236373731303832383638303236663731303936383037363235353039363137323633363836353734373937303635373130613238363830323666373130623638303736323535303236363637373130633238363830323666373130643638303736323735326571002e"><vh>question marks</vh></v>
</v>
<v t="ekr.20050227071948.12" annotate="54000100003764373130303238353530383730373236393666373236393734373937313031323836333631366536653666373436313734363530613534366235303639363336623663363535363631373230613731303236663731303334623634363235353034366536663634363537313035323836383032366637313036353530303731303736323535303236323637373130383238363830323666373130393535303635303735373237303663363537313061363235353039363137323633363836353734373937303635373130623238363830323666373130633638303736323535303236363637373130643238363830323666373130653638303736323735326571002e"><vh>Done</vh>
<v t="ekr.20050227071948.13" annotate="7d71005509617474656e74696f6e71014930300a732e"><vh>Clear All markings</vh></v>
<v t="ekr.20050227071948.15" annotate="5592376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333462363436323535303936313732363336383635373437393730363537313035323836383032366637313036353530303731303736323735326571002e"><vh>arbitary colouring</vh></v>
<v t="ekr.20050227071948.16" annotate="55f037643731303032383535303837303732363936663732363937343739373130313238363336313665366536663734363137343635306135343662353036393633366236633635353636313732306137313032366637313033346236343632353530343665366636343635373130353238363830323666373130363535303037313037363235353032363236373731303832383638303236663731303936383037363235353039363137323633363836353734373937303635373130613238363830323666373130623638303736323535303236363637373130633238363830323666373130643638303736323735326571002e"><vh>rename to cleo</vh></v>
<v t="ekr.20050227071948.17" annotate="7d71002e"><vh>headline colours</vh></v>
<v t="ekr.20050227071948.18" annotate="7d71005509617474656e74696f6e71014930300a732e"><vh>priority colouring</vh></v>
<v t="ekr.20050227071948.19" annotate="7d71005509617474656e74696f6e71014930300a732e"><vh>archtetype colouring</vh></v>
</v>
<v t="ekr.20050227071948.20" annotate="7d71002e"><vh>Problems</vh>
<v t="ekr.20050227071948.6" annotate="5592376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333462303136323535303936313732363336383635373437393730363537313035323836383032366637313036353530303731303736323735326571002e"><vh>No attributes for @thin nodes</vh></v>
<v t="ekr.20050227071948.21" annotate="5592376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333462303236323535303936313732363336383635373437393730363537313035323836383032366637313036353530303731303736323735326571002e"><vh>features are not orthogonal</vh></v>
<v t="ekr.20050227071948.22" annotate="7d71002e"><vh>Too many colours !!</vh></v>
</v>
<v t="ekr.20050227071948.23" annotate="5404010000376437313030323835353038373037323639366637323639373437393731303132383633363136653665366637343631373436353061353436623530363936333662366336353536363137323061373130323666373130333464306632373632353530343665366636343635373130353238363830323666373130363535303734363635363137343735373236353731303736323535303236323637373130383238363830323666373130393535303037313061363235353039363137323633363836353734373937303635373130623238363830323666373130633638306136323535303236363637373130643238363830323666373130653638306136323735326571002e"><vh>BUGS</vh>
<v t="ekr.20050227071948.24" annotate="55f037643731303032383535303837303732363936663732363937343739373130313238363336313665366536663734363137343635306135343662353036393633366236633635353636313732306137313032366637313033346236343632353530343665366636343635373130353238363830323666373130363535303037313037363235353032363236373731303832383638303236663731303936383037363235353039363137323633363836353734373937303635373130613238363830323666373130623638303736323535303236363637373130633238363830323666373130643638303736323735326571002e"><vh>popup location</vh></v>
</v>
<v t="ekr.20050227071948.27" annotate="7d71002e"><vh>colour table</vh></v>
<v t="ekr.20050227071948.28" annotate="54060100003764373130303238353530383730373236393666373236393734373937313031323836333631366536653666373436313734363530613534366235303639363336623663363535363631373230613731303236663731303334643066323736323535303436653666363436353731303532383638303236663731303635353038343336663664366436353665373437333731303736323535303236323637373130383238363830323666373130393535303037313061363235353039363137323633363836353734373937303635373130623238363830323666373130633638306136323535303236363637373130643238363830323666373130653638306136323735326571002e"><vh>Notes</vh>
<v t="ekr.20050227071948.29" annotate="7d71002e"><vh>drawing hooks</vh></v>
</v>
</v>
<v t="tbrown.20060828111141"><vh>@thin cleo.py</vh></v>
</v>
<v t="ekr.20050303080042"><vh> footprints</vh>
<v t="ekr.20050303080236"><vh>To do</vh></v>
<v t="ekr.20050303080042.1" tnodeList="ekr.20050303080042.1"><vh>@nosent footprints.ini</vh></v>
<v t="pap.20041020001240"><vh>@thin footprints.py</vh></v>
</v>
<v t="mork.20041018162155.1"><vh>@thin EditAttributes.py</vh></v>
<v t="ekr.20040915073259.1"><vh>@thin maximizeNewWindows.py</vh></v>
<v t="mork.20041022155742.1"><vh>@thin nodebar.py</vh></v>
<v t="edream.110203113231.924"><vh>@thin redirect_to_log.py</vh></v>
<v t="ekr.20040915075530"><vh>@thin UASearch.py</vh></v>
<v t="ekr.20040831122004"><vh>@thin UniversalScrolling.py</vh></v>
<v t="ekr.20040831115238"><vh>@thin URLloader.py</vh></v>
</v>
<v t="AGP.20230214111049"
marks="AGP.20230317140108,AGP.20230316112635.1,AGP.20230214111049.91,AGP.20230214111049.101,AGP.20230214111049.102,AGP.20230214111049.103,AGP.20230214111049.104,AGP.20230214111049.105,AGP.20230214111049.106,AGP.20230214111049.107,AGP.20230214111049.108,AGP.20230214111049.114,AGP.20230214111049.116,AGP.20230214111049.117,AGP.20230214111049.118,AGP.20230214111049.119,AGP.20230214111049.224,AGP.20230214111049.227,AGP.20230214111049.229,AGP.20230214111049.244,AGP.20230214111049.250,AGP.20230214111049.251,AGP.20230214111049.260,AGP.20230214111049.261,AGP.20230214111049.265,AGP.20230214111049.266,AGP.20230214111049.270,AGP.20230214111049.275,AGP.20230214111049.283,AGP.20230214111049.284,AGP.20230214111049.287,AGP.20230214111049.289,AGP.20230214111049.295,AGP.20230214111049.297,AGP.20230214111049.300,AGP.20230214111049.305,AGP.20230214111049.329,AGP.20230522153016,AGP.20230214111049.382,AGP.20230521193302,AGP.20230214111049.461,AGP.20230529114310,AGP.20230214111049.466,"><vh>@thin xcc_nodes.py</vh></v>
<v t="AGP.20230307095223"><vh>thin bin_nodes.py</vh>
<v t="AGP.20230307095223.1"><vh>Documentation</vh>
<v t="AGP.20230307095223.2"><vh>&lt;&lt; About this plugin &gt;&gt;</vh></v>
<v t="AGP.20230307095223.3"><vh>&lt;&lt; version history &gt;&gt;</vh></v>
<v t="AGP.20230307095223.4"><vh>&lt;&lt; what I did &gt;&gt;</vh></v>
<v t="AGP.20230307095223.5"><vh>&lt;&lt; what was redid/undid &gt;&gt;</vh></v>
<v t="AGP.20230307095223.6"><vh>Known Flaws</vh></v>
<v t="AGP.20230307095223.7"><vh>Future Features</vh></v>
<v t="AGP.20230307095223.8"><vh>Tracing Problems</vh></v>
<v t="AGP.20230307095223.9"><vh>XCC Explanation</vh>
<v t="AGP.20230307095223.10"><vh>The Three Distinctive Nodes</vh></v>
<v t="AGP.20230307095223.11"><vh>The Parser</vh></v>
</v>
</v>
<v t="AGP.20230307095223.12"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="AGP.20230307095223.13"><vh>&lt;&lt; globals &gt;&gt;</vh>
<v t="AGP.20230307095223.14"><vh>Icons</vh>
<v t="AGP.20230307095223.15"><vh>Go</vh></v>
<v t="AGP.20230307095223.16"><vh>StepIn</vh></v>
<v t="AGP.20230307095223.17"><vh>StepOver</vh></v>
<v t="AGP.20230307095223.18"><vh>StepOut</vh></v>
<v t="AGP.20230307095223.19"><vh>Pause</vh></v>
<v t="AGP.20230307095223.20"><vh>Stop</vh></v>
<v t="AGP.20230307095223.21"><vh>Doc</vh></v>
<v t="AGP.20230307095223.22"><vh>Watch</vh></v>
<v t="AGP.20230307095223.23"><vh>Config</vh></v>
<v t="AGP.20230307095223.24"><vh>Prompt</vh></v>
<v t="AGP.20230307095223.25"><vh>Xcmd</vh></v>
</v>
<v t="AGP.20230307095223.26"><vh>Colors</vh></v>
</v>
<v t="AGP.20230307095223.27"><vh>Module level</vh>
<v t="AGP.20230307095223.28"><vh>init</vh></v>
<v t="AGP.20230307095223.29"><vh>Module-level event handlers</vh>
<v t="AGP.20230307101554"><vh>OnCreate</vh></v>
<v t="AGP.20230307095223.32"><vh>OnSelect2</vh></v>
<v t="AGP.20230307182804"><vh>OnCreate</vh></v>
<v t="AGP.20230307095223.37"><vh>OnHeadKey2</vh></v>
</v>
</v>
<v t="AGP.20230307182502"><vh>class controllerClass</vh>
<v t="AGP.20230307182502.1"><vh>__init__</vh></v>
<v t="AGP.20230307182502.12"><vh>Event handlers</vh>
<v t="AGP.20230307182502.13"><vh>onSelect</vh></v>
<v t="AGP.20230307182502.15"><vh>onCommand2</vh></v>
<v t="AGP.20230307182502.18"><vh>onHeadKey2</vh></v>
</v>
<v t="AGP.20230307185825"><vh>GetParentBin()</vh></v>
<v t="AGP.20230307185825.1"><vh>IsAtBin()</vh></v>
<v t="AGP.20230307185825.2"><vh>ShowHexed()</vh></v>
<v t="AGP.20230307185825.3"><vh>HideHexed()</vh></v>
</v>
</v>
<v t="AGP.20230214101615"><vh>thin quicksearch.py - integrated into leo src</vh>
<v t="AGP.20230214101615.1"><vh>&lt;&lt; doc string &gt;&gt;</vh></v>
<v t="AGP.20230214101615.2"><vh>&lt;&lt; version history &gt;&gt;</vh></v>
<v t="AGP.20230214101615.3"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="AGP.20230214101615.5"><vh>onCreate</vh></v>
<v t="AGP.20230217110614"><vh>class History</vh>
<v t="AGP.20230217110614.1"><vh>__init__()</vh></v>
<v t="AGP.20230217112453"><vh>onKey</vh></v>
<v t="AGP.20230217110614.2"><vh>onFocusIn()</vh></v>
<v t="AGP.20230217110626"><vh>onFocusOut()</vh></v>
<v t="AGP.20230217110937" a="M"><vh>onLeftClick()</vh></v>
<v t="AGP.20230217111007"><vh>onMenuLeftClick()</vh></v>
<v t="AGP.20230217110956"><vh>onMenuMotion()</vh></v>
</v>
<v t="AGP.20230214101615.6"><vh>class SearchBox</vh>
<v t="AGP.20230214101615.7"><vh>__init__()</vh>
<v t="AGP.20230216131200"><vh>init vars</vh></v>
<v t="AGP.20230216131200.1"><vh>create widgets</vh></v>
<v t="AGP.20230218142713"><vh>Options menu</vh></v>
</v>
<v t="AGP.20230215183000"><vh>onFocusIn()</vh></v>
<v t="AGP.20230215152338"><vh>onFocusOut()</vh></v>
<v t="AGP.20230214101615.12"><vh>onkey</vh></v>
<v t="AGP.20230218130414"><vh>testcommand()</vh></v>
<v t="AGP.20230214114431"><vh>onRightClick()</vh></v>
<v t="AGP.20230218011003"><vh>find_repack()</vh></v>
<v t="AGP.20230218011952"><vh>change_repack()</vh></v>
<v t="AGP.20230216123933"><vh>destroy() dummy</vh></v>
<v t="AGP.20230216122007"><vh>leoFind implements</vh>
<v t="AGP.20230216235537"><vh> Top level</vh>
<v t="AGP.20230216235537.1"><vh>findAllCommand</vh></v>
<v t="AGP.20230216235537.2"><vh>findAgainCommand</vh></v>
<v t="AGP.20230216235537.3"><vh>cloneFindAllCommand</vh></v>
<v t="AGP.20230216235537.4"><vh>findNext/PrefCommand</vh></v>
<v t="AGP.20230216235537.5"><vh>change/ThenFindCommand</vh></v>
</v>
<v t="AGP.20230214101615.17"><vh>update_ivars</vh></v>
<v t="AGP.20230214101615.18"><vh>init_s_ctrl</vh></v>
</v>
</v>
</v>
<v t="AGP.20230207163742" a="M"
marks="AGP.20230207163742.15,AGP.20230207163742.58,AGP.20230207163742.64,"><vh>@thin node_colors.py</vh></v>
<v t="AGP.20230208000543" a="M"><vh>@thin body_rclick.py</vh></v>
<v t="AGP.20230214092456"
expanded="AGP.20230214092456.6,AGP.20230214092456.22,"><vh>@thin node_scripting.py</vh></v>
<v t="AGP.20240831123716"><vh>@thin keywords_nodes.py</vh></v>
<v t="AGP.20240902191147" a="E"
marks="AGP.20240902191425,AGP.20240903161242,"><vh>@thin version_file.py</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="AGP.20201210160828">class FUNCASMRULE:
    @others</t>
<t tx="AGP.20201210160828.1">def __init__(self,Parser):
    
    self.Parser = Parser	
    self.Matcher = re.compile("^__asm(?P&lt;HEAD&gt;.*)")
    </t>
<t tx="AGP.20201210160828.2">def Match(self,head):
    return self.Matcher.search(head)
</t>
<t tx="AGP.20201210160828.3">def OnMatch(self,mo,node):
    
    p = self.Parser
    p.CURRENT_RULE = "funcasm"
    
    w = p.FUNC_WRITER
    groups = mo.groupdict()
    
    head = groups["HEAD"]
    if head == None:
        head = ""
        
    p.CURRENT_LOCATION = 0  #head
    p.Tab()
    w(p.TAB_STRING+"//__asm"+head+"\n")
    
    if p.WriteOthers_asm(node,w) == False:
        return False
    
    p.CURRENT_LOCATION = 2  #tail
    p.UnTab()
    w("\n")

    return True
</t>
<t tx="AGP.20201210161232">def WriteOthers_asm(self,node,w):
    
    cc = self.cc
    if cc.CREATE_DOC == "True":
        doc = cc.cGet("DOC","",node)
        self.Docum(doc)
        
    b = node.bodyString().strip("\n")
    o = b.find("@others")
    
    self.CURRENT_LOCATION = 1   #body
    
    if o != -1:
        lb = b[:o]
        pnl = lb.rfind("\n")
        if pnl &gt; -1:
            lb = lb[:pnl]
        
        tb = b[o+7:]
        pnl = tb.find("\n")		
        if pnl &gt; -1:
            tb = tb[pnl+1:]        
        
        if lb != "":
            self.TabWrite_asm(lb+"\n",w)
        self.PushBodyLine()
        if self.ParseNode(node) == False:
            return False
        self.PopBodyLine()
        self.CURRENT_LOCATION = 1   #body
        self.TabWrite_asm(b[o+7:]+"\n",w)
        #self.TabWrite(b[o+7:],w)
    else:        
        #self.TabWrite(b+"\n",w)
        self.TabWrite_asm(b,w)
        if self.ParseNode(node) == False:
            return False
    
    return True
</t>
<t tx="AGP.20201210161442">def TabWrite_asm(self,text,outfunc):
    lines = text.splitlines(True)
    #if len(lines)==1 and lines[0]=="\n":
    #    return
    for l in lines:
        chunks = l.split("/",1)
        
        asm_code = chunks[0].strip()
        if asm_code != "":
            asm_code = "asm(\""+asm_code+"\\n\");\t"
        
        chunks[0] = asm_code
        
        lo = string.join(chunks,"/")
        
        outfunc(self.TAB_STRING + lo)
</t>
<t tx="AGP.20230214101615">&lt;&lt; doc string &gt;&gt;

@language python
@tabwidth -4

__version__ = "0.7"

&lt;&lt; version history &gt;&gt;
&lt;&lt; imports &gt;&gt;


@others

if Tk: # OK for unit testing.

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        leoPlugins.registerHandler("after-create-leo-frame", onCreate)
        g.plugin_signon(__name__)
        
</t>
<t tx="AGP.20230214101615.1">'''Add a quick search to Leo's toolbar.

A search box which behaves like a web site search is added, along with
a "GO" button to do quick searches right from the main Leo window. All the
current search options are retained except that "search body text" is
explicitely set - mainly because this is by far the most common use case.

Pressing &lt;CR&gt; while editing the text automatically does a search. Repeated
searches can be done by clicking the "GO" button.

The combo box also stores a list of previous searches, which can be
selected to quickly repeat a search. When activating a previous
search the original search mode is used.

Still to do:

- incremental search
- reverse search
- persist recent searches across Leo sessions
- use INI file to set options for list size etc
'''</t>
<t tx="AGP.20230214101615.2">@
0.4 EKR: Don't mess with button width on MacOS/darwin.

0.5 EKR: Create a separate SearchBox instance for each open window.
- This eliminates problems when multiple windows are open.
0.6 EKR: Changes required by revisions of leoFind.leoFind class in Leo 4.3:
- Removed '_flag' suffixes in OPTION_LIST.
- Added c arg to QuickFind ctor.
    - We now have per-commander find panels.
- update_ivars
    - Changed name from set_ivars.
    - Call setattr(self,key,0), not setattr(c,key+'_flag',0)
    - No more _flag hack.
    - Set self ivars, not c ivars.
- Changed init_s_text to init_s_ctrl.
    - Changed s_text to s_ctrl.
0.7 EKR: Fixed crasher in Leo 4.4 by initing self.p in Quickfind ctor.</t>
<t tx="AGP.20230214101615.3">import leoGlobals as g
import leoPlugins

import leoFind

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

#import ttk

import sys
import pickle,zlib,base64

#import leoEditCommands.py #leoEditCommands.py-&gt;createEditCommanders(c)
                            #c.searchCommands.findTabHandler</t>
<t tx="AGP.20230214101615.5">def onCreate(tag, keywords):
    
    # Not ok for unit testing: can't use unitTestGui.
    if g.app.unitTesting:
        return

    c = keywords.get("c")
    searchbox = SearchBox(c)
    
    
    #search.addWidgets()</t>
<t tx="AGP.20230214101615.6">class SearchBox(leoFind.leoFind):

    @others
</t>
<t tx="AGP.20230214101615.7">def __init__ (self,c):
    # Init the base class.
    leoFind.leoFind.__init__(self,c)
    
    self.c = c
    self.s_ctrl = Tk.Text() # Used by find.search()
    
    self.top = self #leo will call panel.top.destroy() in destroyallpanels()... see destroy() dummy
    
    #c.searchCommands.openFindTab(show=False)
    #self.finder = c.searchCommands.findTabHandler 
    #print self.findtab.dict.keys()
    
    c.searchCommands.findTabHandler = self
    
    self.finder = self
    
    self.rmenu = None
    
    
    
    
    @others
    
    </t>
<t tx="AGP.20230214101615.12">def onKey (self,event=None): 
    """Called when the user presses a key in the text entry box"""
    
    
    if self.lmenu != None:
        self.lmenu.destroy()
        self.lmenu = None
        
    
    #print event.keysym
    
    if event.keysym == "Return":
        sv = self.searchvar.get()
        if sv != "" and not sv in self.history:
            self.history.insert(0,sv)
            #self.searchbox.after_idle(self.doSearch)
        
        # when using fintab
        #self.finder.find_ctrl.delete("1.0","end")
        #self.finder.find_ctrl.insert("1.0",sv)
        
        c = self.c
        
        #if c.frame.findPanel != self.finder:
        #c.frame.findPanel = self.finder
        c.searchCommands.findTabHandler = self.finder
        
        self.p = c.currentPosition() # Bug fix: 5/14/06
        
        #c.findNext()
        #c.searchCommands.findTabFindNext()
        self.findNextCommand(c)
        
        
            </t>
<t tx="AGP.20230214101615.17">def update_ivars (self):
    
    """Called just before doing a find to update ivars."""

    for key in self.intKeys:
        # g.trace('settattr',key,False)
        setattr(self, key,False)

    self.change_text = self.changebox.var.get()
    self.find_text = self.searchbox.var.get()

    # Set options
    
    vd = self.dict
    
    for k in self.dict.keys():
        setattr(self, k, vd[k].get())</t>
<t tx="AGP.20230214101615.18">def init_s_ctrl (self,s):
    t = self.s_ctrl
    t.delete("1.0","end")
    t.insert("end",s)
    t.mark_set("insert",g.choose(self.reverse,"end","1.0"))
    return t
</t>
<t tx="AGP.20230214114431">def onRightClick(self,event):    
    try:
        self.rmenu.tk_popup(event.x_root+1,event.y_root-10)
    finally:
        self.rmenu.grab_release()
</t>
<t tx="AGP.20230215152338">def onFocusOut(self,event):
    if self.lmenu != None:
        self.lmenu.destroy()
        self.lmenu = None</t>
<t tx="AGP.20230215183000">def onFocusIn(self,event):
    self.searchbox.select_range(0, Tk.END)
</t>
<t tx="AGP.20230216122007"></t>
<t tx="AGP.20230216123933">def destroy(self):
    pass</t>
<t tx="AGP.20230216131200">#tkinter ivars
#self.searchvar = Tk.StringVar()
#self.changevar = Tk.StringVar()

self.dict = vd = {}

for key in self.intKeys:
    vd[key] = Tk.IntVar()

for key in self.newStringKeys:
    vd[key] = Tk.StringVar()

        
#set some default options
vd["search_headline"].set(1)
vd["search_body"].set(1)
vd["ignore_case"].set(1)
vd["radio-search-scope"].set("entire-outline")

#for k in vd.keys():
#    print k,vd[k].get()</t>
<t tx="AGP.20230216131200.1">#create widgets
self.toolbar = toolbar = c.frame.iconFrame


self.changebox = cb = History(toolbar)


self.tolabel = Tk.Label(toolbar,text="To")


self.searchbox = sb = History(toolbar)   

#sb.bind("&lt;Key&gt;", self.onKey)
sb.bind("&lt;Button-3&gt;", self.onRightClick)

self.action_button = ab = Tk.Menubutton(toolbar,text="Find",activebackground="light sky blue")


self.action_menu = am = Tk.Menu(ab,tearoff=0,takefocus=0)
ab["menu"] = am

self.find_repack()

</t>
<t tx="AGP.20230216235537"></t>
<t tx="AGP.20230216235537.1">def findAllCommand (self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    self.findAll()
</t>
<t tx="AGP.20230216235537.2">def findAgainCommand (self):
    self.findNextCommand()
    return True
</t>
<t tx="AGP.20230216235537.3">def cloneFindAllCommand (self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    self.clone_find_all = True
    self.findAll()
    self.clone_find_all = False
</t>
<t tx="AGP.20230216235537.4">def findNextCommand (self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    return self.findNext()
    
def findPrevCommand (self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    self.reverse = not self.reverse
    ret = self.findNext()
    self.reverse = not self.reverse
    return ret</t>
<t tx="AGP.20230216235537.5">def changeNextCommand (self,event=None):
    if self.findNextCommand():
        self.changeCommand()

def changeCommand (self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    self.change()
    
def changeAllCommand (self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    self.changeAll()
    
def changeThenFindCommand(self,event=None):
    self.p = self.c.currentPosition()
    self.setup_command()
    self.changeThenFind()


</t>
<t tx="AGP.20230217110614">class History(Tk.Entry):
    @others</t>
<t tx="AGP.20230217110614.1">def __init__(self,parent,width=30,bd=2,):
    
    self.var = Tk.StringVar()
    
    Tk.Entry.__init__(self,parent,width=30,bd=2,exportselection=0,textvariable=self.var)#,takefocus=1))
    
    self.bind("&lt;Key&gt;", self.onKey)
    self.bind("&lt;FocusIn&gt;", self.onFocusIn)
    self.bind("&lt;FocusOut&gt;", self.onFocusOut)
    self.bind("&lt;Button-1&gt;", self.onLeftClick)
    
    self.history = []
    self.lmenu = None
    
    self.action = None
    
    

    
    </t>
<t tx="AGP.20230217110614.2">def onFocusIn(self,event):
    self.select_range(0, Tk.END)
</t>
<t tx="AGP.20230217110626">def onFocusOut(self,event):
    if self.lmenu != None:
        self.lmenu.destroy()
        self.lmenu = None</t>
<t tx="AGP.20230217110937">def onLeftClick(self,event):
    
    if self.lmenu != None:
        self.lmenu.destroy()
        self.lmenu = None
    
    h = self.history
    if len(h) &gt; 0:
        self.lmenu = lmenu = Tk.Listbox(
                                            self.winfo_toplevel(),
                                            width=30,
                                            height=len(h),
                                            takefocus=0,
                                            bg="white",
                                            activestyle="none",
                                            selectmode=Tk.SINGLE
                                        )
        
        lmenu.bind("&lt;Motion&gt;", self.onMenuMotion)
        lmenu.bind("&lt;Button-1&gt;", self.onMenuLeftClick)
        
        
        for s in h:
            lmenu.insert(Tk.END,s)
        
        
        
        x= event.widget.winfo_x()
        y= event.widget.winfo_y()
        h= event.widget.winfo_height()
        
        #print x,y,h
        lmenu.place(x=x+1,y=y+h,anchor=Tk.NW)
        
        
    
        
    </t>
<t tx="AGP.20230217110956">def onMenuMotion(self,event):
    self.lmenu.selection_clear(0,Tk.END)
    self.lmenu.selection_set(self.lmenu.nearest(event.y))</t>
<t tx="AGP.20230217111007">def onMenuLeftClick(self,event):
    self.var.set(self.lmenu.get(self.lmenu.curselection()[0]))
    self.focus_set()
    
    self.lmenu.destroy()
    self.lmenu = None
    
    return "break"</t>
<t tx="AGP.20230217112453">def onKey (self,event=None): 
    """Called when the user presses a key in the text entry box"""
    
    if self.lmenu != None:
        self.lmenu.destroy()
        self.lmenu = None
    
    if event.keysym == "Return":
        sv = self.var.get()
        if sv != "" and not sv in self.history:
            self.history.insert(0,sv)
            
        if self.action != None:
            self.action()
</t>
<t tx="AGP.20230218011003">def find_repack(self):
    self.changebox.pack_forget()
    self.tolabel.pack_forget()
    self.searchbox.pack_forget()
    self.action_button.pack_forget()

    #self.changebox.pack(side="right", padx=0, pady=0,fill="y", expand=0)
    #self.tolabel.pack(side="right", padx=2, pady=0,fill="y", expand=0)
    self.searchbox.pack(side="right", padx=2, pady=0,fill="y", expand=0)
    self.action_button.pack(side="right", padx=3, pady=0,fill="y", expand=0)
    
    self.action_button.config(text="Find")
    
    am = self.action_menu
    am.delete(0, am.index(Tk.END))
    
    am.add_command(label="Find Next",command=self.findNextCommand)
    am.add_command(label="Find Prev",command=self.findNextCommand)
    am.add_command(label="Find All",command=self.findAllCommand)
    am.add_command(label="Clone Find All",command=self.cloneFindAllCommand)
    am.add_separator()
    am.add_command(label="Change Mode",command=self.change_repack)
    
    
    
    self.searchbox.action = self.changebox.action = self.findNextCommand</t>
<t tx="AGP.20230218011952">def change_repack(self):
    self.changebox.pack_forget()
    self.tolabel.pack_forget()
    self.searchbox.pack_forget()
    self.action_button.pack_forget()

    self.changebox.pack(side="right", padx=0, pady=0,fill="y", expand=0)
    self.tolabel.pack(side="right", padx=2, pady=0,fill="y", expand=0)
    self.searchbox.pack(side="right", padx=0, pady=0,fill="y", expand=0)
    self.action_button.pack(side="right", padx=2, pady=0,fill="y", expand=0)
    
    self.action_button.config(text="Change")
    
    am = self.action_menu
    am.delete(0, am.index(Tk.END))
    
    am.add_command(label="Change Next",command=self.changeNextCommand)
    am.add_command(label="Change Prev",command=self.changePrevCommand)
    am.add_command(label="Change All",command=self.changeAllCommand)
    am.add_command(label="Change And Find",command=self.changeThenFindCommand)
    am.add_command(label="Change Selection",command=self.changeCommand)
    am.add_separator()
    am.add_command(label="Find Mode",command=self.find_repack)
    
    self.searchbox.action = self.changebox.action = self.changeNextCommand</t>
<t tx="AGP.20230218130414">def testcommand(self):
    print "testcommand",self
</t>
<t tx="AGP.20230218142713">self.rmenu = rmenu = Tk.Menu(self.searchbox.winfo_toplevel(),tearoff=0,takefocus=1)
    
vd = self.dict
    
#for k in vd.keys():
#    print k,vd[k].get()
    
rmenu.add_checkbutton(label="Search Headline",variable=vd["search_headline"])
rmenu.add_checkbutton(label="Search Body",variable=vd["search_body"])
    
    
rmenu.add_separator()
#rmenu.add_command(label="_________________")
    
rmenu.add_radiobutton(label="Entire Outline",variable=vd["radio-search-scope"],value="entire-outline")
rmenu.add_radiobutton(label="Suboutline Only",variable=vd["radio-search-scope"],value="suboutline-only")
rmenu.add_radiobutton(label="Node Only",variable=vd["radio-search-scope"],value="node-only")
    
rmenu.add_separator()
rmenu.add_checkbutton(label="Mark Finds",variable=vd["mark_finds"])
rmenu.add_checkbutton(label="Mark Changes",variable=vd["mark_changes"])
    
rmenu.add_checkbutton(label="Ignore Case",columnbreak=1,variable=vd["ignore_case"])
rmenu.add_checkbutton(label="Whole Word", variable=vd["whole_word"])
rmenu.add_checkbutton(label="Wrap Around",variable=vd["wrap"])
rmenu.add_checkbutton(label="Reverse",variable=vd["reverse"])
rmenu.add_checkbutton(label="Regexp",variable=vd["pattern_match"])</t>
<t tx="AGP.20230307095223">"""Integrate C/C++ compiler and debugger in a node."""

&lt;&lt; About this plugin &gt;&gt;
&lt;&lt; version history &gt;&gt;
&lt;&lt; what I did &gt;&gt;
&lt;&lt; what was redid/undid &gt;&gt;
&lt;&lt; imports &gt;&gt;

controllers = {}

if 1: # To be replaced by ivars
    &lt;&lt; globals &gt;&gt;

@language python
@tabwidth -4

__version__ = "0.5"

@others</t>
<t tx="AGP.20230307095223.1"></t>
<t tx="AGP.20230307095223.2">@nocolor
@ 			X C++ Compiler nodes----
PLEASE SEE http://xccnode.sourceforge.net/
 The xcc_nodes.py plugins simplify c++ syntax and integrate compiling and debuging tools.

To start debugging, create a node whose headline is::

    @xcc projectname

or::

    @xcc projectname.ext

The optional extension (*.ext) set the kind of project the node will build.
An empty extension is equivalent to the '.exe' extension.

As soon as "@xcc" is written in the headline the plugin creates an empty configuration.

    if ext == cpp,
        inflate name.cpp
        the node will attempt to build an executable
    if ext == h,
        inflate name.h
        the node will attempt to check the syntax of the header
    if ext == exe,
        this is equivalent to no ext at all
        inflate name.h and name.cpp
        the node will attempt to build an executable
    if ext == dll,
        inflate name.h and name.cpp
        the node will attempt to build a dynamic link library
    if ext == lib,
        inflate name.h and name.cpp
 			the node will attempt to build a static link library

Creating programs

The "@xcc" node support Leo's @others syntax but **not**  section references.
 	The actual code is written in the children of the main node and the code generation is
 	affected by headlines.

 	Here are the rules: (see examples for good understanding)
- The '@' rule: If a headline starts with "@", the node and its children are ignored.

- The semicolon rule: If a headline ends with ";" and another compatible rule is trigered in the
 same headline, the rule will be written in the source if there is one.

**//**: If a headline start with "//", all its body and children are commented out as follows::
    /*headline
        body text
        and
        childs
        */

This rule is compatible with the ';' rule.

- The function rule: If a headline ends with ")", the headline is used as funtion prototype.
  The body and children are encased automatically in the opening and closing curly brace.

  The class and function rules are disabled while in a function rule.
  The function rule is compatible with the semicolon rule, except that if there is a
  header in the project the function will always be declared in the header and
  defined in the	source, appending "!" prevents declaration in header for global functions.

- The class rule: If a headline starts with "class", a class is declared and opening and
  closing curly brace are automatically written, all the children of this node are class members,
  the functions are correctly dispatched between header and source (access specifier is
   appended if needed).

- The "Default" rule: If a headline doesn't match any of the preceeding rules,
  its headline is written as a comment and the body and childs written "as is" as follows::

    //headline
        body text
        and all children.

This rule is compatible with the semicolon rule.

-&gt; Config Panel reference:
	-&gt; options : generally the most used options.
		-&gt; Create files : Request that files should be inflated.
		-&gt; Compile : Request that the project should be built using the configured compiler.
			-&gt; Seek first error : Attempt to locate the first error encountered.
		-&gt; Execute : Request to run the built exe.
			-&gt; Connect to pipe : Interface the built exe pipe to the node interface, exe is simply spwned if unchecked.
		-&gt; Debug : Request to run the built exe with the configured debugger (overide the "Execute" option).
			-&gt; Seek breapoints : Detect and "Goto" encountered breakpoints.
		-&gt; Xcc verbose : Special verbose mode usefull to config the debugger and widely used when coding the plugin
 		-&gt; Filter output : Filter compiler and debugger ouput, showing only error and warning
		-&gt; Colorize log : Colorize the output if checked, allowing easyer browsing.

- by Alexis Gendron Paquette</t>
<t tx="AGP.20230307095223.3">@nocolor
@

v 0.1: Alexis Gendron Paquette. - web &amp; graphics: Felix Malboeuf

v 0.2 EKR:
- Add per-node controller class.  This required many changes.
- Many stylistic changes.  More are coming.

v 0.3 EKR:
- Fixed a large number of crashers due to the reorganized code.
- The major panels now appear to work.

v 0.4 EKR:
- Added a ``what I did`` section.
- Made UpdateProcess a cc method.
- It appears that cc.OPTS is not set properly in PageClass.LoadObjects.
  This prevents the compiler from working.
v 0.5 AGP:
- Asserted compatibility with leo 4.4.2.1 final
- Many bug fix and improvement regarding line numbers and scroll system.
- Added Language pane allowing to configure the node for almost any language.
- Added a tool launch sequencer in the option pane.
- Added a Xcmd toggleable pane.
- Began basic Linux testing, major problem reside in the use of "\" wich worked in win32 wherea linux seem to require "/". Since window use both, the solution is to always use "/".
- Lot of other improvement.</t>
<t tx="AGP.20230307095223.4">@nocolor
@

**Important**: I have spent 8 or more hours making the following changes.
Without doubt I have introduced some bugs while doing so. However, it was
important to make these changes, for the following reasons:

1. This is very important code, and deserves the best packaging.

2. This code may form the basis of a Python-oriented debugger, so I wanted
   to make the code base as solid as possible.

3. Working and debugging code is the best way for me to really understand it.

Here is what I have done in detail:

- Eliminated * imports:
    ``* imports`` are bad style in complex code.
    Replaced ``from leoPlugins import *`` by ``import leoPlugins``
    Replaced ``from leoGlobals import *`` by ``import leoGlobals as g``
    Replaced ``from Tkinter import *`` by import Tkinter as Tk.
        Replaced Tk constants like END, FLAT, NW, etc. by 'end','flat','nw', etc.

- Created the module-level init function that registers all hooks.
  This is the recommended style: it shows in one place where all the hooks are.

- Removed most try/except handling.
    - Such handling is *usually* unnecessary, especially since Leo does a good job
      of recovering from crashes. However, try/except blocks might be important
      when executing user code, so perhaps it will be necessary to put some back in.
    - Replaced ``x = aDict[key]`` by ``x = aDict.get(key)`` to avoid exceptions.

*** Eliminated *all* global variables (except commanders) as follows:

- Created per-commander controller class instances.
    - The controllers dictionary is the only global variable.
    - The new OnCreate event handler creates controller instances.
    - Replaced all global variables by ivars of the controller class.
    - Global constants still exist.
    - Most former global functions now are methods of the controller class.
    - By convention, cc refers to the proper controller, i.e., the controller for the proper commander c.
    - cc gets passed to the constructor of almost all classes.
    - Replaced init logic (start2 hook) by logic in the ctor for the controller class.

- Simplified module-level event handlers.
    - They simply call the corresponding event handler in the proper controller instance.

- Renamed most classes from XXX to XxxClass.

- Eliminated the Parser global.
    - All Rule classes now get a Parser argument and define self.Parser.

- Disabled some weird code in OnIdle.  I'm not sure what this is supposed to do.

- Create a new pause module-level function that calls winPause or linPause as appropriate.

- Used more Pythonic or Leonic ideoms in many places:
    - Replaced ``if x == True:`` by ``if x:``.
    - Replaced ``if x == False:`` by ``if not x:``.
    - Replaced ``if x != '':`` by ``if not x:``
    etc.
    *** Warning: these simplifications might cause problems.
        For example, the re module uses None as a sentinal, and can also return 0,
        so tests like ``if result:`` are not correct in such cases.  I have tried
        not to simplify the code "too much" but I may have made mistakes.
    *** if p is a node, ``if p == None:`` *must* be replaced by ``if not p:``.
    - cc.VERBOSE and cc.FILTER_OUTPUT now have values True/False instead of 'true'/'false'.
    - Defined TraceBack as g.es_exception.
    - Changed ``Error(x) ; return`` to ``return Error(x)``, and similarly for Warning, etc.

- Simplified the code wherever possible.
    - Sometimes the change can be dramatic, as in cc.cGetDict.

* There does not seem to be any definition of ExtractLines.</t>
<t tx="AGP.20230307095223.5">@nocolor
@

Ok, Edward made a great job on its own and has he expected somme bugs where introduced but nothing too serious. I finished the code adaptation and resolved the bug. I tried as much as possible to follow Ed's syntactic rules. The major bugs introduced where caused by the replacement of code like "if x == "True"" by "if x == True" or "if x". The config store those value as the string, thats why they are compared against strings. I cant explain why those tree form doesnt produce the same effect by i can tell that they where causing trouble, so for now i use only comparition against string.

Ther was also problems with the leo tracing system, see the "Tracing Problems" node that follow.

</t>
<t tx="AGP.20230307095223.6">@nocolor
@ 

*** Most flaw can be worked around by using "default" node(or rule) and writing all	code inside it.
 (default rule -&gt; comment out headline &amp; write body "as is")

- line number refresh isnt 100% accurate when editing text in the body.
- Breakpoints can only be Added/deleted, Enabling/Disabling isnt supported yet.
- code auto dispath feature wont work as expected with template class and function.
- class is the only structural keyword supported in the tree to date, union, struct and enum dont trigger any rule.
- DLL debugging is untested to date, it surely dont work.
- Untested on Linux, see linPause and aPause functions.</t>
<t tx="AGP.20230307095223.7">@nocolor
@

- C/C++ code/project importer/merger
- Display external files if needed.(external error or similar)
- "Browse Info" management allowing declaration/references to be searched and displayed.
- Automation of precompiled headers, possibly using a "#PCH" node.
- in the debugger regular expression/task list:
    reg exp:
        if a group named "FOO" is returned by the regular
        expression, then the "_FOO_" variable is supported
        by the corresponding "Task" line.
    Task:
        Apart from those defined by the corresponding regular	expression,
</t>
<t tx="AGP.20230307095223.8">@
-the g.trace func seem to randomly crash:
----------------------------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Documents and Settings\gendroal\Programs\leo\plugins\xcc_nodes.py", line 884, in onIdle
    cc.UpdateProcess()
  File "C:\Documents and Settings\gendroal\Programs\leo\plugins\xcc_nodes.py", line 979, in UpdateProcess
    g.trace()#ProcessClass.List
  File "C:\Documents and Settings\gendroal\Programs\leo\src\leoGlobals.py", line 1650, in trace
    print name + ": " + message
IOError: [Errno 9] Bad file descriptor
----------------------------------------------------------------------------------------

    This crash occur on idle time when opening leo with xcc_nodes enabled, it show up randomly even if nothing is touched and no file operation is made by the xcc plugin.
    Seem that the only file descriptor present is the one used by the "print" statement.

-try/except block were re-added to nearly all the plugin entry points, wich are:
    -All module level events handler
    -The funcs called by the plugin buttons:
        in ToolbarClass.Go &amp; Refresh
        in ControllerClass:
            aPause
            aStop
            aStepIn
            aStepOver
            aStepOut
        in ConfigClass.Show &amp; Hide
        in ConfigClass.CplPageClass.Browse &amp; AddPath
        in ConfigClass.DbgPageClass.Browse
        in WatcherClass.Show &amp; Hide
- All g.trace occurence were commented out
</t>
<t tx="AGP.20230307095223.9">@
UNFINISHED

The xcc nodes idea emerge from a unpublished simple plugin called cpp_nodes that i'v developed about 2 years ago. The aim of the cpp nodes plugin was to reduce redondant c++ syntaxe. It then was obvious what the next step was going to be, the breeding of the cpp nodes with the run nodes. The outcoming xcc plugin result, with the aid of already present leo's feature, in a powerfull code managing and building software. It work for any laguage and tool we'v tried so far, from assembler to c++, from sdcc to windebug.

Special coding effort are made for this plugin to work in linux, but unfortunately i have no report of any actual testing for that.


Overall operation of the node is separated in three main actions.

Firstly the source and documentation files are generated by interfacing the ParserClass, wich propose a generic parsing algorithm(tought it was developed for c++), with opened files write methodes.

Secondly the build sequence is launched by running the configured tools with a boosted version of the run_nodes plugin PROCESS class.

Thirdly, if configured for, the debugger will be launched for an interactive debuging session.


</t>
<t tx="AGP.20230307095223.10">@
Amongst the members of the controllerclass, SELECTED_NODE, ACTIVE_NODE and CHILD_NODE are some valuable and cherished companions. Hence they are great clue of generale implement's stance. One who meddle with therein divine matter is to make vigilant awareness of the nameless trinity.</t>
<t tx="AGP.20230307095223.11">@
The ParserClass is one of the core component of the plugin, it run a set of syntactic rules on the child nodes headlines. When a rule trigger, it usually write the headline and the body(@others too) by using the Declare(),Define() or Docum() function from ParserClass. These three functions are the only outputs of the plugin(apart from config save), and in fact they are not entirely output, the ParserClass must be configured to do whatever suit one. Each of these increment a specific variable contained in the parser. Define()\Declare() increment CURRENT_SRC_LINE\CURRENT_HDR_LINE and Docum() incremnent CURRENT_DOC_LINE. Apart from the increment they call functions contained in three separatelist, DEC_PROC_LIST, DEF_PROC_LIST and DOC_PROC_LIST(now try to guess wich function call wich list). In the ParserClass the lists are empty by default, so it produce nothing on its own.</t>
<t tx="AGP.20230307095223.12"># from leoPlugins import *
# from leoGlobals import *
import leoPlugins
import leoGlobals as g

# from Tkinter import *
import Tkinter as Tk
import traceback
import os,sys,thread,threading,time,string,re
import tkFileDialog,tkMessageBox,tkSimpleDialog
import pickle,base64,zlib


Pmw = g.importExtension('Pmw',    pluginName=__name__,verbose=True,required=True)</t>
<t tx="AGP.20230307095223.13">@others

path_sym = "\\"

LeoTop = None
LeoFrame = None

LeoBodyText = None
LeoBodyParent = None
LeoYBodyBar = None
LeoXBodyBar = None

HexView = None
</t>
<t tx="AGP.20230307095223.14">#binary mapping: 00 0000 (6bit)MSB-&gt;LSB
# b0:mark
# b1:doc
# b2:content
# b3:clone
# b4-5:type : class func or comment
MARK_MARK = 1
DOC_MARK = 2
CONTENT_MARK = 4
CLONE_MARK = 8

FUNC_MARK = 0
CLASS_MARK = 16
</t>
<t tx="AGP.20230307095223.15">Go_e = "S\'x\\xdam\\x8e\\xcbn\\x830\\x14D\\xf7\\xfcLk \\xb2\\xbc\\xe8\\xe2\\xda@\\xc4\\xd32\\xe0\\x90.!J\\xa1\\x04\\x02\\x04K\\x80\\xbf\\xbeV\\xd6\\x1d\\xe9\\xe8\\x8cf5\\xf9\\xe7p\\xe6\\xde\\xd0\\xf9\\x00\\x02R\\x01\\xc0\\x9b\\xbb\\xa3\\xf0\\xfdd@\\nWH5\\x95\\xe9\\x956\\xd6+\\xe6\\x844\\xdcl|\\xbf]\\x03\\xfd\\xb2\\t\\xc16r\\x96j \\xa7\\xe3f\\xe9\\xb9\\x90\\xea\\xfbH\\xb1[\\xf8\\xfa\\xa90v2\\xadG\\xf5\\xc2v\\xd6\\x7f\\x18\\x88\\x01\\x8d\\xaa\\xef\\x83\\xb9v\\x1es\\xdc\\xc1?a\\xdb[\\xd6\\xfb\\x11@X\\t(\\x19\\xdd\\xc35\\xa6\\xd4\\x83)\\x8d\\x1fG\\xeb\\x8a\\x98uB\\xa2K\\xd2\\xb5\\xc0#\\xf8\\xcd\\xe5xI\\x8ap\\x95\\xb1\\xdf\\x8b\\x15_\\x9eT\\xf8\\xac\\xf4X\\\'\\xd7\\xf9,\\xc0\\x92u\\x11\\xc0\\x81\\xf2i\\xd8\\xdbtIR\\xdaJw\\x9aD\\xbb\\xf1(b%\"\\xf5\\x02b\\x8b\\x7f\\x80n\\xa2E]\\xe1f~\\x00\\xe0\\xad_\\xd6\\x1f\\x96\\x88[)\'\np0\n."</t>
<t tx="AGP.20230307095223.16">StepIn_e = "S\'x\\xda\\x95\\xd0Ms\\x820\\x10\\x06\\xe0;\\x7f\\xa5\\x17\\x15\\xa6\\x0e\\x87\\x1e6\\x100|\\x9a\\xa4\\x0c\\xda\\x9bP\\x0b\\x02\\x82\"\\x18\\xf0\\xd77\\xe1\\xdaS3\\xf3dg\\x92\\xec\\xbb3a\\xab\\xc6\\x8d\\xed\\xa6\\xc4\\x00\\x14\\xa2\\x04 \\xce\\xae\\xfa\\x98\\x9d\\xf5a{^\\x0f\\xdbTy\\r\\x99\\x12+S\\xbe\\x95R\\xf3)\\r\\xd9\\xc6|J\\xb2\\xae\\xe5\\x93\\xb5\\xa6\\xb6\\xfe\\xb4\\x19n\\xa7\\xb4QZo\\xce\\x95\\xc6\\xe3\\x89Ry&lt;\\xac\\xc8\\xac\\xe0\\x92\\xf0\\xc52I\\xca\\xf5\\xe1\\x95\\xeb\\xd1\\xe2\\xa4G\\xbd&amp;sTV\\x7f\\xdcD\\x95\\x92\\xaa\\x84\\xfa\\xe6\\xf3\\xfaf\\xd1\\xda\\xb3h\\x85\\xa7\\x90\\xab\\x03\\x99\\xc3\\xea/\\x97\\x01\\xc5P\\x10\\x0b\\xfe.\\r\\xfe\\xb3,\\xb1\\x94\\xe5K\\x00H\\x05\\xb0\\xb7\\xd0D\\x1e&gt;\\x02{\\xee\\xb8v\\x7f \\x01\\xc4A\\x05\\x159\\x8f^\\xd4\\xe8\\xb8+\\xef\\xcfQ5O\\x06\\xd0\\x10\\x17yq\\xddU\\xc4H(B(\\x19-\\x87N\\x82\\xcb\\x8e\\x82\\xf8c\\x8f\\x8aU\\xe8\\x072\\x9b\\x89\\x1d\\x08m\\x15\\xbb\\xc8f\\xc2\\xb7\\xf6\\xcc\\xeb.\\x07\\x84\\xcb\\x90\\xec\\x03Q\\xd0\\xb1\\xa4\\x989\\xf7\\x9f\\x16\\xdek,\\x1b&gt;\\x9b\\xef\\xc0\\xb6\\x8f\\x1d=\\xc4\\xed\\xe5M\\x0e\\xe1\\x8c^Z\\xe4|\\xd2 j\\x10\\x1a\\xf8.\\xd3J\\xd1\\xcd\\x1e\\xb2\\rJb\\xd4\\x82i:\\x85 `?&gt;\\xb4_\\xa4j\\x9b\\xc9\'\np0\n."</t>
<t tx="AGP.20230307095223.17">StepOver_e = "S\'x\\xda\\x95\\xd0Mo\\x830\\x0c\\x06\\xe0;\\xbf\\xa6|hh\\x87\\x1e\\x9c\\x10h`@\\x03\\xed(\\xbbA\\x86\\xc2\\x97J\\x05l\\x01~\\xfdHw\\x9f\\xb4Wz\\xec\\x8b-YN\\x0e\\xbd\\x17;}M\\x00\\x18DW\\x80\\xc8\\xae\\xf4\\xd9\\xce\\x94m.\\x95XY\\xb8\\xad\\xb8\\xca7\\xbf\\xed\\xb2We.\\rE\\xdfGuM\\x95\\xb1\\xccf\\xe5Q\\x18\\xf3\\xb8{\\x14Y\\xaf\\xdc\\x83\\x8c\\xdf\\xfd\\x95\\xf7\\xfez\\xed\\xe9\\x1a\\xb6t%5M\\x9f*s\\xb6+3\\xda\\xf8\\xae0#\\xb56j\\xb9\\xfe\\xbbz\\xed\\xfdTI\\xbbG\\x90v&gt;f\\xed\\xf0\\x12\\xb7d\\t\\x93\\xee\\xc3K\\x80\\x11\\x10\\x14\\xc3\\xdf\\xd1\\xe0?\\xc1\\xf2\\xd9\\x9e/\\x01\\xa0\\x8d\\x847\\x8c\\x16:\\x05\\x08\\xe1uJ\\xb5\\xb1\\xc3IN]$\\x98\\x90\\\'\\x1f\\xa4\\xcc\\xc3\\xc0\\x850\\x8c\\x9a\\xba\\xa6A\\xec\\x92U\\xcf\\xc0At\\x10\\x11r\\x93\\xeb\\x019\\xc8bS\\x02\\x08\\x1f\\x863\\x96\\xcc\\xea.\\x1e\\x08\\xbd8a4hy\\x00\\x143\\xdf\\xee\\xef\\xb5\\xe0\\xd4\\xa3h\\xab\\x9c\\xf2\\xaba\\xef\\x1e\\xc6\\x84I\\xcag!\\xac\\x98\\x9cH\\xcbo\\x13\\x069Y\\xa9?b\\x03\\xce\\xedV[\\xc5%\\xac\\x97O\\xc2\\xb1!)\\xb9]4Q\\x87\\xab\\xe77\\xc2\\xca\\xf4\\xb30\\xf9\\xdb~\"\\xc4\\xf2x\\xd4~\\x00\\\'\\xed\\x9a\\xd0\'\np0\n."</t>
<t tx="AGP.20230307095223.18">StepOut_e = "S\"x\\xda\\x95\\xd0\\xddn\\x820\\x14\\xc0\\xf1{\\x9eF\\xc5\\x8c\\xedb\\x17\\xa7\\xa5`a\\x80\\x05;\\xd4;As\\xca\\x87\\x9bQ\\x94\\x8f\\xa7_\\xcb\\x1b\\xac\\xc9/\'9i\\xfeM\\x9a.Z?q[\\xc5\\x00\\x04\\xc4\\x12 )\\xae\\xf6\\xb3\\xb8\\xd8\\x9dsYvNnL]a$\\xc6P:\\xda\\xde{\\x95\\xf9\\x87\\xd1\\x15\\xab\\x8f\\x97\\xa6\\xe7\\xd2\\xd2\\xf7\\x96\\xc6\\xbd\\xc8;\\xe3vZiy\\xab\\x95?\\xc18k\\x83L\\xd6A\\x16\\xd5|\\x8c\\x14\\x1f\\x99\\xe2\\xd9\\xec\\xb2N\\x9d\\xf9U\\xad\\xb4\\xbb\\xc9*\\xedx2Nv|\\xd7\\x9d\\xd9a\\x15\\xd7F~\\x8duV\\x97\\x9a[\\x985\\x01\\x15\\xf5\\xef[R\\xb3!\\xca\\xccB\\xf7\\xd2\\xe6\\xe8\\xa7 \\x18 \\xa7\\x00`\\xc1\\x7f\\x0e\\xed\\xe71\\x7f\\t\\x00o\\x01\\xb6\\x94\\x0c\\\\\\xfa\\xd4E\\xc4\\xad\\xa5\\xb7\\x04\\x9b\\xfc\\x8b\\x02\\xde7A\\x8f\\xb8\\x90\\xa17E\\xef\\x8ce=6\\x8c\\xd0\\x1d[\\xec&lt;\\xa2\\xb8\\xdc\\x10w|\\x84\\x02\\xf0\\xb6\\xe0\\xd2S4F\\xeaUp8\\xd1\\xe8\\x8ar\\x98\\xa0\\xea\\xad\\xa6&lt;\\xb9(\\x90\\x9d_J\\x08\\xdf\\x150\\x9e/\\xacI\\x15J\\x97\\xba4\\x0f\\xfdjI c&gt;\\xfb\\xe6\\x9b\\xfd/\\x0e\\x870\\x8a\\x08*2$\\x10\\x9c\\xf91\\xc3*&gt;$t\\xbf\\x86\\xeaL,2\\xae\\xc6M\\xa3{O\\x07H\\xfa\\x90\\x94\\xef\\xa0/]_\\xb1\\xf2\\x8b\\xa0\\x80\\xa4\\xff\\xfc\\xb4\\xfe\\x00\\xd4\\xc7\\xa1 \"\np0\n."</t>
<t tx="AGP.20230307095223.19">Pause_e = "S\'x\\xda\\x95\\xceKn\\x830\\x18\\x04\\xe0=\\x97i\\xf3t\\xba\\xc8\\xe2\\xb7\\t\\xc6N\\xb0e\\x08\\x02\\x96\\x85\\x02\\x86:\\x84\\x14Wn9}Q{\\x82\\x8e\\xf4I\\xb3\\x19i\\xe2gC\\xa5o\\xf4\\t@A\\xa4\\x00\\x04\\xaa7\\x16e+[f\\xbb\\xc5f1\\xdbR.]\\xce\\x13Z\\xe4\\xc1\\xcb!\\x0f\\xd0&gt;3\\x03OR\\xc3\\x92\\x93\\t-\\xeaC1{\\x9a\\x8a\\xfeim?\\xea\\xb5\\xedM\\xc0\\x93\\xda\\xc1\\xffC\\xfeF\\xde\\xef#\\x00V(\\x10\\x04\\x7f\\xb1\\xe9\\xec\\xe3\\xd6U\\xb9\\x0c}\\xd82B\\xb4\\xdaJ\\xca\\xaf\\xeeN\\x19&amp;8m8\\xef\\x8aT\\xf9\\xb4\\xd3\\xd3%}\\xcc\\xf7(\\x13\\xac\\xed\\xa2\\xc6\\x80\\xday\\xef\\xcc\\x07\\x03\\xac\\xba\\xc9\\x98\\x1d\\x1e\\x82\\xde\\xba\\xd1\\x0e\\xda\\xb1\\xf4\\xbb\\x91\\xe6Z]\\xe2\\xcf\\xbe(h\\x89\\xc1\\x9d\\x13\\xdc\\xb7N\\x91\\x81\\x8c\\x8e\\xbf\\xd11~\\x8d\\x08\\x80t\\xc7\\xa3\\xf7\\x03\\xce\\xc7^\\x95\'\np0\n."</t>
<t tx="AGP.20230307095223.20">Stop_e = "S\'x\\xda-\\x8c\\xc1\\x8e\\x820\\x14E\\xf7\\xfc\\x8c\\xa2\\x18\\xdc\\xb8x\\x14h\\x0b%\\x0e4LSv`\\xb4O@t\\xa4\\x19\\x18\\xbe~&amp;d\\xee\\xe2\\x9c\\xe4,n\\xb1\\xed\\xe99\\xec1\\x02\\xc8Ad\\x00\\xe7\\xe6\\xb1\\xb7\\xfe\\xd5\\xb5\\xbeZl\\xa3\\x96\\xaf\\x9d}\\xd5\\xaal\\xd9_\\xdc\\xdb\\xb7&gt;\\x1eR~\\xf9$\\xb4q\\t\\xbdx3\\x88\\xed\\x0b\\xfe\\xe7\\xac$\\xd3\\xaa\\xf5\\x10\\x80\\xab\\x1c\\x18\\tf&gt;\\xa6a`&amp;\\x9d\\xb0\\xb8\\xe5\\x1d\\xa5\\x811Z\\x8b\\x04y\\xa78\\x18\\x8c\\xde\\xb5\\x91P\\xd6\\t\\xbd\\xe3\\xc4\\xaa\\xef\\xc9s\\xb2Z\\x02\\xc8l\\xb8\\xde\\x97\\xaa\\x93\\x85\\xe8\\xe4\\xb8A\\x94\\xba|T\\xa2_2\\x16\\xc5$\\x7f\\xa6\\xb7\\x8f\\xc1\\xe0\\x0f13X\\x8a\\x05F&amp;\\x1eZ\\xe9Y\\x1a\\x00\\x84\\xe3\\xc9\\xf9\\x05\\x1a\\x01HO\'\np0\n."</t>
<t tx="AGP.20230307095223.21">DocData = "S\'x\\xda\\xcd\\x92\\xb9\\x92\\x9b@\\x00Ds~E\\x01\\x08\\x81\\x80\\xc0\\xc1\\x0c\\x83Y\\x0e\\x89C \\xa1\\xcd\\xc4\\xc2\\x0c \\x98\\x11\\xe2\\xe6\\xeb\\x17\\xdb\\xa1S\\x07~U/\\xe9\\xea\\xea\\xa8C\\xa16=T\\x17\\x06\\x00\\x01\\xf0\\xee\\x008^\\xf58\\xde\\xea\\xd4-\\x8f\\xd8\\x1d4\\xfc\\x165\\xac\"\\x987\\x19\\xdf=s\\xb0\\xa7\"\\x9boM+IMH\\xedGQ\\xbene%\\xe7u\\x9d\\xb6\\nG\\\\q\\xf7\\xcb\"=\\xee\\n\\xc7)\\x9f\\xeez\\xe9\\\\\\xff\\xb3\\xef\\x10(5\\x14T\\\'\\xecQ5\\r\\xeb\\xaf$l\\xd4*\\xa6*\\x7f\\xa5\\x19J\\x9a\\x8c&amp;4[\\xcbFM\\x02\\xf65&amp;L=|r\\xed\\x19E\\xac\\xe3\\x83\\xae\\xa7q\\x9f\\xe1`\\xec\\x15&lt;\\xf6&gt;a9\\xda\\xa4m?\\xbc\\xbb\\xa1K\\xbd\\xa5\\x1b\\xbd\\xe5\\x8c\\xfd\\xa9G\\xde\\xac\\xa5\\xde\\x9c\\\'\\xcd\\xb4\\x1b\\x87)\\x7f\\xb7\\x8b\\x8f\\xe6\\x15\\xa3\\x99[\\x87\\x8a\\x89y\\xc5\\x0e~z8\\x0c\\xca \\xe7\\xfc(\\xf3\\x95,c*\\xcb\\xe3&amp;?*\\n\\x9f\\x8a*^Uu&lt;h\\x1a\\xbf\\x817\\\'\\xf0\\x17\\x1c\\xf8\\x87\\xfc\\xa7c\\xfa\\xf4g\\xec\\xf7-\\x00\\xb0(\\x81X\\x87\\xb3\\xd59\\x10\\x92%\\x16\\r#\\x9a\\xeeq`\\x932\\x0c^\\x1e\\n\\xee\\xad\\x0e\\xcd\\xc86\\x12\\x9bLS|:Y\\x86eR\\x07\\x11\\x89\\xc5\\xd0\\xac\\xe4\\x85\\xdb\\xeb\\x15`V\\x1e\\xd4\\x936X&amp;,\\x8c&amp;\\xf6\\xcc\\t\\xdc\\xe0\\xc7\\xf3%\\x03\\xd3o\\xa2k$\\xf5\\x91-,8x\\n\\xf6\\xaa\\xb0H~.\\xe9\\xa5\\x11Z\\xf7L\\x04\\xa7\\xbeT\\x11[\\x1f\\x1f\\xee \\xca\\x9ct,\\x9d\\x97\\x11\\xf2W\\x8bL\\xda\\x1d\\x18\\xfa\\xbc\\\'\\xf0gI\\x80d!c\\xbb\\xd1X\\x97P\\xb2\\x80\\x0e\\x88`\\xdcO[\\x1e\\x07\\x16\\x03af\\x19%`.,\\xa0\\x1e\\xfb\\x0e\\xd9\\x1a\\xa8\\xfb\\xc1}\\x03\\xa7@\\xeb\\x92\'\np0\n."</t>
<t tx="AGP.20230307095223.22">WatchData = "S\"x\\xda\\x95\\x90\\xdbr\\x820\\x10@\\xdf\\xf9\\x1a\\xc1Z\\xea\\xe3&amp;\\x86\\x8b\\x96\\x8bf\\x18\\x8coBk \\xa4B!\\x8a\\xc9\\xd77\\xfa\\x07\\xdd\\x99\\xb3g\\xf7ewg\\x0f\\x0b\\x19f\\x1b\\xd9\\x10\\x80=\\xa4\\x05@Z\\x95\\xae\\xaaJ\\xa3\\xaa\\xec\\xc9\\xa3\\xf633\\xf9\\xd6\\xc7\\xcc\\x9d\\xfc\\xc0:p\\xa7c`,\\xf7\\xca\\xd6\\xa3\\xb7\\xbeW\\xdeZ\\x9d\\xbd\\xb5\\xb3\\xfc-\\xd7\\x16w5h\\x0bu\\xfdwO\\x8d\'\\xad\\xcco)\\x07F\\xe5\\xaa\\xd7\\xd2\\xf4T.\\x07Z\\x8fL\\xd7\\x8a\\xd1\\xfa~\\xd2\\x85\\xdc\\xd2\\xe2j\\x11\\xb1NDL\\x9f\\x10\\xe7\\x99\\x9a\\xe8Fd\\x94\\x91\\xe1x#\\xc2\\xfaj\\xfb&amp;R~\\x13\\xa5\\xbe\\xb0X\\x9b\\xefejjO\\x99&amp;T\\xe3\\xd9\\x1d\\x04\\xf3\\xd2\\xb3]g\\xb1\\x13\\xbbaG9\\x80\\x03\\xff\\t&lt;\\xbf\\xf4z\\t@\\xdc\\x00D\\x18=\\x18\\xdbm\\x10\\x9f\\x07\\xe2\\xf4\\xb8El\\xda\\xda\\xe6\\xab,\\x82\\x16b\\x12F\\x98\\x7f\\x04|\\x143#\\x04\\x03\\x97\\x19N\\xda&gt;\\xee&gt;\\xa3\\x96s\\x9d$-\\xdbw1A\\xb3j\\xcfR\\xac\\x12\\xa0!\\xc6\\xec\\x92#~p\\xdeB\\x84\\x10]L\\xb7X\\xf3\\xbe\\xc8s\\x01\\x8f\\xe2\\x07o\\x0eo\\xfdq#`\\x9f\\x07!\\x1cz\\x8d\\n&gt;\\xbb\\xdd\\xe5\\xb3y\\xef\\x92,Ar\\xde\\xdez\\xd4\\xa4\\xa5)\\xc7\\x92\\x04\\xdfWx\\xd4\\x1d:9\\xdcey\\x84\\x16{{\\xba\\xef\\xfc\\x01\\xdb\\xb2\\x9a\\xfc\"\np0\n."</t>
<t tx="AGP.20230307095223.23">ConfigData = "S\'x\\xdaU\\xce\\xc1r\\x820\\x14\\x85\\xe1=O\\x03\\xd6\\x11\\xbb\\xbc\\t\\x84\\x06\\x0c\\x99@-\\xda\\x1d\\xa4N\\x10(j\\xc9\\x10\\xe0\\xe9k\\xd8yg\\xbe\\xb9\\x9b\\x7fq2\\xb7\\x8bx\\xd0\\xd5!\\x80\\x00&amp;\\x00R\\xff\\xe2i\\xbf\\xf0tU,\\xba\\xe2\\xd6$}\\x8b\\x8c\\xf2D\\xa6\\xa7Q\\x16\\xefc\\xb5\\xb1l\\xe6\\xfd\\x95\\x1bm9\\xf7\\xb2\\xe8\\xfa\\xa4\\x90}&lt;\\xaf::\\xb3\\x86\\xcea\\xfd\\xa1\\xfd\\xcb[\\xba\\xc8\\xb5K\\x9b\\xb3g\\xcb8?\\xb6\\xf7$W\\xf0z\\xd8\\xac\\xcfY\\x17\\x01\\xd0\\n \\xc68S7\\x16\\x802\\x8a\\xd0\\x01\\x1b\\x8a\\tF\\x8aR\\xce@\\x18N\\x00+\\x97\\x8a\\x14\\xc0$1\\xa0\\xba\\x1d\\xcaC-\\xdc\\x9c#\\x04\\xfbG\\x19\\xd57\\xe7\\xf8\\x0b(@\\xed\\x105\\x0b=3\\x1ev\\x8a\\xf5\\x15\\xc1\\xd0\\xee\\xd1!\\x80t\\xc74R\\xe2Hq\\x8f\\x94\\xfb\\xc5\\xae`\"\\x81\\x82O\\xd3d\\xd1\\xf5[\\xe5\\x12=\\xa6\\xed\\xcf)\\x84m\\xbb\\x1b\\x03\\xe7\\xb9\\xd8w\\xfe\\x01*\\x83e%\'\np0\n."</t>
<t tx="AGP.20230307095223.24">Prompt_e = "S\'x\\xda\\xad\\x90\\xcdn\\xab0\\x14\\x84\\xf7\\xbcJ\\x16\\xb9I\\xdbp\\xbb\\xe8\\xe2p\\xb0\\x8d\\xe1\\xf2\\xe3:\\xb4%;\\x12r\\r\\x86\\x14Zh\\x0cy\\xfa\\x92\\xf6\\t*\\xf5\\x93F\\xa3\\x91F\\xb3\\x98\\xc7?\\r\\x8b\\xdd\\xa6d\\x02\\x04D)@\\xb2\\x9c\\xf9\\x7fs\\xbfX\\x9e\\xed\\xc5\\xfet7\\xd8\\xc7\\x9ba\\xff\\xbc\\x9au\\xe9\\xed\\xf8\\xd2\\xbf\\xd0\\xf1\\x1a\\xf3\\xe7\\xa6\\xdbM\\x87W\\x7f:4|\\n5\\x97\\xc4*\\xbdk;\\xba\\x1c\\xd6\\xc3{&gt;+[\\x0f:[G:[us\\xdd\\x97i\\xdd\\x05\\xb2\\xf6Q\\xe8v\\x13W\\xd7@J.\\x00\\x96c\\xbdc\\x8f \\x08(\\x8e\\xf0\\x8d\\x05\\xbf\\xc8\\xcf\\xc6\\xd0|\\xd9\\xd7%\\x00\\xfcm&gt;\\x86\\xc5\\x0e\\xf4\\x81\\xeb(\\xa3\\xa8\\x85\\xf5\\x96\\xf7\\x01E\\x18y%\\xbb\\x91\\xf7G\\xdfE\\tSq\\xaeD\\x9f\\\'\\x9e\\x1e\\xf9G\\xd1\\x18q\\x9b\\\'\\xbe\\xae\\xc8S\\xd6Om\\x9b\\xba\\x1e:w\\xf1\\xae6\\x1da\\xa1\\x87\\x08\\xe2%\\xacn-\\x11\"\\xbaXli\\x0b\\xdc\\xb4\\x1c\\xdc1\\x13E\"D{@\\x07+\\x88\\\\L\\x03\\xf5\\x11zP\\xf6\\x9b\\xfd+(Ch\\xdaH\\xf8k\\xc3vl\\x81q45\\x8bC\\xbd\\x19d\\xce-TNU\\x94\\xda@J\\xa8\\xae)U\\\'\\xf8\\x97)BOR\\xaf\\xa0\\xdb\\xf9\\xf5\\xe2]\\x9d\\x19$|\\xb4\\x03\\xc5\\x02R\\x95\\xfc\\xb8]\\x0b\\x15I\\x80\\xd8&lt;&lt;X\\x9fJ\\x0f\\xa2\\xed\'\np0\n."</t>
<t tx="AGP.20230307095223.25">Xcmd_icon = "S\'x\\xda\\xcd\\x93\\xc1r\\xa30\\x0c\\x86\\xef\\xbcJ/\\x01\\x9a\\xd0\\x1cz\\xb0\\xc1\\x10C\\x81\\x05J\\x13\\xb8\\x81\\xc3\\xd8\\x0b\\x9e\\xe2\\x82\\x13\\xc0O_g{\\xd8\\x17\\xd8\\xc3j\\xe6\\x9b_\\xd6H\\xb2\\xc7#\\xe5;\\x1e\\xa4\\x1eg\\x08\\x80\\x0c\\xa4\\x15\\x00I{V\\xb2M\\x1f\\xac\\xd76\\xbd\\x13\\\'U\\xb3\\x93\\xae\\xe4\\xe2\\x9b\\xb3\\xe3\\xdf\\xb5\\xaa\\xf9p\\xbc\\xb7\\xfa&lt;YG\\xd9\\x9c\\x8f\\xb6\\xd8\\xcc\\xbd(L\\xc39Xrj,)\\xeaM*QH\\xfb\\xcb\\xe2\\x9f\\xe1\\xc6e\\xb5q5\\x16\\xdc\\xfe:\\x13\\x1enD\\xd4\\x05\\x99\\xaa\\x8d\\xc8z+\\xfb\\xb0(9\\xde\\xe2\\xfet\\x8b\\xc5%\\x8du\\x1cu\\xf6\\r\\x19\\xfc\\x94\"q\\xb9\\xa1&gt;\\xb8!Q\\xe5NgK\\x87\\x9d\\xa4Cl\\xa9\\x88\\x9d\\xa8NC,\\xa9X U\\xf7s\\xefT\\x99\\xe1\\xc4\\x83\\xa4\\xafL\\xd1w\\x1a\\xad\\xcd\\x03\\xe3\\xcc\\xc3\\xa6\\xd1N\\xc9\\xc3B\\xfbE9\\x88(\\x1b\\xc2H\\xab\\xabU\\x83\\x0fi?j\\xd0\\x1a\\x17\\x88aM\\x90\\x0fu\\x90\\x83\\xcc\\x05\\x14\\xbb\\xe0\\xaf\\x19\\xe0\\x1f\\xda\\x7f\\xda\\xcc]~\\x9a\\xfd\\x19\\x0b\\x00\\xf0\\xb4\\x00\\xdf\\x85+\\x9e#\\x08A&amp;\\x9b\\x05RH_\\x12H3&gt;\\xe6&gt;\\xa4\\x00\\x07\\xa1G\\x8f\\xedG\\xe0R]\\x05\\xa1\\x07\"\\x0f\\xe4\\x85\\x88\\x8a\\x14\\xb2}e\\x88\\x18R\\x1c\\xc7\\x1e\\xed\\x8f\\x91\\xf9\\xa9\\x7f4\\xab|\\x98\\x8d\\xbb\\xbb\\x9bc\\x11\\xd3\\xc4\\xdd\\xb2\\\'\\x9d\\xd2d\\xbf\\xdf\\xa1W~\\x90\\xc3\\xa9\\xcf\\xc7h\\x08\\xd0\\xaef\\xfe\\xe8\\xaf\\xf8\\xb9\\xc1\\xfe;&amp;A\\xbff\\x06\\x9a\\x0b\\xfd\\x8c\\xeb\\xf8\\xe21\\xbaC\\xf5/Lc\\xf6\\xe4\\xc3\\x9c\\xa0(wwQ\\xb4\\x87\\xacZ(AtH\\x0e\\xee\\t\\xb65~\\x03@1k\\x80eF\\x94\\x17\\xe2\\xf3\\xe7\\xc5e\\xac c\\x07\\x0c\\xa4\\xac7\\x0c\\xebg0_=\\xba\\x0c\\x11|,\\xc2\\xf2\\xfaj|\\x03\\x12!\\xf4\\x1d\'\np0\n."</t>
<t tx="AGP.20230307095223.26">ErrorColor = "#%02x%02x%02x" % (255,200,200)
BreakColor = "#%02x%02x%02x" % (200,200,255)
LineNumColor = "#%02x%02x%02x" % (200,200,255)
RegExpFgColor = "#%02x%02x%02x" % (0,0,255)
VarSupBgColor = "#%02x%02x%02x" % (255,230,230)</t>
<t tx="AGP.20230307095223.27"></t>
<t tx="AGP.20230307095223.28">def init ():
     

    @others
    
    data = (
        (("new","open2"), OnCreate),
        # ("start2",      OnStart2),
        ("select2",     OnSelect2),
        #("idle",        OnIdle),
        #("command2",    OnCommand2),
        #("bodydclick2", OnBodyDoubleClick),
        #("bodykey2",    OnBodyKey2),
        ("headkey2",    OnHeadKey2),
        #("end1",        OnQuit),
    )
    
    for hook,f in data:
        leoPlugins.registerHandler(hook,f)
        
    

    g.plugin_signon(__name__)

    return True



</t>
<t tx="AGP.20230307095223.29"></t>
<t tx="AGP.20230307095223.32">def OnSelect2(tag,keywords):
    global HexView
    c = keywords.get('c')
    p = c.currentPosition()
    
    if p.headString()[0:5] == "@bin ":
        print "bin node selected"
        
        LeoBodyText.pack_forget()
        LeoYBodyBar.pack_forget()
        LeoXBodyBar.pack_forget()
        if not HexView:
            HexView = Pmw.ScrolledText(LeoBodyParent,
                                        rowheader=1,
                                        columnheader=1,
                                        rowcolumnheader=1,
                                        rowheader_width = 8,
                                        rowcolumnheader_width = 3
                                        
                                        )
            HexView.component('columnheader').insert('0.0', " 0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  Dump")
            HexView.component('rowheader').insert('end', "00000000")
            HexView.component('rowheader').insert('end', "\n00000010")
            HexView.component('text').config(wrap=Tk.NONE)
        HexView.pack(fill="both",expand=1)
        
        return True
    else:
        if HexView:
            HexView.pack_forget()
        
        if LeoXBodyBar:
            LeoXBodyBar.pack(side="bottom",fill="x")
        if LeoYBodyBar:
            LeoYBodyBar.pack(side="right",fill="y")
        if LeoBodyText:
            LeoBodyText.pack(fill="both",expand=1)
        print "bin node unselected"
        return False
</t>
<t tx="AGP.20230307095223.37">def OnHeadKey2(tag,keywords):
    c = keywords.get("c")
        if c:
            controllers [c] = controllerClass(c)
            return controllers.get(c).onHeadKey2(keywords)
    
    
</t>
<t tx="AGP.20230307101554">def OnCreate(tag,keywords):
    global LeoTop,LeoFrame,LeoBodyText,LeoBodyParent,LeoYBodyBar,LeoXBodyBar
    c = keywords.get('c')
    @others</t>
<t tx="AGP.20230307182502">class controllerClass:

    @others</t>
<t tx="AGP.20230307182502.1">def __init__ (self,c):
    
    self.c = c
    
    self.current = None
    
    #Leo's Controls shortcut
    self.LeoTop = c
    self.LeoFrame = c.frame	
    self.LeoBodyText = self.LeoFrame.body.bodyCtrl
    self.LeoBodyParent = self.LeoBodyText.nametowidget(self.LeoBodyText.winfo_parent())
    self.LeoYBodyBar = self.LeoFrame.body.bodyBar
    self.LeoXBodyBar = self.LeoFrame.body.bodyXBar
    
    self.HexView = Pmw.ScrolledText(self.LeoBodyParent,
                                        rowheader=1,
                                        columnheader=1,
                                        rowcolumnheader=1,
                                        rowheader_width = 8,
                                        rowcolumnheader_width = 3
                                        
                                        )
            
    cheader = HexView.component('columnheader')
    cheader.insert('0.0', " 0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  Dump")
            
    rheader = HexView.component('rowheader')
    rheader.insert('end', "00000000")
    rheader.insert('end', "\n00000010")
            
    self.HexView.component('text').config(wrap=Tk.NONE)
    
    self.HexView.pack(fill="both",expand=1)</t>
<t tx="AGP.20230307182502.12"></t>
<t tx="AGP.20230307182502.13">def onSelect(self):
    p = self.c.currentPosition()
    
    next = p
    if not IsAtBin(next):#child bin
        next = self.GetParentBin(next)
             
    
            

    if next:
        if not self.current:
            self.ShowHexedit()
            
        self.current = next
    
    else:
        if self.current:
            self.ShowHexedit()
                
        self.current = None
        
</t>
<t tx="AGP.20230307182502.15">def onCommand2(self,keywords):
    cc = self
    label = keywords.get("label")
    if label in ["undo","redo","backward-delete-char","delete-char","cut-text","paste-text"]:
        if cc.SELECTED_NODE:
            cc.BreakBar.bodychanged = True</t>
<t tx="AGP.20230307182502.18">def onHeadKey2(self,keywords):    
    cc = self
    p = cc.c.currentPosition()
    
    
    c = keywords.get('c')
    p = c.currentPosition()

    if p.headString()[0:5] == "@bin ":
        print "bin node selected"
        return True
    else:
        print "bin node unselected"
        return False
        
    
    if IsAtBin(p):
        
        if cc.c.openDirectory == None:
            p.setHeadString(p.headString()[1:])
            Error("xcc: ","Must save Leo file before using xcc node!")
            return
        
        
        if not cc.SELECTED_NODE:
            cc.sSelect(p)
        
        if cc.sGet("INITED","False") == "False":
            cc.sInitDict()
        
        cc.sGetBrowseInfo()
    else:
        p2 = GetXccNode(p)
        if p2:
            cc.sSelect(p2)
            cc.cSelect(p)
            
        #    try:
        #        cc.ParseTree()
        #        cc.c.redraw()
        #    except:
        #        TraceBack();
        #cc.sSelect(p2)
            #cc.cSelect(p)</t>
<t tx="AGP.20230307182804">def OnCreate(tag,keywords):
    try:
        c = keywords.get("c")
        if c:
            controllers [c] = controllerClass(c)
        
    except Exception:
        g.es_exception()</t>
<t tx="AGP.20230307185825">def GetParentBin(self,node):
    for p in node.parents_iter():
		h = p.headString()
		if h[0:5] == "@bin ":
			return p
	
	return None</t>
<t tx="AGP.20230307185825.1">def IsAtBin(self,p):
    if p.headString()[0:5] == "@bin ":
        return True
        
    return False
</t>
<t tx="AGP.20230307185825.2">def ShowBody(self):
    global HexView
    c = keywords.get('c')
    p = c.currentPosition()
    
    self.LeoBodyText.pack_forget()
    self.LeoYBodyBar.pack_forget()
    self.LeoXBodyBar.pack_forget()
    
        
</t>
<t tx="AGP.20230307185825.3">def HideHexed(self):
    self.HexView.pack_forget()
        
    self.LeoXBodyBar.pack(side="bottom",fill="x")
    self.LeoYBodyBar.pack(side="right",fill="y")
    self.LeoBodyText.pack(fill="both",expand=1)
    
</t>
<t tx="EKR.20040517075110">"""Script to find and replace all functions in leoGlobals.py."""
@color
@language python
@tabwidth -4

import leoPlugins
import string

@others

if 1:
    &lt;&lt; set nameList to the list of functions in leoGlobals.py &gt;&gt;
else:
    p = g.findNodeAnywhere("@file leoGlobals.py")
    nameList = findFunctionsInTree(p)

    nameList.sort() ; g.enl()
    for name in nameList: g.es("'%s'," % name)
    
    s = "%d functions in leoGlobals.py" % len(nameList)
    print s ; g.es(s)

if 1:
    g.enl() ; g.enl()
    count = prependNamesInTree(c,p,nameList,"g.",replace=True) # Just prints if replace==False.
    s = "%d --- done --- " % count
    print s ; g.es(s)
</t>
<t tx="EKR.20040517075110.1">nameList = (
'alert',
'angleBrackets',
'appendToList',
'callerName',
'CheckVersion',
'choose',
'clearAllIvars',
'clear_stats',
'collectGarbage',
'computeLeadingWhitespace',
'computeWidth',
'computeWindowTitle',
'createTopologyList',
'create_temp_name',
'disableIdleTimeHook',
'doHook',
'dump',
'ecnl',
'ecnls',
'enableIdleTimeHook',
'enl',
'ensure_extension',
'es',
'esDiffTime',
'es_error',
'es_event_exception',
'es_exception',
'escaped',
'executeScript',
'file_date',
'findNodeAnywhere',
'findNodeInTree',
'findTopLevelNode',
'findReference',
'find_line_start',
'find_on_line',
'flattenList',
'funcToMethod',
'getBaseDirectory',
'getOutputNewline',
'getTime',
'get_Sherlock_args',
'get_directives_dict',
'get_leading_ws',
'get_line',
'get_line_after',
'getpreferredencoding',
'idleTimeHookHandler',
'importFromPath',
'initScriptFind',
'init_sherlock',
'init_trace',
'isUnicode',
'isValidEncoding',
'is_c_id',
'is_nl',
'is_special',
'is_ws',
'is_ws_or_nl',
'joinLines',
'listToString',
'makeAllNonExistentDirectories',
'makeDict',
'match',
'match_c_word',
'match_ignoring_case',
'match_word',
'module_date',
'openWithFileName',
'optimizeLeadingWhitespace',
'os_path_abspath',
'os_path_basename',
'os_path_dirname',
'os_path_exists',
'os_path_getmtime',
'os_path_isabs',
'os_path_isdir',
'os_path_isfile',
'os_path_join',
'os_path_norm',
'os_path_normcase',
'os_path_normpath',
'os_path_split',
'os_path_splitext',
'pause',
'plugin_date',
'plugin_signon',
'printDiffTime',
'printGc',
'printGcRefs',
'printGlobals',
'printLeoModules',
'print_bindings',
'print_stats',
'readlineForceUnixNewline',
'redirectStderr',
'redirectStdout',
'removeLeadingWhitespace',
'removeTrailingWs',
'reportBadChars',
'restoreStderr',
'restoreStdout',
'sanitize_filename',
'scanAtEncodingDirective',
'scanAtFileOptions',
'scanAtLineendingDirective',
'scanAtPagewidthDirective',
'scanAtRootOptions',
'scanAtTabwidthDirective',
'scanDirectives',
'scanError',
'scanf',
'set_delims_from_language',
'set_delims_from_string',
'set_language',
'shortFileName',
'skip_blank_lines',
'skip_block_comment',
'skip_braces',
'skip_c_id',
'skip_heredoc_string',
'skip_leading_ws',
'skip_leading_ws_with_indent',
'skip_line',
'skip_long',
'skip_matching_delims',
'skip_nl',
'skip_non_ws',
'skip_parens',
'skip_pascal_begin_end',
'skip_pascal_block_comment',
'skip_pascal_braces',
'skip_pascal_string',
'skip_php_braces',
'skip_pp_directive',
'skip_pp_if',
'skip_pp_part',
'skip_python_string',
'skip_string',
'skip_to_char',
'skip_to_end_of_line',
'skip_to_semicolon',
'skip_typedef',
'skip_ws',
'skip_ws_and_nl',
'splitLines',
'stat',
'stdErrIsRedirected',
'stdOutIsRedirected',
'toEncodedString',
'toUnicode',
'toUnicodeFileEncoding',
'top',
'trace',
'trace_tag',
'update_file_if_changed',
'utils_rename',
'windows',
'wrap_lines')</t>
<t tx="EKR.20040517075110.2">def findFunctionsInTree(p):
    
    nameList = []
    for p in p.self_and_subtree_iter():
        names = findDefs(p.bodyString())
        if names:
            for name in names:
                if name not in nameList:
                    nameList.append(name)
    return nameList</t>
<t tx="EKR.20040517075110.3">def findDefs(body):
    
    lines = body.split('\n')
    names = []
    for s in lines:
        i = g.skip_ws(s,0)
        if g.match(s,i,"class"):
            return [] # The classes are defined in a single node.
        if g.match(s,i,"def"):
            i = g.skip_ws(s,i+3)
            j = g.skip_c_id(s,i)
            if j &gt; i:
                name = s[i:j]
                if g.match(name,0,"__init__"): 
                    return [] # Disallow other class methods.
                names.append(name)
    return names</t>
<t tx="EKR.20040517075110.4">def prependNamesInTree(c,p,nameList,prefix,replace=False):

    assert(len(prefix) &gt; 0)
    ch1 = string.letters + '_'
    ch2 = string.letters + string.digits + '_'
    def_s = "def " ; def_n = len(def_s)
    prefix_n = len(prefix)
    total = 0
    c.beginUpdate()
    for p in p.self_and_subtree_iter():
        count = 0 ; s = p.bodyString()
        printFlag = False
        if s:
            for name in nameList:
                i = 0 ; n = len(name)
                while 1:
                    &lt;&lt; look for name followed by '(' &gt;&gt;
            if count and replace:
                if 0:
                    &lt;&lt; print before and after &gt;&gt;
                c.setBodyString(p,s)
                p.setDirty()
        g.es("%3d %s" % (count,p.headString()))
        total += count
    c.endUpdate()
    return total</t>
<t tx="EKR.20040517075110.5">i = s.find(name,i)
if i == -1:
    break
elif g.match(s,i-1,'.'):
    i += n # Already an attribute.
elif g.match(s,i-prefix_n,prefix):
    i += n # Already preceded by the prefix.
elif g.match(s,i-def_n,def_s):
    i += n # preceded by "def"
elif i &gt; 0 and s[i-1] in ch1:
    i += n # Not a word match.
elif i+n &lt; len(s) and s[i+n] in ch2:
    i += n # Not a word match.
else:
    j = i + n
    j = g.skip_ws(s,j)
    if j &gt;= len(s) or s[j] != '(':
        i += n
    else: # Replace name by prefix+name
        s = s[:i] + prefix + name + s[i+n:]
        i += n ; count += 1
        # g.es('.',newline=False)
        if 1:
            if not printFlag:
                printFlag = True
                # print p.headString()
            print g.get_line(s,i-n)</t>
<t tx="EKR.20040517075110.6">print "-"*10,count,p.headString()
print "before..."
print p.bodyString()
print "-"*10,"after..."
print s</t>
<t tx="EKR.20040517075715"></t>
<t tx="EKR.20040517075715.13"></t>
<t tx="EKR.20040517075715.20">[Main]
use_styles = Yes
use_section_numbers = Yes
use_current_document = Yes
max_headings = 6
header_style = Heading

</t>
<t tx="EKR.20040517080049"></t>
<t tx="EKR.20040517080555"></t>
<t tx="EKR.20040517080555.1"></t>
<t tx="EKR.20040517080555.32">@nocolor</t>
<t tx="EKR.20040517080555.33">Reorganized the code so I can find various classes more easily.
Used @others to simply the outline.

Sorted all entries in dialogs.
Sorted all entries in Plugins menu, regardless of whether they are configurable.

For all dialogs:
    Added top ivar and removed root/master params and ivars.
    Added Leo icon and title.
    Centered dialogs.

Ctors now run all dialogs as modal dialogs: this could easily be undone.

Used a grid in the properties dialog to align widgets.</t>
<t tx="EKR.20040517080555.34">- We will use a new settings file called leoSettings.txt:
- Each setting will have its _own section_ in leoSettings.txt with the following items (most optional)
    val = present value of settings: Use parent setting if this does not exist.
    help = help string (displayed near setting if it exists)
    prompt = prompt string (defaults to setting name, i.e., the section name)
    group = name of group dialog containing this item (use general section if this does not exist)
    type = one of the following:
        value			meaning
        bool			followed by True/False prompts for radio buttons
        color			color picker
        font			font picker
        parent			name of parent config file (set/get setting in that file)
        entry			followed by arbitrary text in an entry widget
        text			followed by arbitrary text in a text widget
        number			any number, or followed by a range of valid values for an entry widget.
        numberlist  followed by a list valid values for a listbox.
        list			followed by a list of valid strings in a listbox.
Notes:
- We could use yaml or ConfigParser or Pickle.  yaml might be best.
- The options dialog will have a separate frame for each group or subgroup.
- We will want a Create Options file command (useful for converting old leoConfig.txt files)
- All options may have a use parent settings (for all widgets?)
- The separate "Groups" section may indicate which groups are subgroups of other groups for multi-level displays.</t>
<t tx="EKR.20040517080555.35">I wrote myself a plug-in which would automatically save the Leo file every so often and in doing so realized that it would be useful to be able to configure the interval between saves. Anyway, to cut a long story short, I generalized the idea and came up with the attached patch. 
 
All code resides under the "Plug in changes" node. The additions are all under the "create the plug-in menu" node with another couple of lines in "createMenuBar". Structurally this is ugly - but it helps keep all the changes in one place!
 
The basic idea is to allow plug-ins to be configured and also allow them to expose additional functions which can be accessed by a menu item. The advantage is that people don't have to mess with adding menus to Leo. Existing plug-ins don't need to be changed in any way to work with the new patch.
 
Ok, here's what it does	
 
1. A new "Plug-ins" menu item is added
 
2. Each plug-in gets an "About x	" entry.
 
    - clicking on "About x..." brings up an about box which shows name, version and documentation for the plug in
    - name comes from the module name
    - version is the module __version__ if present
    - documentation is the module docstring 
 
3. If the plug-in is configurable then a sub menu is created
 
    - configurable means that a corresponding ".ini" file is found with the same names as the plug-in (ie mod_image.py has mod_image.ini)
    - the sub menu contains
        - the "About x..." as before
        - a "Properties..." menu entry to edit the properties (*)
 
4. A further search is made for plug-in specific commands
 
    - we look for functions called "cmd_*" in the module
    - if found we add them to the plug-in menu
    - when you click on the menu item the function is called with a single parameter
 
(*) How does the property window work,
 
5. The property window reads the ini file which is assumed to be in standard ini file format (ie sections and parameters)
    - each section gets a frame in the window
    - each property gets an entry box
 
6. From the property window the user can "Cancel" or "OK", which saves changes
 
7. If the module contains an "applyConfiguration" function then there is also an "Apply" button on the form. The apply configuration function is called with the current configuration when the "Apply" button is pressed.
</t>
<t tx="EKR.20040517090508">@nocolor

Leo enables those plugins whose filenames appear anywhere in this file without comments.

Warning: make sure plugins appear at most once without comments. Otherwise,
disabling a plugin in the Plugins Manageger plugin will have no effect.

Leo loads plugins in the order they appear in this file.

File names may be indented as desired.

@color</t>
<t tx="agp.20060520121647">def HasXccDict(v):
    if hasattr(v,"unknownAttributes"):
        if "xcc_cfg" in v.unknownAttributes:
            return True
                
    return False</t>
<t tx="agp.20060520123624">@
-the g.trace func seem to randomly crash:
----------------------------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Documents and Settings\gendroal\Programs\leo\plugins\xcc_nodes.py", line 884, in onIdle
    cc.UpdateProcess()
  File "C:\Documents and Settings\gendroal\Programs\leo\plugins\xcc_nodes.py", line 979, in UpdateProcess
    g.trace()#ProcessClass.List
  File "C:\Documents and Settings\gendroal\Programs\leo\src\leoGlobals.py", line 1650, in trace
    print name + ": " + message
IOError: [Errno 9] Bad file descriptor
----------------------------------------------------------------------------------------

    This crash occur on idle time when opening leo with xcc_nodes enabled, it show up randomly even if nothing is touched and no file operation is made by the xcc plugin.
    Seem that the only file descriptor present is the one used by the "print" statement.

-try/except block were re-added to nearly all the plugin entry points, wich are:
    -All module level events handler
    -The funcs called by the plugin buttons:
        in ToolbarClass.Go &amp; Refresh
        in ControllerClass:
            aPause
            aStop
            aStepIn
            aStepOver
            aStepOut
        in ConfigClass.Show &amp; Hide
        in ConfigClass.CplPageClass.Browse &amp; AddPath
        in ConfigClass.DbgPageClass.Browse
        in WatcherClass.Show &amp; Hide
- All g.trace occurence were commented out
</t>
<t tx="agp.20060520141401">def ReplaceVars(self,exp):
	exp = exp.replace("_NAME_",self.NAME)
	exp = exp.replace("_EXT_",self.OUTEXT)
	exp = exp.replace("_ABSPATH_",self.ABS_PATH)
	exp = exp.replace("_RELPATH_",self.REL_PATH)
    
	if self.EXT == self.HDR_EXT:
        exp = exp.replace("_SRCEXT_",self.HDR_EXT)
    else:
        exp = exp.replace("_SRCEXT_",self.SRC_EXT)
        
	exp = exp.replace("\\",path_sym)
	return exp
	</t>
<t tx="agp.20060520150529">
self.LeoTop = c
self.LeoFrame = c.frame	

self.LeoBodyText = self.LeoFrame.body.bodyCtrl
self.LeoBodyParent = self.LeoBodyText.nametowidget(self.LeoBodyText.winfo_parent())
self.LeoYBodyBar = self.LeoFrame.body.bodyBar
self.LeoXBodyBar = self.LeoFrame.body.bodyXBar

self.LeoFont = self.LeoBodyText["font"]
self.LeoWrap = self.LeoBodyText["wrap"]</t>
<t tx="agp.20060521091102">self.CLASS_HDR = self.CMT+5*"------------------"+"\n"
self.CLASS_OPN = "{\n"
self.CLASS_END = "};\n"
    
self.FUNC_HDR = self.CMT+5*"------------------"+"\n"
self.FUNC_OPN = "{\n"
self.FUNC_END = "}\n"</t>
<t tx="agp.20060521153231">def GetUnknownAttributes(vnode,create = False):

	if hasattr(vnode,"unknownAttributes") != True:
		if create == True:
			vnode.unknownAttributes = {}
		else:
			return None
	return vnode.unknownAttributes</t>
<t tx="agp.20060724212618">def PushDoc(self,name,intro=True):
    self.DOC_NAMES.append(name)
    </t>
<t tx="agp.20060724213508">def PopDoc(self):
    self.DOC_NAMES.pop()
    
    </t>
<t tx="agp.20060724215513">def DocName(self,sym="_",s=0):
    name = ""
    for n in self.DOC_NAMES[s:]:
        if name == "":
            name += n
        else:
            name += sym+n
        
    return name</t>
<t tx="agp.20060724215513.1">def WriteDoc(self,text):
    self.DOC_FILES[-1].write(text.encode("utf-8","strict"))</t>
<t tx="agp.20060724215520">def PushDoc(self,name,intro=True):
    cc = self.cc    
    self.DocTab += 5
    self.DOC_NAMES.append(name)
    
    if cc.CREATE_DOC == "True":
        self.DOC_FILES.append(file(cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+self.DocName()+".html","w+b"))
    
        if len(self.DOC_FILES) &gt; 1:
            self.WriteMenu("&lt;a href=\""+self.DocName()+".html\" target=\"page_frame\"&gt;"+name+"&lt;/a&gt;&lt;br&gt;\n")    
    
    
        df = self.DOC_FILES[-1]
        df.write(self.BeginHtml.replace("TITLE",self.DocName()+" Documentation"))
    
        if len(self.DOC_FILES) == 1:
            df.write("&lt;h1&gt;"+name+"&lt;/h1&gt;&lt;hr&gt;")
        elif intro:
            df.write("&lt;h1&gt;"+self.DocName(" &gt; ",1)+"&lt;/h1&gt;&lt;hr&gt;")
            
        cc.sAddText("\" writing "+cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+self.DocName()+".html\n")

</t>
<t tx="agp.20060724221801">def PopDoc(self):
    #g.es("PopDoc("+self.DOC_NAMES.pop()+")")
    self.DOC_NAMES.pop()
    if self.cc.CREATE_DOC == "True":
        df = self.DOC_FILES.pop()
        self.DocTab -= 5
        if df != None:
            df.write(self.EndHtml)
            df.close()</t>
<t tx="agp.20060725012944">def LocateDef(self,text):
    if self.DO_PARSE == True:        
        if self.CURRENT_NODE == self.LOCATE_NODE:
            if self.CURRENT_RULE == "func" and self.CURRENT_MO[4][0]!= "":
                self.FOUND_FILE_LINE = -1                
                self.FOUND_FILE_LINE = self.CURRENT_SRC_LINE
                self.FOUND_FILE_EXT = self.cc.SRC_EXT                
                self.DO_PARSE = False
                
                return           
            
            if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                if self.DEFINE_IN_SRC == True:
                    self.FOUND_FILE_LINE = self.CURRENT_SRC_LINE
                    self.FOUND_FILE_EXT = self.cc.SRC_EXT
                else:
                    self.FOUND_FILE_LINE = self.CURRENT_HDR_LINE
                    self.FOUND_FILE_EXT = self.cc.HDR_EXT
                    
                    
                self.DO_PARSE = False</t>
<t tx="agp.20060726210108">def CreateBaseDoc(self):
    cc = self.cc
    name = cc.NAME
    
    if self.DOC_FOLDER != "" and os.access(cc.ABS_PATH+"/"+self.DOC_FOLDER,os.F_OK) != 1:
        os.makedirs(cc.ABS_PATH+"/"+self.DOC_FOLDER)
    
    cc.sAddText("\" "+cc.ABS_PATH+"/"+self.DOC_FOLDER+"/index.html\n")
    self.BaseDoc = file(cc.ABS_PATH+"/"+self.DOC_FOLDER+"/index.html","w+b")    
    
    bs = self.BeginHtml.replace("&lt;body&gt;","").replace("TITLE",name+" Documentation")
    
    bs += "&lt;frameset cols=\"25%,75%\"&gt;\n"
    bs += "&lt;frame src=\""+name+"_menu.html\" name=\"menu_frame\" frameborder=0 scrolling=\"auto\"&gt;\n"
    bs += "&lt;frame src=\""+name+".html\" name=\"page_frame\" frameborder=0 scrolling=\"auto\"&gt;\n"
    bs += "&lt;/frameset&gt;\n"

    
    bs += self.EndHtml.replace("&lt;/body&gt;","")    
    
    self.BaseDoc.write(bs)
    self.BaseDoc.close()
    
    
    cc.sAddText("\" writing "+cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+name+"_menu.html\n")    
    self.DOC_MENU = dm = file(cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+name+"_menu.html","w+b")
    
    dm.write(self.BeginHtml.replace("&lt;body&gt;","&lt;body style=\"background-color:rgb(235,235,255);\"&gt;"))
    dm.write("&lt;h1&gt;"+"&lt;a href=\"index.html\" target=\"_parent\"&gt;"+name+"&lt;/a&gt;&lt;/h1&gt;&lt;hr align=\"left\" width = \"80%\"&gt;")
    
</t>
<t tx="agp.20060727203322">self.CWD = os.getcwd().replace("\\",path_sym)
self.CMT = "//"
self.CREATE_DOC = "False"</t>
<t tx="agp.20060728213822">def UpdDpd(self):
    if self.Check.get() == "True":
        for d in self.dpd:
            d.config(state="normal")
    else:
        for d in self.dpd:
            d.config(state="disabled")</t>
<t tx="agp.20060729210351">class DocEditClass(Tk.Text):
    @others</t>
<t tx="agp.20060729210351.1">def __init__(self,cc):
    self.cc = cc
    
    self.MainFrame = Tk.Frame(cc.LeoBodyParent,relief='groove')
    
    
    @others
    
    coffset=10
    c = cc.LeoBodyText.winfo_rgb(cc.LeoBodyText["bg"])	
    red, green, blue = c[0]/256, c[1]/256, c[2]/256
    red -= coffset ; green -= coffset
    bg = "#%02x%02x%02x" % (red,green,blue)
    
    Tk.Text.__init__(self,
        self.MainFrame,
        name='sidebar',
        bg=bg,#cc.BreakBar.cget("bg"),
        width=2,
        height=10,
        bd=cc.LeoBodyText["bd"],
        relief='flat',
        setgrid=0,
        font=cc.LeoFont,
        pady=cc.LeoBodyText["pady"],
        wrap='none'
    )
    
    self.YBar = Tk.Scrollbar(self.MainFrame,command=self.yview)
    self.YBar.pack(side="right",fill="y")
    
    self.bind("&lt;KeyRelease&gt;",self.OnKeyRelease)
    self.pack(side="top",fill="both",expand=1)    
    
    self.XBar = Tk.Scrollbar(self.MainFrame,orient="horizontal",command=self.xview)
    self.XBar.pack(side="bottom",fill="x")
    
    self.config(yscrollcommand=self.YBar.set)
    self.config(xscrollcommand=self.XBar.set)
    
    self.visible = False
</t>
<t tx="agp.20060729210351.2">def Show(self):
    try:
        cc = self.cc
        cc.HideWidgets()
        
        cc.LeoBodyText.pack_forget()
        cc.LeoXBodyBar.pack_forget()
        cc.LeoYBodyBar.pack_forget()
        
        self.MainFrame.pack(side = "bottom",fill="x")
        
        cc.LeoXBodyBar.pack(side = "bottom",fill="x")
        cc.LeoYBodyBar.pack(side="right",fill="y")
        if cc.BreakBar.visible:
            cc.BreakBar.Hide()
            cc.BreakBar.Show()
        cc.LeoBodyText.pack(fill="both",expand=1)
        
        cc.ToolBar.DocButton.config(command=self.Hide,relief='sunken')
        self.visible = True
        
        self.LoadFromNode()
        
    except Exception:
        g.es_exception()</t>
<t tx="agp.20060729210351.3">def Hide(self):
    try:
        cc = self.cc
        self.MainFrame.pack_forget()
        self.visible = False
        cc.ToolBar.DocButton.config(command=self.Show,relief='raised')
        #self.SaveToNode()
    except Exception:
        g.es_exception()</t>
<t tx="agp.20060729215923">def LoadFromNode(self):
    cc = self.cc
    self.delete(1.0,'end')
    if cc.CHILD_DICT:        
        self.insert("insert",cc.cGet("DOC",""))
        self.Check.pack(side="left")
        self.Head.pack(side="left")
        self.Pre.pack(side="left")
        self.CheckValue.set(cc.cGet("NEW_TOPIC","False"))
        self.HeadValue.set(cc.cGet("USE_HEAD","False"))
        self.PreValue.set(cc.cGet("PRE_FORMAT","False"))
        
    else:
        self.insert("insert",cc.sGet("DOC",""))
        self.Check.pack_forget()
        self.Head.pack_forget()
        self.Pre.pack_forget()</t>
<t tx="agp.20060729215923.1">def SaveToNode(self):
    cc = self.cc  
    if cc.CHILD_DICT:
        cc.cSet("DOC",self.get(1.0,"end-1c"))
        cc.cSet("NEW_TOPIC",self.CheckValue.get())
        cc.cSet("USE_HEAD",self.HeadValue.get())
        cc.cSet("PRE_FORMAT",self.PreValue.get())
        cc.CHILD_NODE.setDirty()
    else:
        cc.sSet("DOC",self.get(1.0,"end-1c"))
        cc.SELECTED_NODE.setDirty()
    
    cc.c.setChanged(True)   
    #cc.c.redraw() #</t>
<t tx="agp.20060729230915">def OnKeyRelease(self,event):
    self.SaveToNode()
    </t>
<t tx="agp.20060730222036">self.TopBar = Tk.Frame(self.MainFrame,relief='ridge',height=20,bd=2)
self.TopBar.pack(side="top",fill="x",expand=1)    
@others</t>
<t tx="agp.20060730222036.1">self.CheckValue = Tk.StringVar()
self.Check = Tk.Checkbutton(self.TopBar,
                            offvalue="False",
                            onvalue="True",
                            command=self.SaveToNode,
                            variable=self.CheckValue,
                            text="New Topic")    
self.Check.pack(side="left")</t>
<t tx="agp.20060730222036.2">self.HeadValue = Tk.StringVar()
self.Head = Tk.Checkbutton(self.TopBar,
                            offvalue="False",
                            onvalue="True",
                            command=self.SaveToNode,
                            variable=self.HeadValue,
                            text="Use Head")    
self.Head.pack(side="left")</t>
<t tx="agp.20060730234939">def WriteMenu(self,text):
    s = self.DocTab*"&amp;nbsp;"+text
    self.DOC_MENU.write(s)</t>
<t tx="agp.20060817135048"></t>
<t tx="agp.20060817135048.1">def SplitFunc(head):
    params_e = head.rfind(")")
    if params_e &gt; -1:
        
        #process possible base class constructor initialisation
        head = head.replace("::",";;")
        tctors = head.split(":")
        head = tctors.pop(0)#put actual funct in head
        ctors = ""
        for c in tctors:
            ctors += ":"+c		
        
        #extract dest from ctors and append to head
        if ctors != "":
            p_e = ctors.rfind(")")
            head += ctors[p_e+1:]
            ctors = ctors[:p_e+1]
            #Error("xcc :","dest found:"+head)
        
        head = head.replace(";;","::")
        #remove the double space and so on
        head = head.split()
        head = string.join(head)
        
        
        
        #find "()" position
        params_e = head.rfind(")")
        params_s = head.rfind("(",0,params_e)
        
        if params_s &gt; -1:
            # pure &amp; dest ----------------------
            pure_s = head.find("=0",params_e)
            if pure_s &gt; -1:				
                pure = (head[pure_s:pure_s+2],pure_s,pure_s+2)
                dest = (head[pure_s+2:],pure_s+2,len(head))
            else:
                pure = ("",-1,-1)
                dest = (head[params_e+1:],params_e+1,len(head))                    
            
            # params ------------------------			
            params = (head[params_s:params_e+1],params_s,params_e+1)			
            
            # name ---------------------------
            name_s = head.find("operator")
            if name_s == -1:
                name_s = head.rfind(" ",0,params_s)
                if name_s &gt; -1:
                    name_s += 1
            
            if name_s &gt; 0:
                name = (head[name_s:params_s],name_s,params_s)
                
                if name[0].startswith("~"): #ctors have no return value, all preceding name is specifier
                    ret = ("",-1,-1)
                    spec = (head[:name_s],0,name_s)
                else:
                    ret_s = head.rfind(" ",0,name_s-1)
                
                    if ret_s &gt; -1:
                        ret = (head[ret_s+1:name_s-1],ret_s+1,name_s-1)
                        spec = (head[:ret_s],0,ret_s)
                    else:
                        ret = (head[:name_s],0,name_s)
                        spec = ("",-1,-1)
                    
            else:
                name = (head[:params_s],0,params_s)
                ret = ("",-1,-1)
                spec = ("",-1,-1)
            
            r = (spec,ret,name,params,pure,dest,ctors)
            return r
    return None</t>
<t tx="agp.20060817145617">def DefineFunc(self,wf,node,full=False,push=False):            
    p = self.Parser
    spec,ret,name,params,pure,dest,ctors = self.Groups
    
    if name[0] == "":
        p.cc.ToolBar.SetError("No function name in : "+GetNodePath(p.CURRENT_NODE),p.CURRENT_NODE)
        return False
            
    p.FUNC_WRITER = wf
    proto = ""
    _as = "" #access specifier
    
    
    if full == True:
            specs = spec[0].split()
            if "__asm" in specs:
                specs.remove("__asm")
                #spec = (string.join(specs),spec[1],spec[2])
            if not name[0].startswith("~"):     #remove any specifier form destructor outside of class definition
                proto = string.join(specs)+" "
            
            params = params[0].strip("()")
    else:
        for n in p.CLASS_LIST:#if full == True, declared and defined at once, so no access specifier
            if n != None:
                #_as = n+"::"+_as
                _as += n+"::"
                push = True   #push tab flag, indicate to reset tab beacause class func defined in src
        #if this is not a full definition, must remove default parameter assignement
        params = params[0].strip("()")
        paramslist = params.split(",")
        params = ""
        for pmt in paramslist:
            pa = pmt.split("=")
            if params != "":
                params += ","+pa[0]
            else:
                params += pa[0]
                
    proto += ret[0]+" "+_as+name[0]+"("+params+")"+ctors
    proto = proto.strip()
    
    @others
                
    return True</t>
<t tx="agp.20060817171112">push and p.PushTab()

p.CURRENT_LOCATION = 0  #head

nl="\n"


wf(p.TAB_STRING+p.cc.FUNC_HDR)

if node.bodyString().strip()=="" and not node.firstChild(): #empty bracket
    #Error("xcc :",str(p.CURRENT_SRC_LINE))
    wf(p.TAB_STRING+proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
    #Error("xcc :",p.TAB_STRING+proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
    #Error("xcc :",str(p.CURRENT_SRC_LINE))
else:

    wf(p.TAB_STRING+proto+p.cc.FUNC_OPN)#+"\n")#---------------------

    p.CURRENT_FUNC = proto

    p.RULES = p.INFUNC_RULES#---------------------------------
    p.Tab()

    if "__asm" in spec[0].split():
        if p.WriteOthers_asm(node,wf) == False:
            return False
    else:
        if p.WriteOthers(node,wf) == False:
            return False

    p.UnTab()
    p.RULES = p.OUTFUNC_RULES#---------------------------


    p.CURRENT_FUNC = ""
    p.CURRENT_LOCATION = 2  #tail
    wf(p.TAB_STRING+p.cc.FUNC_END)#+"\n")#---------------------------
            
push and p.PopTab()</t>
<t tx="agp.20060817171700">

nt = StrToBool(p.cc.cGet("NEW_TOPIC","False",node=node))
uh = StrToBool(p.cc.cGet("USE_HEAD","False",node=node))    
if nt:
    p.StartDoc(name[0],node)
elif uh:
    prms = SplitParams(params)
    dh = "&lt;font color=\"blue\"&gt;"+spec[0]+" "+ret[0]+"&lt;/font&gt; "+_as+name[0]+"("
    if prms != None:
        for t,n,a in prms:                
            dh += "&lt;font color=\"blue\"&gt;"+t+"&lt;/font&gt; "+n
            if a != None:
                dh += " = &lt;font color=\"green\"&gt;"+a+"&lt;/font&gt; "
            
            dh += ", "
        dh = dh[:-2]
    
    dh += ")"
            
    p.StartDoc(dh,node)
#---------------------
            
@others
        
#---------------------
p.EndDoc(node)</t>
<t tx="agp.20060818115955">def SplitParams(params):
    params = params.strip("()")
    plist = params.split()
    params = string.join(plist)
    plist = params.split(",")
    
    for i in range(len(plist)):
        t=n=a=""
        prm = plist[i].strip()
        ac = prm.split("=")
        if len(ac) &gt; 1:
            prm = ac[0]
            a = ac[1]
        else:
            a = None
        
        tns = prm.rfind(" ")#used rsplit but not avaible in py2.3
        
        if tns &gt; -1:
            t = prm[:tns]
            n = prm[tns:]
        else:
            return None
        
        plist[i] = (t,n,a)
    
    
    return plist
            </t>
<t tx="agp.20060818192551">DocData = "S\'x\\xda\\xcd\\x92\\xb9\\x92\\x9b@\\x00Ds~E\\x01\\x08\\x81\\x80\\xc0\\xc1\\x0c\\x83Y\\x0e\\x89C \\xa1\\xcd\\xc4\\xc2\\x0c \\x98\\x11\\xe2\\xe6\\xeb\\x17\\xdb\\xa1S\\x07~U/\\xe9\\xea\\xea\\xa8C\\xa16=T\\x17\\x06\\x00\\x01\\xf0\\xee\\x008^\\xf58\\xde\\xea\\xd4-\\x8f\\xd8\\x1d4\\xfc\\x165\\xac\"\\x987\\x19\\xdf=s\\xb0\\xa7\"\\x9boM+IMH\\xedGQ\\xbene%\\xe7u\\x9d\\xb6\\nG\\\\q\\xf7\\xcb\"=\\xee\\n\\xc7)\\x9f\\xeez\\xe9\\\\\\xff\\xb3\\xef\\x10(5\\x14T\\\'\\xecQ5\\r\\xeb\\xaf$l\\xd4*\\xa6*\\x7f\\xa5\\x19J\\x9a\\x8c&amp;4[\\xcbFM\\x02\\xf65&amp;L=|r\\xed\\x19E\\xac\\xe3\\x83\\xae\\xa7q\\x9f\\xe1`\\xec\\x15&lt;\\xf6&gt;a9\\xda\\xa4m?\\xbc\\xbb\\xa1K\\xbd\\xa5\\x1b\\xbd\\xe5\\x8c\\xfd\\xa9G\\xde\\xac\\xa5\\xde\\x9c\\\'\\xcd\\xb4\\x1b\\x87)\\x7f\\xb7\\x8b\\x8f\\xe6\\x15\\xa3\\x99[\\x87\\x8a\\x89y\\xc5\\x0e~z8\\x0c\\xca \\xe7\\xfc(\\xf3\\x95,c*\\xcb\\xe3&amp;?*\\n\\x9f\\x8a*^Uu&lt;h\\x1a\\xbf\\x817\\\'\\xf0\\x17\\x1c\\xf8\\x87\\xfc\\xa7c\\xfa\\xf4g\\xec\\xf7-\\x00\\xb0(\\x81X\\x87\\xb3\\xd59\\x10\\x92%\\x16\\r#\\x9a\\xeeq`\\x932\\x0c^\\x1e\\n\\xee\\xad\\x0e\\xcd\\xc86\\x12\\x9bLS|:Y\\x86eR\\x07\\x11\\x89\\xc5\\xd0\\xac\\xe4\\x85\\xdb\\xeb\\x15`V\\x1e\\xd4\\x936X&amp;,\\x8c&amp;\\xf6\\xcc\\t\\xdc\\xe0\\xc7\\xf3%\\x03\\xd3o\\xa2k$\\xf5\\x91-,8x\\n\\xf6\\xaa\\xb0H~.\\xe9\\xa5\\x11Z\\xf7L\\x04\\xa7\\xbeT\\x11[\\x1f\\x1f\\xee \\xca\\x9ct,\\x9d\\x97\\x11\\xf2W\\x8bL\\xda\\x1d\\x18\\xfa\\xbc\\\'\\xf0gI\\x80d!c\\xbb\\xd1X\\x97P\\xb2\\x80\\x0e\\x88`\\xdcO[\\x1e\\x07\\x16\\x03af\\x19%`.,\\xa0\\x1e\\xfb\\x0e\\xd9\\x1a\\xa8\\xfb\\xc1}\\x03\\xa7@\\xeb\\x92\'\np0\n."</t>
<t tx="agp.20060821215115">class ATRULE:
    @others</t>
<t tx="agp.20060821215115.2">def Match(self,head):
    if head.startswith("@"):
        return True
    return None

</t>
<t tx="agp.20060821215115.3">def OnMatch(self,mo,node):
    pass
</t>
<t tx="agp.20061014201056"></t>
<t tx="agp.20061014201056.1">OptBuildSequenceHelp = """
Tool launch sequence, each line represents a process 
and they are called in the order that they appear.

File name and arguments must be separated by an "@"
in the form:    pathandfilename@args
    
The COMPILE keyword triggers compilation.
The LINK keyword triggers linkage.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""</t>
<t tx="agp.20061016183631">self.AddSep(length=350)
s1 = self.CHECK(master,"Build",x=5,y=self.H)
s2 = self.CHECK(master,"Seek first error",x=100,y=self.H)

s1.dpd = [s2.c]
self.AddObject(s1)
self.AddObject(s2)

t = self.TEXT(master,"Build sequence",x=5,y=self.H,vs=True)
self.HELP(master,boxtitle="Build sequence info",msg=OptBuildSequenceHelp,x=365,y=self.H+20)
self.AddObject(t)

self.H = self.H+5


</t>
<t tx="agp.20061016183631.1">self.AddSep(length=350)
s1 = self.CHECK(master,"Execute",x=5,y=self.H)
s2 = self.CHECK(master,"Connect to pipe",x=100,y=self.H)
d2 = self.CHECK(master,"Seek breakpoints",x=200,y=self.H)
self.AddObject(s1)
self.AddObject(s2)
self.AddObject(d2)
s1.dpd = [s2.c,d2.c]

d1 = self.CHECK(master,"Debug",x=5,y=self.H)
self.AddObject(d1)



</t>
<t tx="agp.20061016183631.2">self.AddSep(350)
self.AddObject(self.CHECK(master,"Xcc verbose",x=5,y=self.H))
self.AddObject(self.CHECK(master,"Filter output",x=5,y=self.H))</t>
<t tx="agp.20061016184055"></t>
<t tx="agp.20061016193303">def QueueProcess(p):
    if len(ProcessClass.List) == 0:
        ok = p.Open()
        if ok:
            ProcessClass.List.append(p)
        else:
            return False
    else:
        ProcessClass.List.append(p)
        return True</t>
<t tx="agp.20061016193833">class LkrPageClass(PageClass):
    @others
</t>
<t tx="agp.20061016193833.1">def __init__(self,cc):
    
    self.cc = cc
    ConfigClass.PageClass.__init__(self,cc,"Linker")</t>
<t tx="agp.20061016193833.2">def Browse(self):
    try:
        for o in self.Objects:
            if o and o.Name == "Linker":
                break
        else: return

        ft = ('Executables', '.exe;.bin'),
        s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Linker...")
        if s == None:
            return Error("xcc: ","Action canceled by user!")
        elif s == "":
            return Error("xcc: ","Empty path returned!")

        o.Set(os.path.normpath(s))
    except Exception:
        g.es_exception()</t>
<t tx="agp.20061016193833.3">def AddPath(self,name):
    try:
        d = tkFileDialog.askdirectory()
        if d != "":
            d = d.replace("\\",path_sym)
            for o in self.Objects:
                if o.Name == name:
                    opaths = o.Get().splitlines()
                    npaths = []
                
                    for p in opaths:
                        p = p.strip()
                        if p != "":
                            npaths.append(p)
                        
                    npaths.append(d)
                
                    o.Set(string.join(npaths,"\n"))
    except Exception:
        g.es_exception</t>
<t tx="agp.20061016193833.4">def CreateObjects(self,master): #must overide

    @others



</t>
<t tx="agp.20061016193833.5">x=10
y=10
text_w = 350
text_h = 80

# compiler entry -
self.AddObject(self.ENTRY(master,"Linker",x=5,y=5,w=350,h=20))
b = Tk.Button(master,text=" ...",command=self.Browse)
master.create_window(360,self.Y-2,anchor='nw',window=b)</t>
<t tx="agp.20061016193833.6">self.AddSep()
#-------------------------------------------------

t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
self.HELP(master,boxtitle="Arguments info",msg=CplArgumentsHelp,x=360,y=self.H+20)
self.AddObject(t1)

#------------------------------------------
t1 = self.TEXT(master,"Debug arguments",x=5,y=self.H,vs=True)
self.HELP(master,boxtitle="Debug arguments info",msg=CplDebugArgumentsHelp,x=360,y=self.H+20)
self.AddObject(t1)</t>
<t tx="agp.20061016193833.7">self.AddSep()

#-------------------------------------------------------------
b = Tk.Button(master,text="Browse",command=lambda:self.AddPath("Library search paths"))
master.create_window(360,self.H+58,anchor='nw',window=b)
t1 = self.TEXT(master,"Library search paths",x=5,y=self.H)
self.HELP(master,boxtitle="Library search paths info",msg=LibrarySearchPathsHelp,x=360,y=self.H+20)
self.AddObject(t1)

#-------------------------------------------------------------
t1 = self.TEXT(master,"Used libraries",x=5,y=self.H)
self.HELP(master,boxtitle="Used libraries info",msg=UsedLibrariesHelp,x=360,y=self.H+20)
self.AddObject(t1)</t>
<t tx="agp.20061016193833.8">ww =19
self.AddSep()
#------------------------------------------------------
lf = Tk.Frame(master,relief='flat',bd=2)
master.create_window(self.X,self.H+2,width=text_w,height=20,anchor='nw',window=lf)
Tk.Label(lf,text="Linker symbols:").pack(side="left")
self.H += 22

self.HELP(master,boxtitle="Include path and Library path info",msg=IncludePathAndLibraryPathHelp,x=360,y=self.H)
#Use library
e1 = self.ENTRY(master,"Use library",x=5,y=self.H)
#Library path
e2 = self.ENTRY(master,"Library path",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)

self.HELP(master,boxtitle="Build exe and Build dll info",msg=BuildExeAndBuildDllHelp,x=360,y=self.H)
#Build exe
e1 = self.ENTRY(master,"Build exe",x=5,y=self.H)
#Build dll
e2 = self.ENTRY(master,"Build dll",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)</t>
<t tx="agp.20061016193833.9"># ------------------
self.AddSep()
e = self.ENTRY(master,"Error detection",x=5,y=self.H,w=350,re=True)
self.HELP(master,boxtitle="Error detection info",msg=CplArgumentsHelp,x=360,y=self.H)
self.AddObject(e)</t>
<t tx="agp.20061016210621">def Link(self):
    cc = self
    
    try:
        process = ProcessClass(cc,
            cc.SELECTED_NODE,
            cc.LKR.get("Linker"),
            cc.LkrCmd(),
            start=cc.LkrStart,
            out=cc.LkrOut,
            err=cc.LkrErr,
            end=cc.LkrEnd)
        
        return ProcessClass.QueueProcess(process)        
        
    except Exception:
        g.es_exception()</t>
<t tx="agp.20061016210621.1">def RunTool(self,cc,cmdl):
    ca = cmdl.split("@",1)
    if len(ca) == 1: 
        cmd = ca[0]
        args =""
    if len(ca) == 2: 
        cmd = ca[0]
        args = ca[1]                
    
    process = ProcessClass(cc,
        cc.SELECTED_NODE,
        cc.ReplaceVars(cmd),
        cc.ReplaceVars(args),
        start=cc.ProgStart,
        out=cc.ProgOut,
        err=cc.ProgErr,
        end=cc.ProgEnd)
            
    return ProcessClass.QueueProcess(process)</t>
<t tx="agp.20061016211035">def LkrCmd(self):
    
    #g.trace()
    
    cc = self
    cwd = os.getcwd()

    if cc.DEBUG:
        cmd = cc.LKR["Debug arguments"]
    else:
        cmd = cc.LKR["Arguments"]
    
    cmd = cc.ReplaceVars(cmd.replace("\n"," ").strip())
    
    @others

    return cmd


</t>
<t tx="agp.20061016211035.1">s = cc.LKR.get("Library path",'')
if s:
    sym = s
    paths = cc.LKR.get("Library search paths",'').splitlines()
    cc.LIBPATHS = ""
    for p in paths:
        if p != "":
            cc.LIBPATHS += " "+sym+"\""+p+"\""
    cmd = cmd.replace("_LIBPATHS_",cc.LIBPATHS.strip())</t>
<t tx="agp.20061016211035.2">s = cc.LKR.get("Use library")
if s:
    sym = s
    libs = cc.LKR.get("Used libraries",'').split()
    cc.LIBRARIES = ""
    for l in libs:
        if l != "":
            cc.LIBRARIES += " "+sym+"\""+l+"\""
    cmd = cmd.replace("_LIBRARIES_",cc.LIBRARIES.strip())</t>
<t tx="agp.20061016211035.3">if cc.OUTEXT == "exe":
    s = cc.LKR.get("Build exe")
    if s: cmd = cmd.replace("_BUILD_",s)

if cc.OUTEXT == "dll":
    s = cc.LKR.get("Build dll")
    if s: cmd = cmd.replace("_BUILD_",s)</t>
<t tx="agp.20061016223957">class LangPageClass(PageClass):

    @others
</t>
<t tx="agp.20061016223957.1">def __init__(self,cc):
    
    self.cc = cc
    ConfigClass.PageClass.__init__(self,cc,"Language")
</t>
<t tx="agp.20061016223957.2">def CreateObjects(self,master): # must overide

    @others

    self.AddSep(length=self.W)</t>
<t tx="agp.20061016223957.3">e1 = self.ENTRY(master,"Language",x=7,y=15)
e2 = self.ENTRY(master,"Comment symbol",x=150,y=15)
self.AddObject(e1)
self.AddObject(e2)

e1 = self.ENTRY(master,"Source ext",x=7,y=self.H)
e2 = self.ENTRY(master,"Header ext",x=150,y=self.H)
self.AddObject(e1)
self.AddObject(e2)

e1 = self.ENTRY(master,"Binary ext",x=7,y=self.H)
self.AddObject(e1)

self.AddSep(length=self.W)

e1 = self.ENTRY(master,"Fonction opening",x=7,y=self.H)
self.AddObject(e1)
e2 = self.ENTRY(master,"Fonction closing",x=7,y=self.H)
self.AddObject(e2)

e1 = self.ENTRY(master,"Class opening",x=7,y=self.H)
self.AddObject(e1)
e2 = self.ENTRY(master,"Class closing",x=7,y=self.H)
self.AddObject(e2)</t>
<t tx="agp.20061018012249">@
UNFINISHED

The xcc nodes idea emerge from a unpublished simple plugin called cpp_nodes that i'v developed about 2 years ago. The aim of the cpp nodes plugin was to reduce redondant c++ syntaxe. It then was obvious what the next step was going to be, the breeding of the cpp nodes with the run nodes. The outcoming xcc plugin result, with the aid of already present leo's feature, in a powerfull code managing and building software. It work for any laguage and tool we'v tried so far, from assembler to c++, from sdcc to windebug.

Special coding effort are made for this plugin to work in linux, but unfortunately i have no report of any actual testing for that.


Overall operation of the node is separated in three main actions.

Firstly the source and documentation files are generated by interfacing the ParserClass, wich propose a generic parsing algorithm(tought it was developed for c++), with opened files write methodes.

Secondly the build sequence is launched by running the configured tools with a boosted version of the run_nodes plugin PROCESS class.

Thirdly, if configured for, the debugger will be launched for an interactive debuging session.


</t>
<t tx="agp.20061018014003">@
Amongst the members of the controllerclass, SELECTED_NODE, ACTIVE_NODE and CHILD_NODE are some valuable and cherished companions. Hence they are great clue of generale implement's stance. One who meddle with therein divine matter is to make vigilant awareness of the nameless trinity.</t>
<t tx="agp.20061018014003.1">@
The ParserClass is one of the core component of the plugin, it run a set of syntactic rules on the child nodes headlines. When a rule trigger, it usually write the headline and the body(@others too) by using the Declare(),Define() or Docum() function from ParserClass. These three functions are the only outputs of the plugin(apart from config save), and in fact they are not entirely output, the ParserClass must be configured to do whatever suit one. Each of these increment a specific variable contained in the parser. Define()\Declare() increment CURRENT_SRC_LINE\CURRENT_HDR_LINE and Docum() incremnent CURRENT_DOC_LINE. Apart from the increment they call functions contained in three separatelist, DEC_PROC_LIST, DEF_PROC_LIST and DOC_PROC_LIST(now try to guess wich function call wich list). In the ParserClass the lists are empty by default, so it produce nothing on its own.</t>
<t tx="agp.20070109212533">"""Integrate C/C++ compiler and debugger in a node."""

&lt;&lt; About this plugin &gt;&gt;
&lt;&lt; version history &gt;&gt;
&lt;&lt; what I did &gt;&gt;
&lt;&lt; what was redid/undid &gt;&gt;
&lt;&lt; imports &gt;&gt;

controllers = {}

if 1: # To be replaced by ivars
    &lt;&lt; globals &gt;&gt;

@language python
@tabwidth -4

__version__ = "0.5"

@others</t>
<t tx="agp.20070205104231"></t>
<t tx="agp.20070205104231.1">def LkrStart(self):
    
    #g.trace()

    cc = self
    cc.OutBuff = ""
    cc.ErrBuff = ""
    cc.FIRST_ERROR = False
    cc.aSelect(cc.SELECTED_NODE)
    process = ProcessClass.List[0]
    
    text = ""	
    if cc.VERBOSE:
        text += "\" Linking...  Starting "+process.FileName+"...\n"
        text += "\" using arguments: "+process.Arguments+"\n"		
    text += "\""+("="*60)+"\n"
    
    cc.aAddText(text)

</t>
<t tx="agp.20070205104231.2">def LkrOut(self,text):
    
    cc = self
    cc.OutBuff += text
    lines = cc.OutBuff.splitlines(True)
    if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
        cc.OutBuff = lines.pop()
    else:
        cc.OutBuff = ""
    
    text = ""	
    for l in lines:
        if l != "":
            if cc.LKR_ERR_REGEXP:
                m = cc.LKR_ERR_REGEXP.search(l,re.IGNORECASE)
                if m != None:
                    text += cc.CMT+" "+l
                else:
                    if not cc.FILTER_OUTPUT:
                        text += "\" "+l
            else:
                text += l
            
    cc.aAddText(text)

</t>
<t tx="agp.20070205104231.3">def LkrErr(self,text):
    
    cc = self
    
    cc.ErrBuff += text
    lines = cc.ErrBuff.splitlines(True)
    if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
        cc.ErrBuff = lines.pop()
    else:
        cc.ErrBuff = ""
    
    text = ""	
    for l in lines:
        text += cc.CMT+"err: "+l+"\n"
                    
    cc.aAddText(text)</t>
<t tx="agp.20070205104231.4">def LkrEnd(self,exitcode):
    
    #g.trace(repr(exitcode))
    
    cc = self
    
    text = "\""+("="*60)+"\n"
    
    if exitcode == None:
        text += "\" Link process successful!\n"
        Message("xcc : ","Link process successful!")
    else:
        text += "// Link process aborted!\n"
        Error("xcc : ","Link process failed!")
    text += "\""+("-"*60)+"\n"

    cc.aAddText(text)
    cc.aSelect()</t>
<t tx="agp.20070206130657">def ParseTree(self):
    p = ParserClass(self)
    p.Parse()</t>
<t tx="agp.20070206234855"></t>
<t tx="agp.20070206234855.1">def StartDoc(self,name,node):
    cc = self.cc
    nt = StrToBool(cc.cGet("NEW_TOPIC","False",node=node))
    uh = StrToBool(cc.cGet("USE_HEAD","False",node=node))
    pf = StrToBool(cc.cGet("PRE_FORMAT","False",node=node))
    
    if nt:
        if uh:
            self.PushDoc(name)
        else:
            self.PushDoc(name,False)
    else:
        if uh:
            self.Docum("&lt;H3&gt;"+name+"&lt;/H3&gt;\n")
            self.Docum("&lt;blockquote&gt;\n")
            
    
    if pf:
        self.Docum("&lt;pre&gt;")
            
            
</t>
<t tx="agp.20070206234855.2">def EndDoc(self,node):
    cc = self.cc
    nt = StrToBool(cc.cGet("NEW_TOPIC","False",node=node))
    uh = StrToBool(cc.cGet("USE_HEAD","False",node=node))
    pf = StrToBool(cc.cGet("PRE_FORMAT","False",node=node))
    
    if pf:
        self.Docum("&lt;/pre&gt;")
    
    if nt:
        self.PopDoc()
    elif uh:
        self.Docum("&lt;/blockquote&gt;\n")</t>
<t tx="agp.20070207022338">def StrToBool(str,value="True"):
    if str == value:
        return True
    return False</t>
<t tx="agp.20070413002425">self.AddSep()
self.AddObject(self.ENTRY(master,"Pipe eol",x=5,y=self.H))</t>
<t tx="agp.20070413150640">
 #Load button
b = Tk.Button(master,text="Load...",command=self.cfgc.LoadFromFile)
master.create_window(10,self.H+10,anchor='nw',window=b)
    
#Save button
b = Tk.Button(master,text="Save...",command=self.cfgc.SaveToFile)
master.create_window(75,self.H+10,anchor='nw',window=b)

#Python Wrapper
b = Tk.Button(master,text="Wrap to pyton",command=self.cfgc.WrapToPython)
master.create_window(140,self.H+10,anchor='nw',window=b)</t>
<t tx="agp.20070413211057">class DasmClass(Tk.Frame):

    @others
</t>
<t tx="agp.20070413211057.1">def __init__(self,cc):
   
    self.cc = cc
    self.Watching = False
    self.visible = False
    
    Tk.Frame.__init__(self,cc.LeoBodyParent,relief='groove')
    
    #self.DasmFrame = Tk.Frame(self,relief='groove')
    self.YBar = Tk.Scrollbar(self)
    self.XBar = Tk.Scrollbar(self,orient="horizontal")
    
    #self.DasmFrame.pack(side="left",fill="both",expand=1)   
    self.YBar.pack(side="right",fill="y")    
    self.XBar.pack(side="bottom",fill="x")
    
    self.DasmText = Tk.Text(
        self,
        yscrollcommand=self.YBar.set,
        xscrollcommand=self.XBar.set,
        font=cc.LeoFont,
        state='disabled',wrap='none',height=10)
    
    self.DasmText.pack(side="bottom",fill="both",expand=1)
    self.XBar.config(command=self.DasmText.xview)
    self.YBar.config(command=self.DasmText.yview)</t>
<t tx="agp.20070413211057.6">def Hide(self):
    try:
        cc = self.cc
        self.pack_forget()
        self.visible = False
        cc.ToolBar.DasmButton.config(command=self.Show,relief='raised')
    except Exception:
        g.es_exception()</t>
<t tx="agp.20070413211057.7">def Show(self):
    try:
        cc = self.cc
        cc.HideWidgets()
        
        cc.LeoBodyText.pack_forget()
        cc.LeoXBodyBar.pack_forget()
        cc.LeoYBodyBar.pack_forget()
        
        self.pack(side = "bottom",fill="both",expand=1)
        
        cc.LeoXBodyBar.pack(side = "bottom",fill="x")
        cc.LeoYBodyBar.pack(side="right",fill="y")
        if cc.BreakBar.visible:
            cc.BreakBar.Hide()
            cc.BreakBar.Show()
        cc.LeoBodyText.pack(fill="both",expand=1)
        
        cc.ToolBar.DasmButton.config(command=self.Hide,relief='sunken')
        self.visible = True
        self.Sync()
        
        if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
            DasmTaskClass(cc)
            cc.DbgOut("")
    except Exception:
        g.es_exception()</t>
<t tx="agp.20070413211057.8">def Sync(self):
    
    cc = self.cc

    if self.visible == True:
        self.DasmText.config(state='normal')
        
        self.DasmText.delete(1.0,'end')
        
        #for v in cc.sGet("Watch",[]):
        #    self.InBox.mark_set("insert",'end')			
        #    self.InBox.insert("insert",v+"\n")
            
        #    self.OutBox.mark_set("insert",'end')
        #    self.OutBox.insert("insert","- ?? -\n")	
    
        self.DasmText.config(state='disabled')</t>
<t tx="agp.20070413213649">def HideWidgets(self):
    if self.Config.visible:
        self.Config.Hide()
            
    if self.DocEdit.visible:
        self.DocEdit.Hide()
        
    if self.Watcher.visible:
        self.Watcher.Hide()
        
    if self.Dasm.visible:
        self.Dasm.Hide()</t>
<t tx="agp.20070413223141">class DasmTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="agp.20070413223141.1">def __init__(self,cc,index=0):
    
    self.cc = cc
    self.Index = index
    cc.WATCH_TASK = self
    self.Buffer = ""
    
    cc.DBG_SD.append(self.Send)
    
    self.Inited = False
</t>
<t tx="agp.20070413223141.2">def Cancel(self):
    cc = self.cc
    if self.Send in cc.DBG_SD:
        cc.DBG_SD.remove(self.Send)
    if self.Receive in cc.DBG_RD:
        cc.DBG_RD.remove(self.Receive)
    if self.OnPrompt in cc.PROMPT_RD:
        cc.PROMPT_RD.remove(self.OnPrompt)
        
    self.Watching = False
    cc.WATCH_TASK = None

</t>
<t tx="agp.20070413223141.3">def Send(self):
    cc = self.cc    
    cc.aWrite(cc.DBG["X cmd"])
    cc.DBG_SD.remove(self.Send)
    cc.DBG_RD.append(self.Receive)
    cc.PROMPT_RD.append(self.OnPrompt)
    self.Buffer = ""</t>
<t tx="agp.20070413223141.4">def Receive(self,line):
    cc = self.cc
    if cc.DBG_PROMPT == False:	
        self.Buffer += line
        </t>
<t tx="agp.20070413224924">def OnPrompt(self):
    cc = self.cc
    
    cc.DBG_RD.remove(self.Receive)
    cc.PROMPT_RD.remove(self.OnPrompt)
    t = cc.Dasm.DasmText
        
    t.config(state='normal')        
    t.delete(1.0,'end')
        
    t.insert("insert",self.Buffer)
    
    t.config(state='disabled')
    g.es("xcmd2")

</t>
<t tx="agp.20070505102536">@nocolor
@

Ok, Edward made a great job on its own and has he expected somme bugs where introduced but nothing too serious. I finished the code adaptation and resolved the bug. I tried as much as possible to follow Ed's syntactic rules. The major bugs introduced where caused by the replacement of code like "if x == "True"" by "if x == True" or "if x". The config store those value as the string, thats why they are compared against strings. I cant explain why those tree form doesnt produce the same effect by i can tell that they where causing trouble, so for now i use only comparition against string.

Ther was also problems with the leo tracing system, see the "Tracing Problems" node that follow.

</t>
<t tx="agp.20070505122726">Xcmd_icon = "S\'x\\xda\\xcd\\x93\\xc1r\\xa30\\x0c\\x86\\xef\\xbcJ/\\x01\\x9a\\xd0\\x1cz\\xb0\\xc1\\x10C\\x81\\x05J\\x13\\xb8\\x81\\xc3\\xd8\\x0b\\x9e\\xe2\\x82\\x13\\xc0O_g{\\xd8\\x17\\xd8\\xc3j\\xe6\\x9b_\\xd6H\\xb2\\xc7#\\xe5;\\x1e\\xa4\\x1eg\\x08\\x80\\x0c\\xa4\\x15\\x00I{V\\xb2M\\x1f\\xac\\xd76\\xbd\\x13\\\'U\\xb3\\x93\\xae\\xe4\\xe2\\x9b\\xb3\\xe3\\xdf\\xb5\\xaa\\xf9p\\xbc\\xb7\\xfa&lt;YG\\xd9\\x9c\\x8f\\xb6\\xd8\\xcc\\xbd(L\\xc39Xrj,)\\xeaM*QH\\xfb\\xcb\\xe2\\x9f\\xe1\\xc6e\\xb5q5\\x16\\xdc\\xfe:\\x13\\x1enD\\xd4\\x05\\x99\\xaa\\x8d\\xc8z+\\xfb\\xb0(9\\xde\\xe2\\xfet\\x8b\\xc5%\\x8du\\x1cu\\xf6\\r\\x19\\xfc\\x94\"q\\xb9\\xa1&gt;\\xb8!Q\\xe5NgK\\x87\\x9d\\xa4Cl\\xa9\\x88\\x9d\\xa8NC,\\xa9X U\\xf7s\\xefT\\x99\\xe1\\xc4\\x83\\xa4\\xafL\\xd1w\\x1a\\xad\\xcd\\x03\\xe3\\xcc\\xc3\\xa6\\xd1N\\xc9\\xc3B\\xfbE9\\x88(\\x1b\\xc2H\\xab\\xabU\\x83\\x0fi?j\\xd0\\x1a\\x17\\x88aM\\x90\\x0fu\\x90\\x83\\xcc\\x05\\x14\\xbb\\xe0\\xaf\\x19\\xe0\\x1f\\xda\\x7f\\xda\\xcc]~\\x9a\\xfd\\x19\\x0b\\x00\\xf0\\xb4\\x00\\xdf\\x85+\\x9e#\\x08A&amp;\\x9b\\x05RH_\\x12H3&gt;\\xe6&gt;\\xa4\\x00\\x07\\xa1G\\x8f\\xedG\\xe0R]\\x05\\xa1\\x07\"\\x0f\\xe4\\x85\\x88\\x8a\\x14\\xb2}e\\x88\\x18R\\x1c\\xc7\\x1e\\xed\\x8f\\x91\\xf9\\xa9\\x7f4\\xab|\\x98\\x8d\\xbb\\xbb\\x9bc\\x11\\xd3\\xc4\\xdd\\xb2\\\'\\x9d\\xd2d\\xbf\\xdf\\xa1W~\\x90\\xc3\\xa9\\xcf\\xc7h\\x08\\xd0\\xaef\\xfe\\xe8\\xaf\\xf8\\xb9\\xc1\\xfe;&amp;A\\xbff\\x06\\x9a\\x0b\\xfd\\x8c\\xeb\\xf8\\xe21\\xbaC\\xf5/Lc\\xf6\\xe4\\xc3\\x9c\\xa0(wwQ\\xb4\\x87\\xacZ(AtH\\x0e\\xee\\t\\xb65~\\x03@1k\\x80eF\\x94\\x17\\xe2\\xf3\\xe7\\xc5e\\xac c\\x07\\x0c\\xa4\\xac7\\x0c\\xebg0_=\\xba\\x0c\\x11|,\\xc2\\xf2\\xfaj|\\x03\\x12!\\xf4\\x1d\'\np0\n."</t>
<t tx="agp.20070506104706">def OnFunc(self,mo):
    pass</t>
<t tx="agp.20070506104706.1">class PyWrapperClass(ParserClass):
    @others
</t>
<t tx="agp.20070506104706.2">def __init__(self,cc):
    
    self.Result = False
    
    ParserClass.__init__(self,cc)
    self.OnStart = self.OnWrapStart
    self.OnEnd = self.OnWrapEnd
    self.WRAP_NODE = None
    
    
    self.Result = self.Parse()
    #g.trace('WriteClass.Result',self.Result)
</t>
<t tx="agp.20070506104706.7">def OnWrapStart(self):    
    
    cc = self.cc
    
    self.WRAP_NODE = cc.SELECTED_NODE.insertAfter()
    self.WRAP_NODE.setHeadString("xcc py_"+cc.NAME)
    
    self.METH_TABLE = "static PyMethodDef py_"+self.cc.NAME+"_Methods[] = {\n"
        
    return True</t>
<t tx="agp.20070506104706.8">def OnWrapEnd(self):
    self.METH_TABLE += "\t{NULL, NULL, 0, NULL}\n};"
    
    #methods table
    tn = self.WRAP_NODE.insertAsLastChild()
    tn.setHeadString("Methodes Table")
    tn.scriptSetBodyString(self.METH_TABLE)
    
    #init func
    tn = self.WRAP_NODE.insertAsLastChild()
    tn.setHeadString("PyMODINIT_FUNC initpy_"+self.cc.NAME+"();")
    
    b = "PyObject* m = Py_InitModule3(\"py_"+self.cc.NAME+"\", py_"+self.cc.NAME+"_Methods,\"\");\n\
PyObject* d = PyModule_GetDict(m);\n"
    
    #if (PyType_Ready(&amp;pytork_PYWARPType) &lt; 0)\n /
    #    return;\n /
    #Py_INCREF(&amp;pytork_PYWARPType);\n /
    #PyModule_AddObject(m, \"WARP\", (PyObject *)&amp;pytork_PYWARPType);\n"
    
    
    tn.scriptSetBodyString(b)
    
    self.cc.c.redraw()</t>
<t tx="agp.20070506114337">def WrapToPython(self):
    PyWrapperClass(self.cc)</t>
<t tx="agp.20070506114337.1">def OnFunc(self,mo):
    types = {
        "char":"b",
        "short":"s",
        "int":"i",
        "unsigned char":"B",
        "unsigned short":"S",
        "unsigned int":"I",
        "float":"f"
    }
    
    if len(self.CLASS_LIST) != 0:
        return   
    
    spec,ret,name,params,pure,dest,ctors = mo
    
    name = name[0]
    
    
    self.METH_TABLE += "\t{\""+name+"\",py_"+name+", METH_VARARGS,\"\"},\n"
    
    if ret[0].find("*") &gt; -1:
        ret = "int"
    else:
        ret = ret[0].strip()
    
    tn = self.WRAP_NODE.insertAsLastChild()
    tn.setHeadString("PyObject* py_"+name+"(PyObject* self,PyObject* args)")
    #tabf.write("{\""+name+"\",py_"+name+", METH_VARARGS,\"\"},\n")    
        
    body = ""
    varref = ""
    frmt = ""
    prm = ""
    
    g.es(params[0])
    for t,n,a in SplitParams(params[0]):
        if t.find("*") &gt; -1:
            t = "int"
        n=n.strip()
        t = t.strip()
        body += t+" "+n+";\n"
        varref += ",&amp;"+n
        frmt += types[t]
        prm += ","+n
    
    
    body += "PyArg_ParseTuple(args,\""+frmt+"\""+varref+");\n"
        
        
    if ret == "void":
        body += name+"("+prm+");\n"
        body += "return Py_BuildValue(\"i\",1);\n};\n\n"
    else:
        body +="return Py_BuildValue(\""+types[ret]+"\","+name+"("+prm[1:]+"));\n"
        
    tn.scriptSetBodyString(body)
</t>
<t tx="agp.20070519110410">self.PreValue = Tk.StringVar()
self.Pre = Tk.Checkbutton(self.TopBar,
                            offvalue="False",
                            onvalue="True",
                            command=self.SaveToNode,
                            variable=self.PreValue,
                            text="Preformat")    
self.Pre.pack(side="left")</t>
<t tx="edream.110203113231.233">@ To do:
    
     WARNING: problems with locking out event handlers could cause Leo to drop Text!
    - Do not trust this version of Leo with important data !!!
    
- The find logic doesn't properly show the found selection (or the correct body text).
    - Remove traces.

- Replace body widget with something better.

- Update joined headlines when any headline changes.

- Minor:
    - Finish all callbacks.
    - Finish dragging code.
    - Handle exception when starting by double-clicking LeoPy.leo.</t>
<t tx="edream.110203113231.618">@ It is usually best _not_ to catch exceptions in plugins:
doHook catches all exceptions and disables further calls to plugins.

If a plugin catches exceptions during startup it should either:
    
- raise the exception again.
- provide an init function at the top level that reports the failure.
@c

@language python
@tabwidth -4
@pagewidth 80
</t>
<t tx="edream.110203113231.667"></t>
<t tx="edream.110203113231.668"></t>
<t tx="edream.110203113231.722"></t>
<t tx="edream.110203113231.723">[Main]
active = Yes
interval = 20</t>
<t tx="edream.110203113231.729"></t>
<t tx="edream.110203113231.872"></t>
<t tx="edream.110403140857"></t>
<t tx="edream.110403140857.1"></t>
<t tx="edream.110403140857.2">@
--How to install the wiki markup plugin--

1) first make sure that the "add_directives" plugin is enabled. This plugin turns on support for @markup directives, and it can be found in leoPlugins.leo under the section "Plugins &amp; scripts" -&gt; Directives. In particular:
    a) check that the plugin code is enabled. You should have a line like (note the "if 1"):
        if 1: # Register the handlers...
    b) generate the plugin file. Right click with the mouse on the outline heading "@file add_directives.py" and select "Write @file nodes".

2) enable the "color_markup.py" plugin:
    a) check that the plugin code is enabled. You should have a line like:
        if Tkinter: # Register the handlers...
    b) generate the plugin file. Right click with the mouse on the outline heading "@file color_markup.py" and select "Write @file nodes".

</t>
<t tx="edream.110403140857.3">@
--How to use the wiki markup plugin--

Make sure first that both the add_directives and color_markup plugins are installed and enabled (see the Installation node for details). Make also sure that coloring is not disabled for your outline (i.e. you should not have @nocolor in an ancestor node).
    
Important: coloring via wiki markups is only supported in doc parts and Python triple-double-quoted strings (not in Python triple-single-quoted strings!).

To use the wiki markup, write

@markup wiki # turn on the wiki markup
@            # start a doc part
(here goes your marked-up text, see below)

To disable the wiki markup, write

@markup      # turn off the wiki markup

You can now use the markups either selecting the Wiki menu entries (or the corresponding keyboard shortcuts) found in the Edit-&gt;Edit Body-&gt;Wiki Tags menu, or manually inserting the tags yourself. 

If you use the menus, you can either select a word and choose the appropriate menu entry to appy styling to that word, or you can just choose a menu entry (e.g. "Bold") and start writing text with the correspongin style. Select the menu entry again to return to normal text.

See the "Supported markups" for the currently supported markups.

See also the "Example" subnode. If you have the add_directives and color_markup plugins enabled, you should see the text in that node displayed as styled text.</t>
<t tx="edream.110403140857.4">@
The currently supported markups are:

''text''                   # write text in italics
__text__                   # write text in bold
~~&lt;color&gt;:text~~           # write text in the color specified by &lt;color&gt; (e.g. blue, grey, etc)
{picture file=&lt;filename&gt;}  # load the picture indicated by &lt;filename&gt;
http://url                 # URL support: double clicking on the url will open it in the default browser.
https://url                # URL support: double clicking on the url will open it in the default browser.

Note 1: italics and bold markups can be nested, e.g.

''__text__''               # write text in italics and bold

Just remember to terminate the tags in the order they were opened.

Note 2: URLs must be terminated by a space.

By default, once the text has been markup up, the actual tags (e.g. __ for bold) are not displayed anymore. You can choose to display them selecting "Show Invisibles" from the Edit menu.
</t>
<t tx="edream.110403140857.5">@color
@markup wiki
@doc (this turns on a doc section; a '@ ' would do too)

This should be ''italic'' text
This should be __bold__ text
This text should be ~~pink:colored in pink~~, ~~blue:this one in blue~~.
This text should be ''__both bold and italic__''.
Leo's homepage is at http://webpages.charter.net/edreamleo/front.html 

You can also have wiki markups in python triple-double-quoted strings:

@c

def __dummy():
    """This is a __very important__ function."""
    return None
</t>
<t tx="edream.110403140857.6">@
Wiki markups are supported ''in subnodes too''.</t>
<t tx="edream.110403140857.7">@
Version 1.2.1, October 29, 2003.

Added documentation.
Added menu entries to tag selected text and to start/end wiki tagging.

Version 1.3, October 29, 2003.

Fixed bug in the creation of the wiki menu.
Added support for clickable http tags.

Version 1.4, November 4, 2003.
Put import tkinter in a try/except block.
Made changes for 4.1 g.app.gui architecture. (More work needed).</t>
<t tx="edream.111303100039"></t>
<t tx="edream.111303100039.1"></t>
<t tx="edream.111303100039.6">def insertHeadlineTime (self):
    
    g.es("insertHeadlineTime not ready yet")
    return

    frame = self ; c = frame.c ; v = c.currentVnode()
    h = v.headString() # Remember the old value.

    if c.edit_widget(v):
        sel1,sel2 = g.app.gui.getTextSelection(c.edit_widget(v))
        if sel1 and sel2 and sel1 != sel2: # 7/7/03
            c.edit_widget(v).delete(sel1,sel2)
        c.edit_widget(v).insert("insert",c.getTime(body=False))
        frame.idle_head_key(v)

    # A kludge to get around not knowing whether we are editing or not.
    if h.strip() == v.headString().strip():
        g.es("Edit headline to append date/time")</t>
<t tx="edream.111303100039.7"></t>
<t tx="edream.111303100039.8">def cascade(self):
    
    g.es("cascade not ready yet")
    return

    x,y,delta = 10,10,10
    for frame in g.app.windowList:
        top = frame.top
        # Compute w,h
        top.update_idletasks() # Required to get proper info.
        geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
        dim,junkx,junky = string.split(geom,'+')
        w,h = string.split(dim,'x')
        w,h = int(w),int(h)
        # Set new x,y and old w,h
        frame.setTopGeometry(w,h,x,y)
        # Compute the new offsets.
        x += 30 ; y += 30
        if x &gt; 200:
            x = 10 + delta ; y = 40 + delta
            delta += 10</t>
<t tx="edream.111303100039.9">def equalSizedPanes(self):
    
    g.es("equalSizedPanes not ready yet")
    return

    frame = self
    frame.resizePanesToRatio(0.5,frame.secondary_ratio)
</t>
<t tx="edream.111303100039.10">def hideLogWindow (self):
    
    g.es("hideLogWindow not ready yet")
    return
    
    frame = self
    frame.divideLeoSplitter2(0.99, not frame.splitVerticalFlag)</t>
<t tx="edream.111303100039.11">def minimizeAll(self):
    
    g.es("minimizeAll not ready yet")
    return

    self.minimize(g.app.findFrame)
    self.minimize(g.app.pythonFrame)
    for frame in g.app.windowList:
        self.minimize(frame)
    
def minimize(self, frame):

    if frame:
        frame.Show(False)</t>
<t tx="edream.111303100039.12"># The key invariant: self.splitVerticalFlag tells the alignment of the main splitter.
def toggleSplitDirection(self):
    
    g.es("toggleSplitDirection not ready yet")
    return

    # Abbreviations.
    frame = self
    bar1 = self.bar1 ; bar2 = self.bar2
    split1Pane1,split1Pane2 = self.split1Pane1,self.split1Pane2
    split2Pane1,split2Pane2 = self.split2Pane1,self.split2Pane2
    # Switch directions.
    verticalFlag = self.splitVerticalFlag = not self.splitVerticalFlag
    orientation = g.choose(verticalFlag,"vertical","horizontal")
    g.app.config.setWindowPref("initial_splitter_orientation",orientation)
    # Reconfigure the bars.
    bar1.place_forget()
    bar2.place_forget()
    self.configureBar(bar1,verticalFlag)
    self.configureBar(bar2,not verticalFlag)
    # Make the initial placements again.
    self.placeSplitter(bar1,split1Pane1,split1Pane2,verticalFlag)
    self.placeSplitter(bar2,split2Pane1,split2Pane2,not verticalFlag)
    # Adjust the log and body panes to give more room around the bars.
    self.reconfigurePanes()
    # Redraw with an appropriate ratio.
    vflag,ratio,secondary_ratio = frame.initialRatios()
    self.resizePanesToRatio(ratio,secondary_ratio)</t>
<t tx="edream.111303101257">def abortEditLabelCommand (self):

    g.es("abortEditLabelCommand not ready yet")
    return
    
    c = self.c ; v = c.currentVnode ; tree = self.tree
    # g.trace(v)
    if self.revertHeadline and c.edit_widget(v) and v == self.editVnode:
        
        # g.trace(`self.revertHeadline`)
        c.edit_widget(v).delete("1.0","end")
        c.edit_widget(v).insert("end",self.revertHeadline)
        tree.idle_head_key(v) # Must be done immediately.
        tree.revertHeadline = None
        tree.select(v)
        if v and len(v.t.joinList) &gt; 0:
            # 3/26/03: changed redraw_now to force_redraw.
            tree.force_redraw() # force a redraw of joined headlines.</t>
<t tx="edream.111303101257.1">def endEditLabelCommand (self):
    
    g.es("endEditLabelCommand not ready yet")
    return

    c = self.c ; tree = self.tree ; v = self.editVnode

    if v and c.edit_widget(v):
        tree.select(v)

    if v: # Bug fix 10/9/02: also redraw ancestor headlines.
        # 3/26/03: changed redraw_now to force_redraw.
        tree.force_redraw() # force a redraw of joined headlines.

    gui.set_focus(c,c.frame.bodyCtrl) # 10/14/02</t>
<t tx="edream.111303101709">def toggleActivePane(self):
    
    # This can't work from the menu...
    
    g.es("toggleActivePane not ready yet")
    return

    if self.FindFocus() == self.body.bodyCtrl:
        self.tree.SetFocus()
    else:
        self.body.bodyCtrl.SetFocus()</t>
<t tx="edream.111303103141.3">def delete_range (self,menu,n1,n2):
    
    if not menu:
        g.trace("no menu")
        return
        
    # g.trace(n1,n2,menu.GetTitle())
    
    items = menu.GetMenuItems()
    
    if 0: # debugging
        for item in items:
            id = item.GetId()
            item = menu.FindItemById(id)
            g.trace(item.GetText())
            
    ## Doesn't work:  a problem with wxPython.
    
    if len(items) &gt; n1 and len(items) &gt; n2:
        i = n1
        while i &lt;= n2:
            id = items[i].GetId()
            item = menu.FindItemById(id)
            g.trace("deleting:",item.GetText())
            menu.Delete(id)
            i += 1</t>
<t tx="edream.111303184347">@ The wxWindows menu code has problems:  changes do not take effect immediately.</t>
<t tx="edream.111303204025"></t>
<t tx="edream.111303204025.1">def adjustIndex (self,index,offset):
    
    try:
        column, row = index
        return column, row + offset
    except:
        return index + offset</t>
<t tx="edream.111303204025.2">def compareIndices(self,i,rel,j):
    
    try:
        y1,x1 = i
        y2,x2 = j
        pos1 = self.bodyCtrl.XYToPosition(x1,y1)
        pos2 = self.bodyCtrl.XYToPosition(x2,y2)
    except:
        pos1 = i
        pos2 = j
    
    val = eval("%d %s %d" % (pos1,rel,pos2))
    g.trace(i,j,rel,val)
    return val</t>
<t tx="edream.111303204025.3">def convertRowColumnToIndex (self,row,column):
    
    index = self.bodyCtrl.XYToPosition(column,row-1)
    # g.trace(column,row,"-&gt;",index)
    return index</t>
<t tx="edream.111303204025.4">def convertIndexToRowColumn (self,index):
    
    x,y = self.bodyCtrl.PositionToXY(index)
    # g.trace(index,"-&gt;",y+1,x)
    return y+1,x</t>
<t tx="edream.111303204025.5">def getImageIndex (self,image):
    
    g.trace(image)</t>
<t tx="edream.111303204517"></t>
<t tx="edream.111303205442">@ The colorizer isn't ready for prime time:
    
    - It's too slow when selecting long text
    - The screen flashes too much
    - The tkColorToWxColor routine needs much more work.
    
wxLeo should use wxStc rather than wxText!</t>
<t tx="edream.111303205611">def tag_add (self,tagName,index1,index2):
    
    # g.trace(tagName,index1,index2)

    style = self.styles.get(tagName)
    if style:
        self.bodyCtrl.SetStyle(index1,index2,style)</t>
<t tx="edream.111303205611.1">def tag_bind (self,tagName,event,callback):
    
    # g.trace(tagName,event,callback)
    pass
</t>
<t tx="edream.111303205611.2">def tag_configure (self,colorName,**keys):
    
    foreground = keys.get("foreground")
    background = keys.get("background")

    if foreground:
        fcolor = self.tkColorToWxColor (foreground)
        bcolor = self.tkColorToWxColor (background)
        if fcolor and bcolor:
            # g.trace(colorName,foreground,keys)
            style = wx.wxTextAttr(fcolor,bcolor)
            self.styles[colorName] = style
        elif fcolor:
            style = wx.wxTextAttr(fcolor)
            self.styles[colorName] = style</t>
<t tx="edream.111303205611.3">def tag_delete(self,tagName):

    if tagName == "keyword": # A kludge.

        # g.trace(tagName)
        style = wx.wxTextAttr(wx.wxBLACK)
        last = self.maxWxIndex()
        
        if 1: # This may cause the screen flash.
            self.bodyCtrl.SetStyle(0,last,style)</t>
<t tx="edream.111303205611.4">def tag_remove (self,tagName,index1,index2):
    
    g.trace(tagName,index1,index2)
    pass
</t>
<t tx="edream.111403080609">def maxWxIndex (self):
    
    return self.bodyCtrl.GetLastPosition()</t>
<t tx="edream.111403082513">def tkColorToWxColor (self, color):
    
    d = {
        "red": wx.wxRED,
        "blue": wx.wxBLUE,
        "#00aa00": wx.wxGREEN,
        "firebrick3": wx.wxRED }
        
    return d.get(color)</t>
<t tx="edream.111703103908"></t>
<t tx="edream.111703103908.2">def leoHelp (self):
    
    g.es("leoHelp not ready yet")
    
    return ##
    
    file = os.path.join(g.app.loadDir,"..","doc","sbooks.chm")
    file = g.toUnicode(file,g.app.tkEncoding) # 10/20/03

    if os.path.exists(file):
        os.startfile(file)
    else:	
        answer = g.app.gui.runAskYesNoDialog(c,
            "Download Tutorial?",
            "Download tutorial (sbooks.chm) from SourceForge?")

        if answer == "yes":
            try:
                if 0: # Download directly.  (showProgressBar needs a lot of work)
                    url = "http://umn.dl.sourceforge.net/sourceforge/leo/sbooks.chm"
                    import urllib
                    self.scale = None
                    urllib.urlretrieve(url,file,self.showProgressBar)
                    if self.scale:
                        self.scale.destroy()
                        self.scale = None
                else:
                    url = "http://prdownloads.sourceforge.net/leo/sbooks.chm?download"
                    import webbrowser
                    os.chdir(g.app.loadDir)
                    webbrowser.open_new(url)
            except:
                g.es("exception dowloading sbooks.chm")
                g.es_exception()</t>
<t tx="edream.111703103908.3">def showProgressBar (self,count,size,total):

    # g.trace("count,size,total:" + `count` + "," + `size` + "," + `total`)
    if self.scale == None:
        &lt;&lt; create the scale widget &gt;&gt;
    self.scale.set(count*size)
    self.scale.update_idletasks()</t>
<t tx="edream.111703103908.4">top = Tk.Toplevel()
top.title("Download progress")
self.scale = scale = Tk.Scale(top,state="normal",orient="horizontal",from_=0,to=total)
scale.pack()
top.lift()</t>
<t tx="edream.120603093808">@comment #
@tabwidth -4

@ Leo loads plugins in the order they appear in this file.

The FIRST mention of a plugin in this file controls whether the plugin is enabled or not:
- If the plugin's name is commented out, it is disabled, otherwise it is enabled.
- Plugins not appearing in this file are disabled.

File names may be indented as desired.
@c

##### Experimental.  Use with caution.
#__wx_gui.py

##### Standard plugins enabled in official distributions.

# Plugin_manager.py needs plugins_menu.py
#plugins_menu.py
#plugin_manager.py
#open_with.py
#mod_scripting.py
node_scripting.py
#rst3.py
#UNL.py

##### Recent work by EKR

#leoOPML.py
#__jEdit_colorizer__.py

##### All other plugins.
##### Order is important for enabled plugins that add items to the icon area.

#ConceptualSort.py
#EditAttributes.py
#FileActions.py
#Library.py
#UASearch.py
#URLloader.py
#UniversalScrolling.py

#add_directives.py
#arrows.py
#at_view.py
#autotrees.py
#base64Packager.py
#bibtex.py
#bin_nodes.py
body_rclick.py
#chapter_hoist.py
#cleo.py
#color_markup.py
#datenodes.py
#detect_urls.py
#dyna_menu.py
#fastGotoNode.py
#footprints.py
#groupOperations.py
#hoist.py
image.py
#import_cisco_config.py
#keybindings.py
keywords_nodes.py
#leo_to_html.py
#leo_to_rtf.py
#leoupdate.py
#macros.py
#mod_autosave.py
#mod_http.py
#mod_labels.py
#mod_read_dir_outline.py
#mod_shadow.py
#multifile.py
#nav_buttons.py
#newButtons.py
#niceNosent.py
node_colors.py
#nodebar.py
#nodenavigator.py
#open_shell.py
#paste_as_headlines.py
#pie_menus.py
#pretty_print.py
#print_cp.py
#quicksearch.py #integrated in leo.py
#rClick.py
read_nodes.py
#rowcol.py
#run_nodes.py
#s_menu.py
#scheduler.py
#searchbox.py
#shortcut_button.py
#slideshow.py
#table.py
#templates.py
#trace_tags.py
version_file.py
#vim.py
#word_count.py
#word_export.py
xcc_nodes.py
#xemacs.py
#xsltWithNodes.py
#zodb.py
</t>
<t tx="ekr.20040205071616">&lt;&lt; docstring &gt;&gt;
&lt;&lt; imports &gt;&gt;

OKFLAG='OK '  # Space required.
__version__ = "0.1"

@others

if Tk and not g.app.unitTesting: # Not (yet) for unit testing.

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        leoPlugins.registerHandler("start1", onStart)
        leoPlugins.registerHandler("create-optional-menus",create_UserMenu)
        leoPlugins.registerHandler("iconrclick2", onRclick)
        g.plugin_signon(__name__)
        g.es('mnplug OK+Commands+Menu aktiv',color='green')</t>
<t tx="ekr.20040205071616.1">def mnstamp():

    lt=time.localtime(time.time())
    mndatetime=time.strftime('%y%m%d %H:%M',(lt))
    return '### '+g.app.leoID+mndatetime
</t>
<t tx="ekr.20040205071616.2">def mnOKstamp():

    lt=time.localtime(time.time())
    mndatetime=time.strftime('%y%m%d %H:%M',(lt))
    return '###'+OKFLAG+g.app.leoID+mndatetime
</t>
<t tx="ekr.20040205071616.3">def onStart (tag,keywords):

    # insert function insertUser as method of class Commands at runtime
    g.funcToMethod(insertUser,leoCommands.Commands)
    g.funcToMethod(insertOKcmd,leoCommands.Commands)

</t>
<t tx="ekr.20040205071616.4">def setHeadOK(v):

    s = OKFLAG + v.headString()
    c.setHeadString(v,s)

</t>
<t tx="ekr.20040205071616.5">def insertBodystamp(c,v):

    stamp=mnOKstamp()+'\n'

    # insertAtBegin - ??!! workaround ??!! 
    # insertPointFormat is  ('row.column')
    
    oldip=c.frame.body.getInsertionPoint()
    newip=str(int(string.split(oldip,'.')[0])+1)+'.'+string.split(oldip,'.')[1]

    c.frame.body.setInsertionPoint('0.0')
    c.frame.body.insertAtInsertPoint(stamp)
    c.frame.body.setInsertionPoint(newip)
    c.frame.body.onBodyChanged("Typing")</t>
<t tx="ekr.20040205071616.6">def is_subnodesOK(v):

    if not v.hasChildren():
        return True
    else:
        ok = False
        child=v.firstChild()
        while child:
            s=child.headString()
            ok=s[0:len(OKFLAG)]==OKFLAG
            if not ok:break
            child=child.next()
    return ok

</t>
<t tx="ekr.20040205071616.7">def onRclick(tag,keywords):
    
    """Handle right click in body pane."""

    c=keywords.get('c')
    insertOKcmd(c)</t>
<t tx="ekr.20040205071616.8">def insertOKcmd(self,event=None):

    c=self; v=c.currentVnode()  
    
    if is_subnodesOK(v) :
        setHeadOK(v)
        insertBodystamp(c,v)
    else: 
        g.es('OK in child missing')</t>
<t tx="ekr.20040205071616.9">def insertUser (self,event=None):
    
    """Handle the Insert User command."""

    c = self ; v = c.currentVnode()
    
    oldSel = c.frame.body.getTextSelection()
    c.frame.body.deleteTextSelection() # Works if nothing is selected.
    
    s = mnstamp()
    
    c.frame.body.insertAtInsertPoint(s)
    c.frame.body.onBodyChanged("Typing",oldSel=oldSel)</t>
<t tx="ekr.20040205071616.10">def create_UserMenu (tag,keywords):

    c = keywords.get("c")
    
    c.pluginsMenu = c.frame.menu.createNewMenu("UserMenu")

    table = [
        ("insUser", 'Shift+F6', c.insertUser),
        ("insOK",'Ctrl+Shift+O',c.insertOKcmd)]

    c.frame.menu.createMenuEntries(c.pluginMenu,table,dynamicMenu=True)</t>
<t tx="ekr.20040331071919"></t>
<t tx="ekr.20040331071919.1">@language plain
@ascfile "doc/mod_asc_dev.asc"
@doc                
@ascskip # Time-stamp: "Mon, Jan 19 15:30 CST 2004  michael@redpriest Leo_AsciiDoc_Developers_Guide_141612300.txt"
Preface
-------

Leo2AsciiDoc is a small Python program which has been built to be used as
a plugin module for the Leo outlining editor.

This is the Developer Documentation and source code listing of
Leo2AsciiDoc.

Leo2AsciiDoc enables the contents of Leo outlines to be published to
HTML or PDF via the DocBook XML set of publishing tools.  Plain text
from the Leo outline is transformed into a final result that has:

    - typeset body text, in which bulleted and numbered lists,
      variable lists, page numbers, URLs, index terms,and bold and
      italic text are automatically recognized.
    - typeset Headings
    - a Table of Contents
    - an Index containing any items marked by the user, and any
      Python classes or functions.

indexterm:[Literate Programming]
For programmers, Leo2AsciiDoc enables a simplified version of
Literate Programming: all the documentation and code for a program
can be written in a Leo outline, and published with just a few
keystrokes.  As is normal for a Leo outline, Leo can also extract
the source code from the outline and package it into text files,
ready to be run or compiled.

Specifically, what the Leo2AsciiDoc program does is:

    - wait to be called by the Leo menu (File; Export; Export to
      AsciiDoc), and then
    - read a part of a Leo outline, and
    - write the contents to a text file that can be understood by
      the AsciiDoc program.

From there:

    - the xref:AsciiDoc[] program can then convert that text file to
      another text file that is in the DocBook XML format.
    - the standard collection of xref:DocBook[] tools can then format the
      text in HTML (web page) files or as a typeset PDF file.
    - Once set up, the whole process happens quickly and
      automatically, usually with a simple "make" command.

Here are some web locations for the items I've referenced above:

Leo::    
    http://webpages.charter.net/edreamleo/front.html[]
Python::
    http://www.python.org[]
Docbook::    
    http://docbook.org/[]
Literate Programming::
    http://www.literateprogramming.com/[]
AsciiDoc::
    http://www.methods.co.nz/asciidoc/[]
PDF::
    Adobe provides a free program, Adobe Acrobat Reader (Windows &amp;
    Linux), that is used to read and print documents produced in the
    Adobe Portable Document Format.
    http://www.adobe.com/products/acrobat/readermain.html[]

---
Michael Dawson
Marshall Research
michael_dawson at marshallresearch dot com
---
@code</t>
<t tx="ekr.20040331071919.2">@doc
@ascskip # Time-stamp: "Fri, Jan  9 15:19 CST 2004  michael@redpriest About_this_document_140583820.txt"

If you are reading this document in HTML (in a web browser) or as a
PDF file (usually in Adobe Acrobat Reader), it may interest you to
know that this document was generated from a Leo outline.

The Leo outline (in the file mod_leo2ascd.leo) contained the
Leo2AsciiDoc Users Guide, the Leo2AsciiDoc Developers Guide, and all
the Leo2AsciiDoc source code.  All of them were created by simply
typing plain text.

The working source code was exported by Leo using the "File; Tangle;
Tangle" menu selection, which created the Python program file
"mod_leo2ascd.py".

The Users Guide and the Developers Guide were created by exporting
the text from Leo, using the menu selection "File; Export; Export
All to AsciiDoc".  This created the plain text files
"mod_asc_user.asc" and "mod_asc_dev.asc" (which are the file names I
told Leo to use.)

I then typed "make all" at the console in the directory, and the
make program:

    - ran the AsciiDoc program to produce the DocBook XML files.
    - ran the xsltproc program to produce the HTML files from the
      XML files.
    - ran the xsltproc program to produce "fo" files, and ran the
      fop program to produce PDF files from the fo files.

Everything was generated automatically without any further work on
my part.

@code</t>
<t tx="ekr.20040331071919.3">@doc
@ascskip # Time-stamp: "Mon, Jan 19 15:28 CST 2004  michael@redpriest License_141615068.txt"

This is part of the Leo2AsciiDoc software package, which is released
as open source.  

The license is the most "open" I know of, and is sometimes referred
to as the "X11" or "MIT" license.  Boiled down, in non-legal terms:

    - the software is yours for free -- to run, modify and
      distribute as you will
    - I have no legal liability for any of it
    - you may not use my name.

Michael Dawson
Marshall Research
michael_dawson at marshallresearch dot com

NOTE: The following license is often referred to as the "MIT/X
Consortium License", as the "MIT license" and as the "X11" license.
My source for the exact wording is the copy at the Open Source
Initiative:  http://opensource.org/licenses/mit-license.html[]


@code
</t>
<t tx="ekr.20040331071919.4">@doc
@ascskip # Time-stamp: "Fri, Jan  9 09:18 CST 2004  michael@redpriest License_document_140581532.txt"
---
Terms and Conditions
 
COPYRIGHT AND PERMISSION NOTICE

Copyright (c) 1999,2000,2001,2002,2003,2004 Michael W. Dawson

All rights reserved.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, provided
that the above copyright notice(s) and this permission notice appear
in all copies of the Software and that both the above copyright
notice(s) and this permission notice appear in supporting
documentation.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT OF THIRD PARTY RIGHTS. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR HOLDERS INCLUDED IN THIS NOTICE BE LIABLE FOR
ANY CLAIM, OR ANY SPECIAL INDIRECT OR CONSEQUENTIAL DAMAGES, OR ANY
DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
OF THIS SOFTWARE.

Except as contained in this notice, the name of a copyright holder
shall not be used in advertising or otherwise to promote the sale,
use or other dealings in this Software without prior written
authorization of the copyright holder.
---
@code</t>
<t tx="ekr.20040331071919.5">@doc
@ascskip # Time-stamp: "Fri, Jan  9 16:13 CST 2004  michael@redpriest Version_Requirements_140584132.txt"

This is version 0.4 of Leo2AsciiDoc.  The major version of zero
indicates that it is an in-house version, not suitable for
production use elsewhere.

It was created and tested using:

    - Leo version 4.1 (release candidate 3).  Leo2AsciiDoc was
      upgraded to use the new features in 4.1 and is no longer
      compatible with previous versions.
    - AsciiDoc version 5.0.2.  Leo2AsciiDoc was upgraded to use the
      new features in 5.0.2, and is no longer compatible with older
      versions of AsciiDoc.
    - DocBook XML DTD version 4.2 and DocBook XSL stylesheets 1.60.1
    - xsltproc 1.0.30
    - fop 0.20.5

The last three items are the DocBook tool chain I'm currently using.
Any working DocBook XML tool chain you may have is likely to work,
since the major Leo2AsciiDoc effort is in producing the XML files
the tool chain uses as input.

@code</t>
<t tx="ekr.20040331071919.6">@language plain
@doc
@ascskip # Time-stamp: "Fri, Jan  9 16:00 CST 2004  michael@redpriest The_General_Approach_140588436.txt"

Leo2AsciiDoc simply copies the text from a portion of a Leo outline
to a text file.  That text file can then be processed by other
programs to produce HTML, PDF's, etc.

The text will be copied from each outline item, in outline order,
though you can skip individual nodes or sub-trees.

The idea is that you write the outline as a book, or series of
books.

If your book contains source code, you can break it up into pieces
that make it convenient to review with the reader.  Additionally,
you can discuss the pieces in any order that you like.  Using the
"tangle" command, Leo will be able to assemble and reorder the
pieces in the order required for a file of compilable source code.

As the text is copied from the outline, Leo2AsciiDoc adds minimal markup,
generally:

    - It marks up node headlines as Titles and Section Headings
      in the AsciiDoc format.
    - Program listings have AsciiDoc section markers inserted before
      and after.

A specific list follows.

@code</t>
<t tx="ekr.20040331071919.7">@language plain
@doc
@ascskip # Time-stamp: "Fri, Jan  9 16:05 CST 2004  michael@redpriest Markup_Added_140589620.txt"

    - headings:
        * By default, all outline node headings are underlined with
          the appropriate section underline character, which
          AsciiDoc will use to transform the headings into titles:
          chapter, section1, section2, etc.
        * code extracts are given an "example" heading.
    - source code sections are marked with delimiters, so that they
      can be assigned to the DocBook "programlisting" element.
    - source code sections are line-wrapped in the document output,
      for convenient html display.
    - wherever source code is exported to a source code file, the
      document with note this with an automatically generated "note"
      element.

@code
</t>
<t tx="ekr.20040331071919.8">@language python
@tabwidth -4

@doc
@ascskip on
 @silent
NB: remove leading space from above silent directive for final clean
code.

@ascskip off
@ascskip # Time-stamp: "Thu, Dec  4 11:58 CST 2003  michael@redpriest _The_Code__140751676.py"

This chapter contains all the source code for the Leo2AsciiDoc program.
The code is arranged in an order that is convenient for discussion.

On its way from the Leo outline to this document, the code has been
reformatted for printing.  Please note that:

    - code lines that are longer than the current publishing limit
      are wrapped.  Wrapped lines end in a "\" character and have
      the remainder of the text on the next line, preceeded by 4
      spaces. The real working code is not changed in this way when
      exported for actual use.
    - Some code has been extracted as Examples, and has a title
      saying something like "Example: Interesting Code".  Rather
      than repeat that code in the main code body, there is simply a
      reference to the name, enclosed in double angle brackets:
      \&lt;&lt;Interesting Code&gt;&gt;. All extracts are indexed, see "Python
      code, extracts used" in the Index at the end of the document.

@ascskip on
@root "mod_leo2ascd.py"
__version__ = ".5" # Set version for the plugin handler.
&lt;&lt; Declarations and Utilities &gt;&gt;
&lt;&lt; Write the outline tree as AsciiDoc file &gt;&gt;
&lt;&lt; Write a node &gt;&gt;
&lt;&lt; Key Functions &gt;&gt;
@code</t>
<t tx="ekr.20040331071919.9">@doc
@ascskip # Time-stamp: "Thu, Dec  4 16:05 CST 2003  michael@redpriest _Key_Functions__141128028.py"

These are the top-level functions that can be called from the Leo menu.

The next function writes the Leo outline tree of the current node to
a text file.  It first checks to see that there is an ascfile
directive in the current node, or above it, and then calls the
WriteTreeAsAsc function to write the tree starting at the ascfile
node.

If you have several documents in one Leo outline, this function will
write out the current one.

@code

def WriteTreeOfCurrentNode(c):
    f = c.frame
    vnode = c.currentVnode() # get the current vnode.
    while vnode:
        ascFileN = GetAscFilename(vnode)
        if ascFileN == None:
            vnode = vnode.parent()
        else:
            break

    if ascFileN == None:
        g.es("Sorry, there was no @ascfile directive in this outline tree.")
    else:
        WriteTreeAsAsc(vnode, ascFileN)

@doc

The next function exports all Leo2AsciiDoc documents in the entire Leo
outline, starting at the top and working through all nodes.

@code
def WriteAll(c):
    f = c.frame
    v = c.rootVnode()
    while v:
        ascFileN = GetAscFilename(v)
        if ascFileN != None:
            WriteTreeAsAsc(v, ascFileN)
            v = v.nodeAfterTree()
        else:
            v = v.threadNext()
@doc

This function is handy to see all the Leo2AsciiDoc sub-trees and source
code sub-trees in a Leo outline.  It prints the results in the log pane.

@code

def WriteAllRoots(c):
    "Writes @root directive and/or @ascfile directive to log pane."

    patternAscDirectiveFile = re.compile(r'^@ascfile')
    patternRoot = re.compile(r'^@root')

    g.es('Looking for @root or @ascfile.')
    f = c.frame
    vnode = c.rootVnode()
    while vnode:
        bodyString = vnode.bodyString()
        lines = bodyString.splitlines()
        printedHeading = False
        for line in lines:
            printLine = False
            containsAscFileDirective = patternAscDirectiveFile.match(line)
            if containsAscFileDirective:
                printLine = True
            containsRootDirective = patternRoot.match(line)
            if containsRootDirective:
                printLine = True
            if printLine:
                if not printedHeading:
                    g.es(vnode.headString())
                    printedHeading = True
                g.es('  ' + line)
        vnode = vnode.threadNext()

@doc

Next, we simply create Leo menu items for the above functions,
assuming Leo is loading this code as a module (i.e. the Python
source has been placed in the Leo plugins directory.)  As a module,
the phrase "if 0:" must be changed to "if 1:" to activate the
module.

But while the "if 0:" is left, this code can be used as a script
from the Leo scripts menu (assuming a copy of the code has been
placed in the Leo scripts directory), implementing the WriteAll
function above. This is useful in testing.

@code
def CreateAscMenu(tag,keywords):

    """Create the Outline to AsciiDoc menu item in the Export menu."""
    
    c = keywords.get('c')
    if not c: return

    exportMenu = c.frame.menu.getMenu('export')
    newEntries = (
        ("-", None, None),
        ("Export all to &amp;AsciiDoc","Alt+Shift+A",WriteAll),
        ("Export current tree to AsciiDoc","Alt+Shift+T",WriteTreeOfCurrentNode),
        ("Log all root and ascfile to log pane","Alt+Shift+L",WriteAllRoots),
    )

    c.frame.menu.createMenuEntries(exportMenu, newEntries,dynamicMenu=True)
    
if 1:
    def init():
        ok = True
        leoPlugins.registerHandler(('new','open2'), CreateAscMenu)
        g.plugin_signon(__name__)
        return ok
else:
    WriteTreeOfCurrentNode()

@doc</t>
<t tx="ekr.20040331071919.10">@doc
@ascskip # Time-stamp: "Tue, Nov 25 11:25 CST 2003  michael@redpriest _Declarations_and_Utilities__140958380.py"

Next, we define new directives to control the way we export the Leo
text, as seen in this extract from the main code.  Directives start
with an "@" character as the first character in the line.

@code
&lt;&lt;New Leo2AsciiDoc directives&gt;&gt;=
patternAscDirectiveConfig = re.compile(r'^@ascconfig\W+(\w+)\s+(\S+)')
patternAscDirectiveFile = re.compile(r'^@ascfile *"*([\w\\/\.]*)"*')
patternAscDirectiveExit = re.compile(r"^@ascexit")
patternAscDirectiveIgnore = re.compile(r"^@ascignore")
patternAscDirectiveSkip = re.compile(r"^@ascskip")
patternAscDirectiveSkipToggle = re.compile(r"^@ascskip\s*(\w+)+.*")
@doc

Next, a class to simulate constants, and make it easy to use
them. We create a class whose variables can be assigned, but not
reassigned inadvertently. As well, the "Next" function gives us an
easy way to acquire a variable of unique value when we don't care
what that value actually is, just that it is unique.

@code
&lt;&lt;Simulate Python constants&gt;&gt;=
class   _AssignUniqueConstantValue:
    """ Provide unique value to be used as a constant """
    def __init__(self):
        self.UniqueInternalValue = 0
        self.Assign_at_start()

    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            if name != "UniqueInternalValue":
                raise self.ConstError, "Can't rebind const(%s)"%name
        self.__dict__[name]=value

    def Assign_at_start(self):
        self.END_PROGRAM = self.Next()   # signal abort
        self.LINE_WAS_NONE = self.Next() # describe last line printed
        self.LINE_WAS_CODE = self.Next()
        self.LINE_WAS_DOC  = self.Next()
        self.LINE_WAS_HEAD = self.Next()
        self.LINE_PENDING_NONE  = self.Next() # describe next line to be printed
        self.LINE_PENDING_CODE  = self.Next()
        self.LINE_PENDING_DOC   = self.Next()

    def Next(self):
        self.UniqueInternalValue += 1
        return(self.UniqueInternalValue)
@doc
@ascexit
@code
&lt;&lt;The Code -- Declarations and Utilities&gt;&gt;</t>
<t tx="ekr.20040331071919.11">@
@ascskip # Time-stamp: "Fri, Dec 19 10:42 CST 2003  michael@redpriest _The_Code_Declarations_and_Utilities__140568852.py"

Here we begin the Python program, importing the modules we need, and
signing on as the Leo2AsciiDoc module in the Leo log window.
@c

import leoGlobals as g
import leoPlugins

import re
import os

g.es("---mod_leo2asc 0.4-------")

@
Next, a class to hold our configuration data. Users can change the
Leo2AsciiDoc configuration by including an "@ascconfig" directive in the
body text of a Leo outline, either in the root node or in the same
node as an "@ascfile" directive.  User directives in the root node
override the Leo2AsciiDoc defaults. Further, directives in an ascfile
node not only override the Leo2AsciiDoc defaults, but also any user
directives in the root node.
@c

&lt;&lt;Simulate Python constants&gt;&gt;

class _ConfigOptions:
    """Hold current configuration options."""
    def __init__(self):
        self.current = {}
        self.default = {}
        self.default["maxCodeLineLength"] = '76'
        self.default["delimiterForCodeStart"] = '~-~--- code starts --------'
        self.default["delimiterForCodeEnd"]   = '~-~--- code ends ----------'
        self.default["delimiterForCodeSectionDefinition"] = '*example*'
        self.default["headingUnderlines"] = '=-~^+'
        self.default["asciiDocSectionLevels"] = '5'
        self.default["PrintHeadings"] = "on"

    def __GetNodeOptions(self, vnode):
        bodyString = vnode.bodyString()
        lines = bodyString.splitlines()
        for line in lines:
            containsAscConfigDirective = patternAscDirectiveConfig.match(line)
            if containsAscConfigDirective:
                # Leo uses unicode, convert to plain ascii
                name = str(containsAscConfigDirective.group(1))
                value = str(containsAscConfigDirective.group(2))
                if self.current.has_key(name):
                    self.current[name] = value
                else:
                    g.es(vnode.headString())
                    g.es("  No such config option: %s" % name)

    def GetCurrentOptions(self,c,vnode):
        self.current.clear()
        self.current = self.default.copy()
        v = c.rootVnode()
        self.__GetNodeOptions(v)             # root node
        self.__GetNodeOptions(vnode)         # current node

# ----- assign constants ---------------------------------------------------
CV = _AssignUniqueConstantValue()
CV.NODE_IGNORE = CV.Next()              # demo of adding in code
Conf = _ConfigOptions()

# ----- globals ------------------------------------------------------------
#   compile the patterns we'll be searching for frequently
patternSectionName = re.compile("\&lt;\&lt; *(.+?) *\&gt;\&gt;")
patternSectionDefinition = re.compile("(\&lt;\&lt; *)(.+?)( *\&gt;\&gt;)(=)")
patternDirective = re.compile(r"^@")
patternCodeDirective = re.compile(r"^(@c *$)|(@code)")
patternDocDirective = re.compile(r"^(@ |@doc)(.*)")
patternRootDirective = re.compile(r"^@root\s+(.+)")
patternAscDirective = re.compile(r"^@asc")
&lt;&lt;New Leo2AsciiDoc directives&gt;&gt;
@doc

AsciiDoc recognizes titles and section headings by the underlining (a
line of characters on the next line after the text) with a line
of flag characters.  This function calculates the section level
(considering the ascfile node to be the top or "book" level) and
creates the appropriate string of flag characters.

@code
def SectionUnderline(h,level,v):
    'Return a section underline string.'
    asciiDocSectionLevels = int(Conf.current["asciiDocSectionLevels"])
    if level &lt; 0:
        g.es("Section level is less than 1:\n  %s" % v.headString())
        level = 1
    elif level &gt; asciiDocSectionLevels - 1:
        g.es("Section level is more than maximum Section Levels: %d\n  %s" \
           % (asciiDocSectionLevels, v.headString()))
        level = asciiDocSectionLevels - 1
    str = Conf.current["headingUnderlines"][level]  #'
    return str*max(len(h),1)
@doc

GetAscFilename is a frequently used function that checks a node for
the presence of an "@ascfile" directive, which specifies the name
and location of the Leo2AsciiDoc output file.

Leo2AsciiDoc will not export text without finding a file name. If no path
is given, the file will be created in the same directory as the Leo
outline.

@code
def GetAscFilename(c,vnode):
    'Checks a node for a filename directive.'
    # f is the Leo outline
    ascFileName = None
    bodyString = vnode.bodyString()
    lines = bodyString.splitlines()
    for line in lines:
        containsAscFileDirective = patternAscDirectiveFile.match(line)
        if containsAscFileDirective:
            ascFileName = containsAscFileDirective.group(1)
            if (ascFileName != None):
                base = os.path.split(c.mFileName)[0]  # linux or windows
                if (((base[0]=="/") and (ascFileName[0] != "/")) or 
                   ((base[1]==":") and (ascFileName[1] != ":"))): 
                    # no full pathname specified
                    ascFileName = os.path.join(base, ascFileName)
                Conf.GetCurrentOptions(vnode)
    return ascFileName
        
@doc

CodeChunk splits a line of text into chunks of a maximum length.
This is used in exporting source code sections of the Leo outline
for publication.

@code
def CodeChunk(text, width=72):
    """Split a line of text into a list of chunks not longer
    than width."""
    chunkList = []
    chunkStart = 0
    chunkEnd = 0
    lastSpacePosition = 0
    shortWidth = width - 4
    prefix = ''
    suffix = ' \\'
    textLen = len(text)
    if width &gt; textLen:
        chunkList.append(text)
    else:
        while chunkEnd &lt; textLen:
            if len(chunkList) &gt; 0:
                prefix = '  '
            chunkEnd = chunkStart + shortWidth
            if chunkEnd &gt; textLen:
                chunkList.append(prefix + text[chunkStart:])
                chunkEnd = textLen          # get out of jail
            else:
                lastSpacePosition = text.rfind(' ',chunkStart, chunkEnd +1)
                if lastSpacePosition != -1:  # success
                    chunkList.append(prefix + text[chunkStart:lastSpacePosition] + ' \\')
                    chunkStart = lastSpacePosition + 1
                else:
                    chunkEnd = chunkStart + shortWidth
                    chunkList.append(prefix + text[chunkStart:chunkEnd] + ' \\')
                    chunkStart = chunkEnd
    return chunkList</t>
<t tx="ekr.20040331071919.12">@doc
@ascskip # Time-stamp: "Thu, Dec  4 15:28 CST 2003  michael@redpriest _Write_the_outline_tree_as_AsciiDoc_file__141131100.py"

This function opens the output file and walks the tree of outline
nodes under the node that is passed as the first parameter.  At each
node, it calls our workhorse "WriteNode".


@code
def WriteTreeAsAsc(vnode, ascFileN):
    'Writes the tree under vnode to the file ascFile'
    def CleanUp():
        'Cleanup on exit'
        ascFile.close()

    writeNodeReturnValue = None
    startinglevel = vnode.level()
    try:
        ascFile = file(ascFileN,'w')
    except IOError:
        g.es("Could not open output file: %s" % ascFileN)
        return
    stopHere = vnode.nodeAfterTree()
    v = vnode
    while v != stopHere:
        writeNodeReturnValue = WriteNode(v, startinglevel, ascFile)
        if  writeNodeReturnValue == CV.END_PROGRAM:
            CleanUp()
            return
        elif  writeNodeReturnValue == CV.NODE_IGNORE:
            v = v.nodeAfterTree()       # ran into an @ascignore
        else:
            v = v.threadNext()

    CleanUp()
    g.es('Wrote: '+`ascFileN`)





</t>
<t tx="ekr.20040331071919.13">@doc
@ascskip # Time-stamp: "Fri, Jan  9 13:58 CST 2004  michael@redpriest _Write_a_node__140596620.py"

This is the workhorse of the program, exporting the text in a node
to the output file in a way that the AsciiDoc program will
recognize.

The basic activity is:
    - output the node headline as a DocBook section heading (Book,
      Chapter, Section1, Section2, etc.)
    - scan each line of the body text for directives, and take the
      appropriate action.  Regular expressions do the heavy lifting.
    - mark the code sections and documentation sections, so that
      DocBook can print them in the correct styles.
    - ensure that code lines do not exceed a maximum length.



@code
def WriteNode(v,startinglevel, ascFile):

    'Writes the contents of the node v to the ascFile.'

    containsAscIignore = None          # initialize
    skippingDocLines = False
    startingCodeExtract = False
    inCodeExtract = False
    statusOfWriteOutputLine = None

    def WriteOutputLine(lineString):

        'Writes a line of text to the output file.'
        try:
            ascFile.write("%s\n" % lineString)
        except IOError:
            g.es("Could not write to output file: %s" % ascFile.name)
            statusOfWriteOutputLine = CV.END_PROGRAM


    # ----- get the headline text ------------------------------------------
    h = v.headString()
    markedupAsSection = patternSectionName.match(h)
    if markedupAsSection:
        h = markedupAsSection.group(1) # dump the angle brackets

    # ----- put the body text into a list of lines -------------------------
    bodyString = v.bodyString()
    lines = bodyString.splitlines()

    lastLinePrintedType = CV.LINE_WAS_NONE
    # ----- by default, nodes start with a code section --------------------
    pendinglineType = CV.LINE_PENDING_CODE

    for line in lines:
        containsRootDirective = None

@doc

If this line starts a code extract, called a Section Definition
here, then extract the text to use as the title and set the
"startingCodeExtract" flag to guide further processing.

@code
        containsSectionDefinition = patternSectionDefinition.match(line)
        if containsSectionDefinition:
            # dump the angle brackets, etc.
#             line = containsSectionDefinition.group(2)  + '\n' + \
#                    (SectionUnderline(containsSectionDefinition.group(2),2,v))
            line = '.' + containsSectionDefinition.group(2)
            pendinglineType = CV.LINE_PENDING_CODE
            startingCodeExtract = True
@doc

Check if this line starts a @doc or @code section.

@code
        containsCodeDirective = patternCodeDirective.match(line)
        if containsCodeDirective:
            pendinglineType = CV.LINE_PENDING_CODE
            skippingDocLines = False
            continue                    # don't print this line

        containsDocDirective = patternDocDirective.match(line)
        if containsDocDirective:
            pendinglineType = CV.LINE_PENDING_DOC
            if containsDocDirective.group(2):
                # it is legal to have text on the same line
                # as a doc directive.
                line = containsDocDirective.group(2)
            else:
                continue
@doc

Check line for a Leo2AsciiDoc directive, and if so, act on it.

@code
        containsAscDirective = patternAscDirective.match(line)
        if containsAscDirective:
            containsAscIignore = patternAscDirectiveIgnore.match(line)
            if containsAscIignore:
                break

            containsAscExit = patternAscDirectiveExit.match(line)
            if containsAscExit:
                break

            containsAscSkip = patternAscDirectiveSkip.match(line)
            if containsAscSkip:
                containsAscSkipDirectiveToggle = patternAscDirectiveSkipToggle.match(line)
                if containsAscSkipDirectiveToggle:
                    if containsAscSkipDirectiveToggle.group(1).lower() == "on":
                        skippingDocLines = True
                    elif containsAscSkipDirectiveToggle.group(1).lower() == "off":
                        skippingDocLines = False
                continue

        containsOtherDirective = patternDirective.match(line)
        if containsOtherDirective:
            containsRootDirective = patternRootDirective.match(line)
            if containsRootDirective:
                line = "*note*\nThe code sections that follow, when extracted from a " + \
                       "Leo outline, will be located in: %s\n*note*" % \
                       containsRootDirective.group(1)
            else:
                continue

        # ----- we have something to print, so print heading ---------------
        if lastLinePrintedType == CV.LINE_WAS_NONE:
            if (len(h) &gt; 0) and (Conf.current["PrintHeadings"] == "on"):
                WriteOutputLine("\n\n%s" % h)
                WriteOutputLine(SectionUnderline(h,v.level()-startinglevel,v))
                lastLinePrintedType = CV.LINE_WAS_HEAD
@doc

Here we manage the transitions between code and doc sections.

@code
        if pendinglineType == CV.LINE_PENDING_DOC:
            if lastLinePrintedType != CV.LINE_WAS_DOC and \
               lastLinePrintedType != CV.LINE_WAS_HEAD:
                WriteOutputLine("%s" % Conf.current["delimiterForCodeEnd"])
                if inCodeExtract:
                    WriteOutputLine("\n%s" % Conf.current["delimiterForCodeSectionDefinition"])
                    inCodeExtract = False
                lastLinePrintedType = CV.LINE_WAS_DOC
            if skippingDocLines:
                if not containsRootDirective: # always document a root directive
                    continue

        if pendinglineType == CV.LINE_PENDING_CODE:
            if lastLinePrintedType != CV.LINE_WAS_CODE:
                if startingCodeExtract:
                    WriteOutputLine("\n%s" % line)
                    WriteOutputLine("%s" % Conf.current["delimiterForCodeSectionDefinition"])
                    inCodeExtract = True
                    line = ''
                WriteOutputLine("%s" % Conf.current["delimiterForCodeStart"])
                lastLinePrintedType = CV.LINE_WAS_CODE
                if startingCodeExtract:
                    startingCodeExtract = False
                    continue
@doc

Check for maximum code line length.  Finally, output the text to the
export file.

@code
            maxCodeLineLength = int(Conf.current["maxCodeLineLength"])
            if len(line) &lt;= maxCodeLineLength:
                WriteOutputLine("%s" % line)
            elif len(line.rstrip()) &lt;= maxCodeLineLength:
                WriteOutputLine("%s" % line.rstrip())
            else:
                lineList = CodeChunk(line, maxCodeLineLength)
                for ln in lineList:
                    WriteOutputLine("%s" % ln)
            lastLinePrintedType = CV.LINE_WAS_CODE
        else:
            WriteOutputLine("%s" % line)

        if statusOfWriteOutputLine != None:
            return statusOfWriteOutputLine

@doc

Before we leave, make sure that any ending code section is marked as
ended.

@code
    if lastLinePrintedType == CV.LINE_WAS_CODE:
        WriteOutputLine("%s" % Conf.current["delimiterForCodeEnd"])
        if inCodeExtract:
            WriteOutputLine("\n%s" % Conf.current["delimiterForCodeSectionDefinition"])
            inCodeExtract = False

    if containsAscIignore != None:
        return CV.NODE_IGNORE                        # flag ignore tree to caller

@doc

</t>
<t tx="ekr.20040331071919.14">@doc
@ascskip # Time-stamp: "Tue, Jan 13 11:09 CST 2004  michael@redpriest Other_programs_140636444.txt"

The appendices are about other programs that are used with Leo.
I'm including them because they are examples of how my setup works,
for those who may be interested in setting up something similar.

    - AsciiDoc is the program that processes the output from Leo2AsciiDoc
      into a DocBook-ready XML file.
    - Setting up DocBook is a topic that is far too large for this
      little manual, but the DocBook section which follows contains
      documentation of exactly how my working system is configured.
    - The XEmacs text editor is the one I prefer, but it is not
      necessary for the use of Leo2AsciiDoc.  Others who also use XEmacs
      might find the documentation of my Leo integration and
      multi-mode support to be useful.
@code</t>
<t tx="ekr.20040331071919.15">@language plain
@ascskip Time-stamp: "Thu, Oct 30 10:58 CST 2003  michael@redpriest Appendix_AsciiDoc__140954356.txt"
@doc
anchor:AsciiDoc[AsciiDoc]

The AsciiDoc program is written by Stuart Rackham and has its own
web site at http://www.methods.co.nz/asciidoc/[], with full
documentation.

AsciiDoc is a small program, written in Python, that reads text
which is in the AsciiDoc text format. Generally speaking, ordinary
text (such as you would write in an email message) is already in the
AsciiDoc format.  The AsciiDoc program produces (among other
choices) output in the DocBook XML format.

Text exported from a Leo outline by Leo2AsciiDoc is ready to be processed
by AsciiDoc, once AsciiDoc has been configured to recognize it.

Leo2AsciiDoc comes with an AsciiDoc configuration file that will enable
AsciiDoc to process all Leo2AsciiDoc features.  The following section
describes that configuration file.

Of course, you don't need to read or understand the configuration
file to use it.  Simply put it (leo-docbook.conf) in the same
directory as AsciiDoc's "docbook.conf" file.  When you invoke
AsciiDoc (see the xref:Makefile[] section in the DocBook appendix for
examples), give the "leo-docbook.conf" file as the configuration
parameter ("-f leo-docbook.conf".)

@ascskip on
&lt;&lt; Appendix: AsciiDoc &gt;&gt;
@code
</t>
<t tx="ekr.20040331071919.16">@language python
@tabwidth -4

@doc
@ascskip # Time-stamp: "Tue, Jan 13 11:58 CST 2004  michael@redpriest _Configuration_file__140640380.py"

AsciiDoc is customized through the use of configuration files, which
cascade, so that you can include other configuration files and
then proceed to add your changes.

The main elements of the configuration file below:

    - adds chapter and web site document types
    - switches code listings to use the DocBook "programlisting"
      element 

    *note*

    If you choose to export this configuration file from the Leo
    outline, you will have to remove escape charactersfrom some
    lines after you have exported it.

    Specifically, some lines begin with the character "\".  That
    character should be removed.

    *note*

@ascskip on
@root "other/asciidoc/leo-docbook.conf"
&lt;&lt; Configuration File &gt;&gt;
@code
# Start with the standard docbook back end configuration.
# ensure the next line is uncommented before installing
\include::docbook.conf[]

@doc

I want tabs interpreted as 4 spaces.

@code
[options]
tabsize=4
@doc

Interpret an indented paragraph as a simple paragraph.

@code
[indentedparagraph]
&lt;simpara&gt;|&lt;/simpara&gt;


@doc

For our code listings we invent a new markup that will use the
DocBook programlisting element.

@code
[blockdef-leocode]
delimiter=^\~\-~--- code(.*?)$
section=programlistingblock
presubs=specialcharacters, replacements

[programlistingblock]
&lt;programlisting&gt;
|
&lt;/programlisting&gt;

@doc

We add new markup to signify the DocBook "note" element.  This
predates AsciiDoc 5.0, and is still useful.

@code
[blockdef-note]
delimiter=^ *\*note\*$
section=noteblock
presubs=specialcharacters,quotes,specialwords,replacements,macros,glossary

# Block macro
[noteblock]
&lt;note&gt;
|
&lt;/note&gt;

[blockdef-example]
delimiter=^ *\*example\*$
options=section
section=exampleblock
presubs=replacements

# Block macro
[exampleblock]
&lt;example&gt;
&lt;title&gt;{title}&lt;/title&gt;
|
&lt;/example&gt;


@doc

The following replacements ensure basic Python code indexing.

@code
[replacements]
#----- indexing markup -----------------------------------------------------
# using regular expressions because I don't want to introduce a filter, which
# would slow things down.
#
# index python classes and defs
^(def +)(.+?)(\(.+:)=\1\2\3&lt;indexterm&gt;&lt;primary&gt;Python code, functions&lt;/primary&gt;&lt;secondary&gt;\2&lt;/secondary&gt;&lt;/indexterm&gt; 
^(class +)(.+?)(:)=\1\2\3&lt;indexterm&gt;&lt;primary&gt;Python code, classes&lt;/primary&gt;&lt;secondary&gt;\2&lt;/secondary&gt;&lt;/indexterm&gt; 
^( +def +)(.+?)(\(.+:)=\1\2\3&lt;indexterm&gt;&lt;primary&gt;Python code, methods and nested functions&lt;/primary&gt;&lt;secondary&gt;\2&lt;/secondary&gt;&lt;/indexterm&gt; 

# index code extracts
(\&amp;lt\;\&amp;lt\;)(.+?)(\&amp;gt\;\&amp;gt\;\=)=\2&lt;indexterm&gt;&lt;primary&gt;Python code, extracts explained&lt;/primary&gt;&lt;secondary&gt;\2&lt;/secondary&gt;&lt;/indexterm&gt;
(\&amp;lt\;\&amp;lt\;)(.+?)(\&amp;gt\;\&amp;gt\;)(\s*$)=\1\2\3\4&lt;indexterm&gt;&lt;primary&gt;Python code, extracts used&lt;/primary&gt;&lt;secondary&gt;\2&lt;/secondary&gt;&lt;/indexterm&gt; 

@doc

Change the standard AsciiDoc article, book and manpage definition to
use the DocBook 4.2 DTD.  Add an empty index element to the end of
the book definition so that DocBook will automatically generate an
index.

@code
#---------------------------------------------------------------------------
#----- article -------------------------------------------------------------
#---------------------------------------------------------------------------

# changing to our version of the docbook dtd
\ifdef::doctype-article[]

[header]
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE article
        PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
        "http://www.oasis-open.org/docbook/xml/4.0/docbookx.dtd"&gt;

&lt;article lang="en"&gt;
&lt;articleinfo&gt;
    &lt;title&gt;{doctitle}&lt;/title&gt;
    &lt;date&gt;{date}&lt;/date&gt;
    &lt;author&gt;
        &lt;firstname&gt;{firstname}&lt;/firstname&gt;
        &lt;othername&gt;{middlename}&lt;/othername&gt;
        &lt;surname&gt;{lastname}&lt;/surname&gt;
        &lt;affiliation&gt;
            &lt;address&gt;
                &lt;email&gt;{email}&lt;/email&gt;
            &lt;/address&gt;
        &lt;/affiliation&gt;
    &lt;/author&gt;
    &lt;authorinitials&gt;{authorinitials}&lt;/authorinitials&gt;
    &lt;revhistory&gt;&lt;revision&gt;&lt;revnumber&gt;{revision}&lt;/revnumber&gt;&lt;date&gt;{date}&lt;/date&gt;&lt;/revision&gt;&lt;/revhistory&gt;
    &lt;corpname&gt;{companyname}&lt;/corpname&gt;
&lt;/articleinfo&gt;

\endif::doctype-article[]


#---------------------------------------------------------------------------
#----- book ----------------------------------------------------------------
#---------------------------------------------------------------------------
# change to our version of docbook dtd

\ifdef::doctype-book[]

[header]
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE book
        PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
        "http://www.oasis-open.org/docbook/xml/4.0/docbookx.dtd"&gt;

&lt;book lang="en"&gt;
&lt;bookinfo&gt;
    &lt;title&gt;{doctitle}&lt;/title&gt;
    &lt;date&gt;{date}&lt;/date&gt;
    &lt;author&gt;
        &lt;firstname&gt;{firstname}&lt;/firstname&gt;
        &lt;othername&gt;{middlename}&lt;/othername&gt;
        &lt;surname&gt;{lastname}&lt;/surname&gt;
        &lt;affiliation&gt;
            &lt;address&gt;
                &lt;email&gt;{email}&lt;/email&gt;
            &lt;/address&gt;
        &lt;/affiliation&gt;
    &lt;/author&gt;
    &lt;authorinitials&gt;{authorinitials}&lt;/authorinitials&gt;
    &lt;revhistory&gt;&lt;revision&gt;&lt;revnumber&gt;{revision}&lt;/revnumber&gt;&lt;date&gt;{date}&lt;/date&gt;&lt;/revision&gt;&lt;/revhistory&gt;
    &lt;corpname&gt;{companyname}&lt;/corpname&gt;
&lt;/bookinfo&gt;


[footer]
&lt;index/&gt;
&lt;/book&gt;

\endif::doctype-book[]

#---------------------------------------------------------------------------
#----- manpage -------------------------------------------------------------
#---------------------------------------------------------------------------
\ifdef::doctype-manpage[]

[header]
&lt;!DOCTYPE refentry
        PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
        "http://www.oasis-open.org/docbook/xml/4.0/docbookx.dtd"&gt;
&lt;refentry&gt;
# The refentryinfo element is legal and should not normally be printed.
# Unfortunately some docbook processors do print it.
&lt;refentryinfo&gt;
    &lt;title&gt;{doctitle}&lt;/title&gt;
    &lt;date&gt;{date}&lt;/date&gt;
    &lt;author&gt;
        &lt;firstname&gt;{firstname}&lt;/firstname&gt;
        &lt;othername&gt;{middlename}&lt;/othername&gt;
        &lt;surname&gt;{lastname}&lt;/surname&gt;
        &lt;affiliation&gt;
            &lt;address&gt;
                &lt;email&gt;{email}&lt;/email&gt;
            &lt;/address&gt;
        &lt;/affiliation&gt;
    &lt;/author&gt;
    &lt;authorinitials&gt;{authorinitials}&lt;/authorinitials&gt;
    &lt;revhistory&gt;&lt;revision&gt;&lt;revnumber&gt;{revision}&lt;/revnumber&gt;&lt;date&gt;{date}&lt;/date&gt;&lt;/revision&gt;&lt;/revhistory&gt;
    &lt;corpname&gt;{companyname}&lt;/corpname&gt;
&lt;/refentryinfo&gt;
&lt;refmeta&gt;
&lt;refentrytitle&gt;{mantitle}&lt;/refentrytitle&gt;
&lt;manvolnum&gt;{manvolnum}&lt;/manvolnum&gt;
&lt;/refmeta&gt;
&lt;refnamediv&gt;
    &lt;refname&gt;{manname}&lt;/refname&gt;
    &lt;refpurpose&gt;{manpurpose}&lt;/refpurpose&gt;
&lt;/refnamediv&gt;

\endif::doctype-manpage[]



@doc

Add chapter and website document types.

@code
#---------------------------------------------------------------------------
#----- new: chapter --------------------------------------------------------
#---------------------------------------------------------------------------
\ifdef::doctype-chapter[]

[header]
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE chapter
        PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
        "http://www.oasis-open.org/docbook/xml/4.0/docbookx.dtd"&gt;
&lt;chapter&gt;
&lt;title&gt;{doctitle}&lt;/title&gt;

[footer]
&lt;/chapter&gt;


# Section macros
# Using &lt;abstract&gt; semantics restricts preface to &lt;simpara&gt; elements.
[preface]
|

[sect1]
&lt;sect1&gt;
&lt;title&gt;{title}&lt;/title&gt;
|
&lt;/sect1&gt;

[sect2]
&lt;sect2&gt;
&lt;title&gt;{title}&lt;/title&gt;
|
&lt;/sect2&gt;

[sect3]
&lt;sect3&gt;
&lt;title&gt;{title}&lt;/title&gt;
|
&lt;/sect3&gt;

[options]
outfilesuffix=.xml

\endif::doctype-chapter[]

@doc

Website requires a unique id for each page.  I've changed AsciiDoc
to provide the HTML filename as the id, and we use it here. We'll
use the date the XML file was created as the update date.

@code
#---------------------------------------------------------------------------
#----- new: website --------------------------------------------------------
#---------------------------------------------------------------------------
\ifdef::doctype-website[]
[header]
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE webpage SYSTEM "website-full.dtd"&gt;
&lt;webpage id="{infilebase}"&gt;
  &lt;head&gt;
    &lt;title&gt;{doctitle}&lt;/title&gt;
  &lt;/head&gt;
  &lt;config param="rcsdate" value="Updated: {localdate}  {localtime}"/&gt;
[footer]
&lt;/webpage&gt;

[options]
outfilesuffix=.xml

\endif::doctype-website[]

</t>
<t tx="ekr.20040331071919.17">@silent
@doc
@ascskip # Time-stamp: "Tue, Jan 13 14:11 CST 2004  michael@redpriest _Patches__140641532.txt"

I've patched the source code for AsciiDoc (asciidoc.py) with a few
small changes to allow AsciiDoc to process chapters and DocBook
web site documents as well as the DocBook book format.  Since I use
Linux, I also changed the default line-ending code to the Linux
default.

For the exact changes I made, the following output at the end of
this section was created by GNU diff (version 2.8.4) with the
command

---
LC_ALL=C TZ=UTC0 diff -Naur 5.0.2-original 5.0.2-mrc-patched \
    &gt;mrc-asciidoc-5.0.2-patch-diff
---

I include this mainly so that you can see the exact changes I made.
However, you may want to patch a copy of the original in exactly the
same way. 

To patch a copy of the original asciidoc.py (version 5.0.2), one
would use the patch command as follows (when in the same directory
as the copy of asciidoc.py and mrc-asciidoc-5.0.2-patch-diff)

---
patch -Np1 &lt;mrc2-asciidoc-5.0.2-patch-diff
---

@ascskip on
@root "other/asciidoc/mrc-asciidoc-5.0.2-patch-diff"
&lt;&lt; Patches &gt;&gt;
@code
diff -Naur 5.0.2-original/asciidoc.py 5.0.2-mrc-patched/asciidoc.py
--- 5.0.2-original/asciidoc.py	2003-12-16 00:16:28.000000000 +0000
+++ 5.0.2-mrc-patched/asciidoc.py	2004-01-08 17:45:37.000000000 +0000
@@ -838,12 +838,15 @@
         '''Set predefined glossary entries that follow configuration file
         loading.'''
         self.glossary['infile'] = reader.fname
+        # mwd Monday, June 23, 2003 for use in website
+        self.glossary['infilebase'] = os.path.splitext(os.path.split(reader.fname)[1]) [0]
         self.glossary['outfile'] = reader.fname
         s = os.path.splitext(writer.fname)[1][1:]   # Output file extension.
         self.glossary['filetype'] = s
         self.glossary['filetype-'+s] = ''
     def translate(self):
-        assert self.doctype in ('article','manpage','book'), \
+        # mwd 2003-Jun-23 assert self.doctype in ('article','manpage','book'), \
+        assert self.doctype in ('article','chapter','website','manpage', 'book'), \
             'illegal document type'
         assert self.level == 0
         reader.tabsize = config.tabsize
@@ -864,7 +867,8 @@
             if not config.suppress_headers:
                 hdr = config.subs_section('header',{})
                 writer.write(hdr)
-            if self.doctype in ('article','book'):
+            # mwd 2003-Jun-23 if self.doctype in ('article','book'):
+            if self.doctype in ('article','book','chapter','website'):
                 # Translate 'preamble' (untitled elements between header
                 # and first section title).
                 if Lex.next() is not Title:
@@ -952,7 +956,7 @@
                 # Parse revision line.
                 s = reader.read()
                 s = subs_glossary([s])[0]
-                # Match RCS/CVS $Id: leoPlugins.leo,v 1.2 2006/04/11 14:34:15 edream Exp $ marker format.
+                # Match RCS/CVS $Id: leoPlugins.leo,v 1.2 2006/04/11 14:34:15 edream Exp $ marker format.
                 mo = re.match(r'^\$Id: \S+ (?P&lt;revision&gt;\S+)' \
                     ' (?P&lt;date&gt;\S+) \S+ \S+ \S+ \$$',s)
                 if not mo:
@@ -2573,7 +2577,8 @@
 
 class Writer:
     '''Writes lines to output file.'''
-    EOL = '\r\n'    # End of line terminator.
+    # mwd 2003-Jun-23 EOL = '\r\n'    # End of line terminator.
+    EOL = '\n'    # End of line terminator.
     f = None        # Output file object.
     fname= None     # Output file name.
     lines_out = 0   # Number of lines written.
@@ -3068,7 +3073,8 @@
     The AsciiDoc document is read from file object src the translated
     DocBook file written to file object dst.'''
     try:
-        if doctype not in ('article','manpage','book'):
+        # mwd-2004-Jan-05 if doctype not in ('article','manpage','book'):
+        if doctype not in ('article','chapter','website','manpage', 'book'):
             raise EAsciiDoc,'illegal document type'
         if backend == 'linuxdoc' and doctype != 'article':
             raise EAsciiDoc,'%s %s documents are not supported' \
</t>
<t tx="ekr.20040331071919.18">@language plain
@ascskip Time-stamp: "Fri, Dec 19 11:48 CST 2003  michael@redpriest Appendix_DocBook_140578660.txt"
@doc

anchor:DocBook[DocBook]
DocBook is a project that provides:

    - a specification for the text markup (DTD) of DocBook XML
      documents, and
    - a set of XSLT stylesheets that can be used by an XSLT engine
      to transform those XML documents to HTML, PDF, etc.
      
If you create your text documents using the rules in the DocBook
DTD, you can use the DocBook XSLT stylesheets to produce various
output formats, such as HTML and PDF.

The DocBook project is designed for the production of computer
documentation, but is actually used for a wide variety of documents.

Some web resources:

    - the official home page for DocBook: The Definitive Guide:
        http://docbook.org/[]
    - DocBook Basics:
        http://www.dpawson.co.uk/docbook/reference.html[]
    - DocBook Open Repository:
        http://sourceforge.net/projects/docbook/[]
    - DocBook XSL: The Complete Guide:
        http://www.sagehill.net/docbookxsl/index.html[]

I include this section as documentation of one setup that works --
it translates Leo2AsciiDoc output to HTML and PDF.

This is not a guide to the installation, setup and operation of
DocBook, just an example of a working system.

@ascskip on
&lt;&lt; Appendix: DocBook &gt;&gt;
@code
</t>
<t tx="ekr.20040331071919.19">@doc
@ascskip # Time-stamp: "Thu, Jan  8 13:57 CST 2004  michael@redpriest _Tool_Chain__140810780.txt"

Documents go through a number of stages in their creation.  Each
stage may involve one or more tools or programs, which form a tool
chain: each performing some processing and handing off to the next.

As a simple example, for this document:


    - text creation was handled by XEmacs, a text
      editor (which functioned as a Leo plugin.)
      indexterm:[XEmacs]
      indexterm:[GNU Make]
      indexterm:[AsciiDoc]
      indexterm:[xsltproc]
      indexterm:[FOP]
    - text storage and organization was handled by Leo, an outlining
      editor.
    - text was exported from Leo to a plain-text file, using the
      Leo2AsciiDoc program.
    - from there, all transformations are automated by the
      GNU Make program.
    - the DocBook XML document was created by the
      AsciiDoc program, which transformed the
      plain-text file to XML.
    - The HTML pages were created by the
      xsltproc program. xsltproc read the XML
      document, and the DocBook XSLT stylesheets, and then created
      each HTML page.
    - To make the PDF file, the xsltproc program used the same
      process as for the HTML pages, except that it created a
      Formatting Objects (FO) file instead.  Then the
      FOP program processed the FO file, producing
      the final PDF file.  This process was also automated.

All I did was type in text for each section, arranging it much as I
usually do for email.  The rest was handled automatically by
clicking on a Leo menu, or entering a short command at the console.
For example: "make all".

There are many, many choices of tools to put in your DocBook tool
chain.  You can even purchase complete packages, from text editing
to PDF generation.

@code</t>
<t tx="ekr.20040331071919.20">@language plain
@tabwidth 4
@doc
@ascskip # Time-stamp: "Thu, Jan 15 15:39 CST 2004  michael@redpriest _Make_File__140651828.txt"

anchor:Makefile[Makefile]
In my case, I use a standard unix-style "make" setup for processing
the text exported from a Leo outline.  It simply automates the
commands which I would otherwise have to type at the command line.

After Leo2AsciiDoc exports the text from the Leo outline to a disk file,
the Make program takes over.  It reads rules in a file named
"Makefile" and calls the necessary programs to make the
requested output.

This Makefile takes over where Leo2AsciiDoc leaves off.  It directs the
AsciiDoc conversion of the Leo2AsciiDoc text file to XML, and then the
DocBook conversion of the XML file to HTML pages or a PDF document.

indexterm:[GNU Make]
I use GNU Make.  For example, assuming I am in xterm and located in
the same directory as the Makefile, I just enter the command

---
make pdf-dev
---
and the make program guides the creation of the PDF version of The
Developers Guide, using the instructions in this Makefile.  The PDF
is available within seconds.

The Makefile instructions, in brief:

    - the AsciiDoc program is called to make an XML file.
    - the xsltproc program is called to process the XML file to
      either HTML or a Formatting Objects file for further
      translation to PDF
        * various XSLT style sheets (html.xsl, man.xsl, etc.) are
          used by xsltproc to guide the transformation of the XML
          file.  Typically, they call the DocBook stylesheets for
          the heavy lifting, and set a few simple options.
    - the FOP program is used to process the intermediate fo file to
      the final PDF file.

This is by no means a model Makefile.  It is included because it
works for me in my office, and may thus be useful as an example for
other people who want to set up Make for this purpose.

@ascskip xemacs-makefile-mode-on
@ascskip on
@root "doc/Makefile"
&lt;&lt; Make File &gt;&gt;
@code
#----- global variables -----------------------------------------
DEVGUIDE=mod_asc_dev
USERGUIDE=mod_asc_user
CSS=dbstyle.css

MAN=${DOC}.1
STYLESHEET_MAN=man.xsl
# default docbook, located by /etc/xml/catalog
STYLESHEET_MAN_HTML=docbook.xsl
MAN_OUTPUT_DIR=man

STYLESHEET_HTML=html.xsl
HTML_DEV_OUTPUT_DIR=html-dev
HTML_USER_OUTPUT_DIR=html-user
STYLESHEET_CHUNK=chunkit.xsl
CHUNK_DEV_OUTPUT_DIR=chunk-dev
CHUNK_USER_OUTPUT_DIR=chunk-user

STYLESHEET_FO_FOP=fo-fop.xsl
PDF_DEV_OUTPUT_DIR=pdf-dev
PDF_USER_OUTPUT_DIR=pdf-user

ASCIIDOC_COMMAND=python asciidoc/asciidoc.py -v -b docbook -d book
ASCIIDOC_CONFIG=asciidoc/leo-docbook.conf

#   $@ target file name
#   $&lt; name of the first prerequisite
#   $* stem that rule matched

#----- pattern rules -------------------------------------------------------
%.xml	:	%.asc
#	asciidoc -b docbook -d book -f ${ASCIIDOC_CONFIG} -o $@ $&lt;
    ${ASCIIDOC_COMMAND}  -f ${ASCIIDOC_CONFIG} -o $@ $&lt;
    xsltproc --output $*.final.xml customize.xsl $@


%.html	:	%.xml css
    xsltproc --xinclude --output ${OUTPUT} ${STYLESHEET}  $*.final.xml
    touch $*.xml

%.pdf	:	%.xml
    xsltproc --xinclude  --output ${OUTPUT}/$*.fo $(STYLESHEET) $*.final.xml
    fop -fo  ${OUTPUT}/$*.fo  -pdf ${OUTPUT}/$*.pdf 
    -$(RM) ${OUTPUT}/$*.fo

#----- usage ---------------------------------------------------------------
usage	:
    @echo; echo "primary make modules: html-dev chunk-dev pdf-dev"
    @echo       "                      html-user chunk-user pdf-user"
    @echo



#---------------------------------------------------------------------------
#----- modules -------------------------------------------------------------
#---------------------------------------------------------------------------

# docbook
#---------------------------------------------------------------------------

all	:	css pdf-dev html-dev sub-chunk-dev html-user sub-chunk-user pdf-user

#----- DocBook html stylesheet ---------------------------------------------
css:
    cat base.css   &gt;  $(CSS)
    cat docstyle.css &gt;&gt; $(CSS)

#----- Developers Guide ----------------------------------------------------
#   #----- one page -----------------------------------------------------
html-dev	:	STYLESHEET=$(STYLESHEET_HTML)
html-dev	:	OUTPUT=${HTML_DEV_OUTPUT_DIR}/$*.html
html-dev	:	mkdirhtmldev ${DEVGUIDE}.html
    cp ${CSS} ${HTML_DEV_OUTPUT_DIR}

mkdirhtmldev	:	cleanhtmldev
    mkdir ${HTML_DEV_OUTPUT_DIR}

#   #----- individual pages ------------------------------------------------
chunk-dev	:	STYLESHEET=$(STYLESHEET_CHUNK)
chunk-dev	:	OUTPUT=$(CHUNK_DEV_OUTPUT_DIR)/
chunk-dev	:	mkdirchunkdev ${DEVGUIDE}.html
    cp chunk-dev-frame*.html ${CHUNK_DEV_OUTPUT_DIR}
    cp ${CSS} ${CHUNK_DEV_OUTPUT_DIR}
    cp frametoc.css ${CHUNK_DEV_OUTPUT_DIR}
    cp -r ../graphics ${CHUNK_DEV_OUTPUT_DIR}
# put in frame target line
    sed -f sed-dev-frame ${CHUNK_DEV_OUTPUT_DIR}/index.html &gt;${CHUNK_DEV_OUTPUT_DIR}/chunk-dev-frame-toc.html

mkdirchunkdev	:	cleanchunkdev
    mkdir ${CHUNK_DEV_OUTPUT_DIR}

sub-chunk-dev	:
    ${MAKE} chunk-dev

#----- Users Guide ---------------------------------------------------------
#   #----- one page -----------------------------------------------------
html-user	:	STYLESHEET=$(STYLESHEET_HTML)
html-user:	OUTPUT=${HTML_USER_OUTPUT_DIR}/$*.html
html-user:	mkdirhtmluser ${USERGUIDE}.html
    cp ${CSS} ${HTML_USER_OUTPUT_DIR}

mkdirhtmluser	:	cleanhtmluser
    mkdir ${HTML_USER_OUTPUT_DIR}

#   #----- individual pages ------------------------------------------------
chunk-user	:	STYLESHEET=$(STYLESHEET_CHUNK)
chunk-user	:	OUTPUT=$(CHUNK_USER_OUTPUT_DIR)/
chunk-user	:	cleanchunkuser ${USERGUIDE}.html
    cp chunk-user-frame*.html ${CHUNK_USER_OUTPUT_DIR}
    cp ${CSS} ${CHUNK_USER_OUTPUT_DIR}
    cp frametoc.css ${CHUNK_USER_OUTPUT_DIR}
    cp -r ../graphics ${CHUNK_USER_OUTPUT_DIR}
# put in frame target line
    sed -f sed-user-frame ${CHUNK_USER_OUTPUT_DIR}/index.html &gt;${CHUNK_USER_OUTPUT_DIR}/chunk-user-frame-toc.html

mkdirchunkuser	:	cleanchunkuser
    mkdir ${CHUNK_USER_OUTPUT_DIR}

sub-chunk-user	:
    ${MAKE} chunk-user

#   #----- pdf -------------------------------------------------------------
pdf-dev		:	STYLESHEET=$(STYLESHEET_FO_FOP)
pdf-dev		:	OUTPUT=$(PDF_DEV_OUTPUT_DIR)
pdf-dev		:	mkdirpdf ${DEVGUIDE}.pdf

pdf-user		:	STYLESHEET=$(STYLESHEET_FO_FOP)
pdf-user		:	OUTPUT=$(PDF_USER_OUTPUT_DIR)
pdf-user		:	mkdirpdf ${USERGUIDE}.pdf

#   mkdirpdf exists only to make an empty directory for the pdf working files
mkdirpdf	:
    -mkdir $(PDF_DEV_OUTPUT_DIR)
    -mkdir $(PDF_USER_OUTPUT_DIR)




#----- clean ---------------------------------------------------------------
clean	: cleanhtml cleanchunk cleanpdf cleanman cleanclutter 

cleanhtml	:	cleanhtmluser cleanhtmldev

cleanhtmluser	:
    -$(RM) -r $(HTML_USER_OUTPUT_DIR)

cleanhtmldev	:
    -$(RM) -r $(HTML_DEV_OUTPUT_DIR)

cleanchunk	:	cleanchunkuser cleanchunkdev

cleanchunkuser	:
    -$(RM) -r $(CHUNK_USER_OUTPUT_DIR)

cleanchunkdev	:
    -$(RM) -r $(CHUNK_DEV_OUTPUT_DIR)

cleanpdf	:
    -$(RM) -r $(PDF_OUTPUT_DIR)

cleanman	:
    -$(RM) -r $(MAN_OUTPUT_DIR)

cleanclutter: 
    -$(RM) -r *.xml

.PRECIOUS	:	%.xml
@doc
@ascskip xemacs-makefile-mode-off
@code
</t>
<t tx="ekr.20040331071919.21">@silent
@doc
@ascskip # Time-stamp: "Wed, Oct  1 15:33 CST 2003  michael@redpriest _Style_Sheets__140741140.txt"

When the Makefile calls the xsltproc program, it gives it the name
of an XSLT stylesheet to guide the production of the result.

Following are simple XSLT stylesheets that are used to:
    - set formatting options, and
    - call the main DocBook XSLT stylesheets.

The stylesheets cascade (each adding its options to the total), with
the original stylesheet including others as needed, and always
calling the main DocBook stylesheets at some point.

@code
</t>
<t tx="ekr.20040331071919.22">@comment &lt;!-- --&gt;
@silent
@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:01 CST 2004  michael@redpriest _General__139758588.txt"

indexterm:[Stylesheets, common-links.xsl]
This is the entire common-links style sheet ("common-links.xsl"),
which sets basic Table of Contents and chapter cross-reference
preferences.

This stylesheet is called by both HTML and PDF stylesheets.

@ascskip on
@ascskip xemacs-xsl-mode-on
@root "doc/common-links.xsl"
&lt;&lt; General &gt;&gt;
@code
&lt;?xml version='1.0'?&gt; 
&lt;xsl:stylesheet  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  version="1.0"&gt; 

&lt;!--===== 
    This changes a chapter cross-reference to include the chapter
    title text. 
--&gt;
&lt;xsl:param name="local.l10n.xml" select="document('')"/&gt; 
&lt;l:i18n xmlns:l="http://docbook.sourceforge.net/xmlns/l10n/1.0"&gt; 
  &lt;l:l10n language="en"&gt; 
    &lt;l:context name="xref"&gt; 
      &lt;l:template name="chapter" text="Chapter %n: &amp;#8220;%t&amp;#8221;"/&gt; 
    &lt;/l:context&gt;   
  &lt;/l:l10n&gt;
&lt;/l:i18n&gt;

&lt;xsl:param name="generate.toc"&gt;
book      toc,title,figure,table,example,equation
chapter   title
&lt;/xsl:param&gt;

&lt;!-- only 1 toc in the doc --&gt;
&lt;xsl:param name="generate.section.toc.level" select="1"/&gt;

&lt;!-- toc shows 3 levels of sections --&gt;
&lt;xsl:param name="toc.section.depth"&gt;3&lt;/xsl:param&gt;

&lt;xsl:param name="generate.index" select="1"&gt;&lt;/xsl:param&gt;

&lt;!--===== omit the title for notes, tips ================================--&gt;
&lt;xsl:param name="admon.textlabel" select="0"&gt;&lt;/xsl:param&gt;

&lt;/xsl:stylesheet&gt;
@doc
@ascskip xemacs-xsl-mode-off


</t>
<t tx="ekr.20040331071919.23">@comment &lt;!-- --&gt;
@silent
@doc
@ascskip # Time-stamp: "Tue, Jan 20 11:42 CST 2004  michael@redpriest _Customize__141637044.txt"


indexterm:[customize.xsl]
This is the entire customize style sheet ("customize.xsl", which is
used by the Makefile to make changes to the standard xml file
produced from the AsciiDoc output.  It results in a file suffixed
".final.xml" which is used by both the HTML and PDF stylesheets.

Currently, the stylesheet copies the xml file:

    - changing any chapter elements that have a title beginning
      with "Appendix: " to DocBook appendix elements.  This is from
      AsciiDoc 3.2 days, when AsciiDoc didn't know about appendix
      elements. I haven't yet modified Leo2AsciiDoc to take
      advantage of the automatic appendix elements in AsciiDoc 5.0.
    - adding custom bookinfo elements

I've used XSLT for this, but it could have been done with python,
AWK, sed, or other tools.

@ascskip on
@ascskip xemacs-xsl-mode-on
@root "doc/customize.xsl"
&lt;&lt; Customize &gt;&gt;
@code
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"&gt;

&lt;xsl:variable name="AppendBegin"&gt;Appendix: &lt;/xsl:variable&gt;

&lt;!--~~~~~~ copy everything ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--&gt;
&lt;xsl:template match="@*|node()"&gt;
   &lt;xsl:copy&gt;
      &lt;xsl:apply-templates select="@*|node()"/&gt;
   &lt;/xsl:copy&gt;
&lt;/xsl:template&gt;

&lt;!--~~~~~~ delete the appendix string from the title ~~~~~~~~~~~~~~~~~~~~--&gt;
&lt;xsl:template match="/book/chapter/title[starts-with(text(),$AppendBegin)]"&gt;
  &lt;title&gt;
  &lt;xsl:value-of select="substring-after(text(),$AppendBegin)"/&gt;
  &lt;/title&gt;
  &lt;xsl:apply-templates select="*" /&gt; 
&lt;/xsl:template&gt;

&lt;!--~~~~~~ change appendix chapter element to appendix element ~~~~~~~~~~--&gt;
&lt;xsl:template match="/book/chapter[starts-with(title,$AppendBegin)]"&gt;
  &lt;appendix&gt;
    &lt;xsl:apply-templates select="*" /&gt; 
  &lt;/appendix&gt;
&lt;/xsl:template&gt;

&lt;!--~~~~~~ bookinfo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--&gt;
&lt;!--
From Leo2AsciiDoc, only the bookinfo title is filled in, with a
blank author.  Here, we replace the author element with any and all
bookinfo elements we please.
--&gt;
  
&lt;xsl:template match="/book/bookinfo/author"&gt;
  &lt;author&gt;
    &lt;firstname&gt;Michael&lt;/firstname&gt;&lt;surname&gt;Dawson&lt;/surname&gt;
    &lt;affiliation&gt;
      &lt;address&gt;
        &lt;otheraddr&gt;
          &lt;ulink url="http://www.marshallresearch.com/contact.html"&gt;
            at Marshall Research
          &lt;/ulink&gt;
        &lt;/otheraddr&gt;
      &lt;/address&gt;
    &lt;/affiliation&gt;
  &lt;/author&gt;
  &lt;revhistory&gt;
    &lt;revision&gt;
      &lt;revnumber&gt;0.4a&lt;/revnumber&gt;
      &lt;date&gt;Jan 21 2004&lt;/date&gt;
      &lt;authorinitials&gt;mwd&lt;/authorinitials&gt;
      &lt;revremark&gt;Formatting enhancements&lt;/revremark&gt;
    &lt;/revision&gt;
    &lt;revision&gt;
      &lt;revnumber&gt;0.4&lt;/revnumber&gt;
      &lt;date&gt;Jan 19 2004&lt;/date&gt;
      &lt;authorinitials&gt;mwd&lt;/authorinitials&gt;
      &lt;revremark&gt;First release&lt;/revremark&gt;
    &lt;/revision&gt;
  &lt;/revhistory&gt;
&lt;/xsl:template&gt;


&lt;/xsl:stylesheet&gt;

@doc
@ascskip xemacs-xsl-mode-off

</t>
<t tx="ekr.20040331071919.24">@silent
@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:02 CST 2004  michael@redpriest _HTML_One_File__139289780.txt"

indexterm:[Stylesheets,html.xsl]
For one long page of HTML, we simply import the DocBook stylesheets
and our small custom stylesheets that set our standard options.
This is the "html.xsl" stylesheet.

@ascskip on
@ascskip xemacs-xsl-mode-on
@root "doc/html.xsl"
&lt;&lt; HTML: One File &gt;&gt;
@code
&lt;?xml version='1.0'?&gt; 
&lt;xsl:stylesheet  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  version="1.0"&gt; 

&lt;!--===== the catalog (/etx/xml/catalog) will convert this to the local pathname --&gt;
&lt;xsl:import href="docbook.xsl"/&gt;

&lt;xsl:import href="common-links.xsl"/&gt;
&lt;xsl:import href="common-html.xsl"/&gt;

&lt;/xsl:stylesheet&gt; 
@doc
@ascskip xemacs-xsl-mode-off


</t>
<t tx="ekr.20040331071919.25">@silent
@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:40 CST 2004  michael@redpriest _HTML_Individual_Pages__141001292.txt"

For individual section pages of HTML, we import the DocBook stylesheets
and our small custom stylesheets that set our standard options.

Then we set our chunking options, and tell the web pages where to
find the header and footer graphics.

indexterm:[Stylesheets,chunkit.xsl]
The following code is the entire chunkit style sheet
("chunkit.xsl").

@ascskip on
@ascskip xemacs-xsl-mode-on
@root "doc/chunkit.xsl"
&lt;&lt; HTML: Individual Pages &gt;&gt;
@code
&lt;?xml version='1.0'?&gt; 
&lt;xsl:stylesheet  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  version="1.0"&gt; 

&lt;xsl:import href="chunk.xsl"/&gt;

&lt;xsl:import href="common-links.xsl"/&gt;
&lt;xsl:import href="common-html.xsl"/&gt;

&lt;xsl:param name="navig.graphics" select="1"/&gt;
&lt;xsl:param name=
  "navig.graphics.path"&gt;graphics/&lt;/xsl:param&gt;
    &lt;!--  "navig.graphics.path"&gt;/usr/share/xml/docbook/docbook-xsl-1.59.1/images/&lt;/xsl:param&gt;--&gt;
    &lt;!--&lt;xsl:param name="navig.graphics.path"&gt;graphics/dbook/navicons/&lt;/xsl:param&gt;--&gt;
&lt;xsl:param name="navig.graphics.extension"&gt;.png&lt;/xsl:param&gt;
&lt;xsl:param name="navig.showtitles"&gt;1&lt;/xsl:param&gt;

&lt;xsl:param name="chunk.first.sections" select="1"&gt;&lt;/xsl:param&gt;
&lt;xsl:param name="chunk.section.depth" select="2"&gt;&lt;/xsl:param&gt;
&lt;xsl:param name="section.autolabel" select="0"&gt;&lt;/xsl:param&gt;

&lt;xsl:param name="css.decoration"&gt;1&lt;/xsl:param&gt;

&lt;/xsl:stylesheet&gt;

@doc
@ascskip xemacs-xsl-mode-off
</t>
<t tx="ekr.20040331071919.26">@silent
@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:58 CST 2004  michael@redpriest _HTML_base_css_style_sheet__141160708.txt"

css style sheet

@ascskip on
@ascskip xemacs-css-mode-on
@root "doc/base.css"
&lt;&lt; HTML: base css style sheet &gt;&gt;
@code
/* base from http://www.w3.org/TR/CSS21/sample.html */

address,
blockquote,
body, dd, div,
dl, dt, fieldset, form,
frame, frameset,
h1, h2, h3, h4,
h5, h6, noframes,
ol, p, ul, center,
dir, hr, menu, pre   { display: block }
li              { display: list-item }
head            { display: none }
table           { display: table }
tr              { display: table-row }
thead           { display: table-header-group }
tbody           { display: table-row-group }
tfoot           { display: table-footer-group }
col             { display: table-column }
colgroup        { display: table-column-group }
td, th          { display: table-cell; }
caption         { display: table-caption }
th              { font-weight: bolder; text-align: center }
caption         { text-align: center }
body            { padding: 8px; line-height: 1.12em }
h1              { font-size: 2em; margin: .67em 0 }
h2              { font-size: 1.5em; margin: .75em 0 }
h3              { font-size: 1.17em; margin: .83em 0 }
h4, p,
blockquote, ul,
fieldset, form,
ol, dl, dir,
menu            { margin: 1.12em 0 }
h5              { font-size: .83em; margin: 1.5em 0 }
h6              { font-size: .75em; margin: 1.67em 0 }
h1, h2, h3, h4,
h5, h6, b,
strong          { font-weight: bolder }
blockquote      { margin-left: 40px; margin-right: 40px }
i, cite, em,
var, address    { font-style: italic }
pre, tt, code,
kbd, samp       { font-family: monospace }
pre             { white-space: pre }

/            * comment             */
/* http://www.w3.org/TR/CSS21/visuren.html#propdef-display lists inline-block */
button, textarea,
input, object, 
select, img { display:inline-block; }

big             { font-size: 1.17em }
small, sub, sup { font-size: .83em }
sub             { vertical-align: sub }
sup             { vertical-align: super }
s, strike, del  { text-decoration: line-through }
hr              { border: 1px inset }
ol, ul, dir,
menu, dd        { margin-left: 40px }
ol              { list-style-type: decimal }
ol ul, ul ol,
ul ul, ol ol    { margin-top: 0; margin-bottom: 0 }
u, ins          { text-decoration: underline }
/*br:before       { content: "\A" }*/
center          { text-align: center }

/            * changed             */
/*
abbr, acronym   { font-variant: small-caps; letter-spacing: 0.1em }
*/

:link, :visited { text-decoration: underline }
:focus          { outline: thin dotted invert }

/* Begin bidirectionality settings (do not change) */
BDO[DIR="ltr"]  { direction: ltr; unicode-bidi: bidi-override }
BDO[DIR="rtl"]  { direction: rtl; unicode-bidi: bidi-override }

*[DIR="ltr"]    { direction: ltr; unicode-bidi: embed }
*[DIR="rtl"]    { direction: rtl; unicode-bidi: embed }

@media print {
  h1            { page-break-before: always }
  h1, h2, h3,
  h4, h5, h6    { page-break-after: avoid }
  ul, ol, dl    { page-break-before: avoid }
}



@doc
@ascskip xemacs-css-mode-off
</t>
<t tx="ekr.20040331071919.27">@silent
@doc
@ascskip # Time-stamp: "Wed, Jan 21 09:13 CST 2004  michael@redpriest _HTML_css_style_sheet__140659188.txt"

css style sheet

@ascskip on
@ascskip xemacs-css-mode-on
@root "doc/docstyle.css"
&lt;&lt; HTML: css style sheet &gt;&gt;
@code

html, body {
  background-color: #CCCCCC;
  font-family: "Verdana", arial;
}

body {
  font-size: 9pt;
  line-height: 125%;
/*   margin: 1em; */
  padding: 2em;
  margin-top: 1em;
  margin-left: 3em;
/*   width: 39em; */
  min-height: 60em;
/*   margin-right: 0.5em; */
  background-color: white;
  border-top: 1px solid black;
  border-left: 1px solid black;
/*   border-right: 2px solid black; */
/*   border-bottom: 2px solid black; */
}

.strong {
  font-weight: bold;
}

h1, h2, h3, h4, h5, h6,
p
{
  margin-bottom: 0.5em;
  margin-top: 0.5em;
  line-height: 125%;
}

h1 { font-size: 2em;}
h2 { font-size: 1.4em; }
h3 { font-size: 1.2em; }
h4 { font-size: 1.0em; }
h5 { font-size: 1.0em; }
h6 { font-size: 1.0em; }

h1, h2, h3, h4, h5, h6 {
  color: #660000;
  margin-right: 20%;
}

* &gt; h1 {
  padding-top: 0.5em;
}

/* h2, h3 */
/* { */
/*   margin-right: 10em; */
/* } */

h1.title 
{
  margin-top: 3em;
  border-top: 3px solid #660000;
  border-bottom: 3px solid #660000;
  border-color: #660000;
  padding: .4em;
  text-align: center;
}

h2.title 
{
  margin-top: 3em;
  border-top: 3px solid #660000;
  border-bottom: 3px solid #660000;
  border-color: #660000;
  padding: .4em;
}

div.toc {
    line-height: 100%;
}

div.list-of-examples {
    margin-top: 3em;
}

div.sect1 h2 {
  font-size: 1.5em;
  margin-top: 4em;
  margin-left: 0em;
  margin-right: 25%;
  margin-bottom: 1em;
  /* border-color: #660000; */
  border-top: 0em;
  border-bottom: 1px solid;
  padding: 0em;
}

div.sect2 h3 {
  font-size: 1em;
  margin-top: 4em;
  margin-bottom: 1em;
  margin-right: 25%;
  /* border-color: #660000; */
  border-top: 0em;
  border-bottom: 1px solid;
}

div.sect3 h4 {
  font-size: small;
  color: black;
  margin-top: 4em;
  margin-bottom: 1em;
  margin-right: 25%;
  /* border-color: #660000; */
  border-top: 0em;
  border-bottom: 1px solid;
}

div.note
{
  margin-top: 1em;
  margin-bottom: 1em;
}
div.note .title
{
  color: black;
  font-size: x-small;
  margin-top: 0em;
  margin-bottom: 0em;
}
/* ----- links ---------------------------------------------------------- */
:link {
  color: #660000;
  text-decoration: none;
  font-weight: bold;
}

:visited {
  color: #333333;
  text-decoration: none;
  font-weight: bold;
}


div.toc :link, :visited {
  font-weight: normal;
 }

div.list-of-examples :link, :visited {
  font-weight: normal;
 }


a:link img {border-style: none;}
a:visited img {border-style: none;}

div.toc dd, dl
{
  margin-top: 0em;
  margin-bottom: 0em;
}
div.toc dt
{
  margin-top: 0.2em;
}

ul, ol
{
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}

.para {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}

.sect1,
.toplevel.section
{
  padding-bottom: 0.25em;
}


tt,pre {
    font-family: Courier New,Courier,monospace;
    font-size: smaller;
}

.programlisting {
    margin-top: 8pt;
    margin-bottom: 8pt;
    margin-left: 1em;
    background-color: #FFFFCC;
    white-space: pre;
    border-style: solid;
    border-width: 1pt;
    border-color: #999999;
    padding-left: 6pt;
    padding-top: 2pt;
    padding-bottom: 2pt;
    width: 100%;
    line-height: 100%;
}

table{
    background-color: #FFFFFF;
    width: 99.6%;
}

div.example {
    margin-top: 0pt;
    margin-bottom: 0pt;
    padding-top: 0pt;
    padding-bottom: 0pt;
}

div.example .title {
    color: black;
    margin-top: 0pt;
    margin-bottom: 0pt;
    padding-top: 8pt;
    padding-bottom: 0pt;
}

div.sidebar .title {
  font-weight: bold;
  color: black;
}

div.sidebar  {
  font-size: x-small;
  margin-top: 2em;
  margin-bottom: 0.5em;
  /* margin-left: 1em; */
  margin-right: 33%; 
  padding: 4pt;
  border-top: 1px solid black;
  border-bottom: 1px solid black;
  border-left: 1px solid black;
  border-right: 1px solid black;
}


h1 &gt; a,
h2 &gt; a {
  padding-top: 0.5em;
}

ol.vert, ol.inline {
  list-style-type: none;
  padding-left: 0;
  margin-left: 0;
}

hr, .toc, .title
{ color: #660000 
}


.navfooter
{
  margin-top: 2em;
}
.navheader
{
  margin-bottom: 1em;

}

/* ------ title page ---------------------------------------------------- */
h3.author
{
  padding: 0em;
  margin-top: 0em;
  margin-bottom: -1em;
}

.affiliation
{
  padding: 0em;
  margin-top: 0em;
  margin-bottom: 0em;
  font-size: smaller;
}


div.revhistory table, tr, td
{
  border-collapse: collapse;
  border: hidden;
  font-size: x-small;
 }

div.revhistory table
{
  width: auto;
  }

div.revhistory td[colspan="3"]
{
  padding-left: 2em;  
 }


/* div.draft { */
/*   background-image: url('pics/draft.png'); */
/* } */


@doc
@ascskip xemacs-css-mode-off

</t>
<t tx="ekr.20040331071919.28">@comment &lt;!-- --&gt;
@silent
@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:03 CST 2004  michael@redpriest _HTML_common__140982180.txt"
@ascskip xemacs-xsl-mode-off

indexterm:[Stylesheets,common-html.xsl]
The following section is the entire common-html style sheet
("common-html.xsl"), which sets basic HTML options.

@ascskip on
@ascskip xemacs-xsl-mode-on
@root "doc/common-html.xsl"
&lt;&lt; HTML: common&gt;&gt;
@code
&lt;?xml version='1.0'?&gt; 
&lt;xsl:stylesheet  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  version="1.0"&gt; 
&lt;!--===== ==========================================================--&gt;
&lt;xsl:param name="default.table.width" select="'100%'"&gt;&lt;/xsl:param&gt;
&lt;xsl:param name="html.stylesheet" select="'dbstyle.css'"/&gt;
&lt;xsl:param name="shade.verbatim" select="1"/&gt;
&lt;xsl:attribute-set name="shade.verbatim.style"&gt;
  &lt;xsl:attribute name="border"&gt;0&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="bgcolor"&gt;#F3F3F3&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;


&lt;/xsl:stylesheet&gt;
@doc
@ascskip xemacs-xsl-mode-off
</t>
<t tx="ekr.20040331071919.29">@comment &lt;!-- --&gt;
@silent
@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:03 CST 2004  michael@redpriest _PDF__139549436.txt"

indexterm:[Stylesheets, fo-fop.xsl]
This is the Formatting Objects style sheet ("fo-fop.xsl", which sets
the options for all printed output.

The actual output is a file with the ".fo" extension, which will be
used by a Formatting Object processor to produce a PDF file.

@ascskip on
@ascskip xemacs-xsl-mode-on
@root "doc/fo-fop.xsl"
&lt;&lt; PDF &gt;&gt;
@code
&lt;?xml version='1.0'?&gt; 
&lt;xsl:stylesheet  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  version="1.0"&gt; 
&lt;!--===== ==========================================================--&gt;

&lt;!--===== catalog will convert the url to our file location =========--&gt;
&lt;xsl:import href="fo-docbook.xsl"/&gt;
&lt;xsl:import href="common-links.xsl"/&gt;

&lt;!--===== using the fop pdf processor ===================================--&gt;
&lt;xsl:param name="fop.extensions" select="1"/&gt;

&lt;!--===== single sided pages ============================================--&gt;
&lt;xsl:param name="double.sided" select="0"&gt;&lt;/xsl:param&gt;

&lt;!--===== body print ====================================================--&gt;
&lt;xsl:param name="body.font.master"&gt;12&lt;/xsl:param&gt;
&lt;xsl:param name="alignment"&gt;left&lt;/xsl:param&gt;
&lt;xsl:param name="hyphenate"&gt;true&lt;/xsl:param&gt;

&lt;!--===== set page margins ==============================================--&gt;
&lt;xsl:param name="page.margin.inner"&gt;
  &lt;xsl:choose&gt;
    &lt;xsl:when test="$double.sided != 0"&gt;1.25in&lt;/xsl:when&gt;
    &lt;xsl:otherwise&gt;1.5in&lt;/xsl:otherwise&gt;
  &lt;/xsl:choose&gt;
&lt;/xsl:param&gt;

&lt;xsl:param name="body.margin.top" select="'.75in'"&gt;&lt;/xsl:param&gt;

&lt;!--===== set title fonts ===============================================
     Title fonts require replacing the standard
     titlepage.templates.xsl with a custom version.  This is done
     here by copying the fo/titlepage.templates.xml to
     mrc.titlepage.templates.xsl, editing it, and then processing it
     with
      xsltproc -output mrc.titlepage.templates.xsl \
         /usr/share/xml/docbook/docbook-xsl-1.60.1/template/titlepage.xsl  \
         mrc.titlepage.templates.xml
     Now we replace the old titlepage.templates.xsl with our new
     mrc.titlepage.templates.xsl
--&gt;
&lt;xsl:include href="mrc.titlepage.templates.xsl"/&gt;

&lt;!--===== blank verso titlepage =========================================--&gt;
&lt;xsl:template name="book.titlepage.verso"/&gt;

&lt;!--===== outdent titles ================================================--&gt;
&lt;xsl:param name="title.margin.left" select="'-2pc'"/&gt;

&lt;!--===== set section font, break ======================================--&gt;
&lt;xsl:attribute-set name="section.title.level1.properties"&gt;
  &lt;xsl:attribute name="font-size"&gt;14pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="break-before"&gt;page&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="border-bottom"&gt;1pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="border-bottom-style"&gt;solid&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="border-bottom-color"&gt;black&lt;/xsl:attribute&gt;  
  &lt;xsl:attribute name="margin-right"&gt;6em&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;
&lt;xsl:attribute-set name="section.title.level2.properties"&gt;
  &lt;xsl:attribute name="break-before"&gt;page&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;
&lt;xsl:attribute-set name="section.title.level3.properties"&gt;
  &lt;xsl:attribute name="break-before"&gt;page&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;

&lt;!--===== Code extract titles are sidebars ==============================--&gt;
&lt;xsl:attribute-set name="sidebar.properties" use-attribute-sets="formal.object.properties"&gt;
  &lt;xsl:attribute name="border-style"&gt;solid&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="border-width"&gt;1pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="border-color"&gt;black&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="background-color"&gt;#EDEDED&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="padding-left"&gt;12pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="padding-right"&gt;12pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="padding-top"&gt;2pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="padding-bottom"&gt;4pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="margin-left"&gt;0pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="margin-right"&gt;4em&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="margin-top"&gt;2pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="margin-bottom"&gt;2pt&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;
&lt;!--===== code (verbatim) font and spacing ==============================--&gt;
&lt;xsl:attribute-set name="verbatim.properties"&gt;
  &lt;xsl:attribute name="space-before.minimum"&gt;0.1pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="space-before.optimum"&gt;2pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="space-before.maximum"&gt;3pt&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="space-after.minimum"&gt;0.4em&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="space-after.optimum"&gt;.5em&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="space-after.maximum"&gt;1.2em&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;
&lt;xsl:attribute-set name="monospace.verbatim.properties"
    use-attribute-sets="verbatim.properties monospace.properties"&gt;
  &lt;xsl:attribute name="text-align"&gt;start&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="font-size"&gt;9pt&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;
    &lt;!--===== 2003-Oct-01 FOP does not appear to support shade.verbatim yet =--&gt;
&lt;xsl:param name="shade.verbatim" select="1"/&gt;
&lt;xsl:attribute-set name="shade.verbatim.style"&gt;
  &lt;xsl:attribute name="border"&gt;1&lt;/xsl:attribute&gt;
  &lt;xsl:attribute name="bgcolor"&gt;#E0E0E0&lt;/xsl:attribute&gt;
&lt;/xsl:attribute-set&gt;

    &lt;!--===== FOP did not like this =========================================--&gt;
&lt;!--&lt;xsl:attribute-set name="xref.properties"&gt;--&gt;
&lt;!--  &lt;xsl:attribute name="font-size"&gt;14pt&lt;/xsl:attribute&gt;--&gt;
&lt;!--  &lt;xsl:attribute name="font-style"&gt;bold&lt;/xsl:attribute&gt;--&gt;
&lt;!--&lt;/xsl:attribute-set&gt;--&gt;

&lt;/xsl:stylesheet&gt;

@doc
@ascskip xemacs-xsl-mode-off




</t>
<t tx="ekr.20040331071919.30">@language plain
@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:21 CST 2004  michael@redpriest Appendix_XEmacs_Text_Editor_140657924.txt"

You can use Leo to enter all the text in an outline, but Leo also
allows you to use your familiar editing environment.  In my case,
that is XEmacs.  Fortunately, Leo integrates with XEmacs quite well.

The following items are code I use, some Leo Python plugins and some
XEmacs elisp functions.  You may find them useful.

@ascskip on
&lt;&lt; Appendix: XEmacs Text Editor &gt;&gt;
@code</t>
<t tx="ekr.20040331071919.31">@language python
@tabwidth -4

@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:10 CST 2004  michael@redpriest _OpenWith_Plugin__140659092.py"

Leo's Open_With plugin can be modified so that the body text of any
outline node can be edited in XEmacs by choosing "File; OpenWith;
XEmacs" or "File; OpenWith; XEmacs - noshow"  from the menu.

What actually happens is that Leo places the text in a temporary
file, and calls XEmacs with the address of that temporary file.  Leo
then watches for changes in the temporary file.  When and if the
temporary file changes, Leo copies the contents to the body text of
the Leo node.
      
Below is the standard open_with.py plugin that came with Leo 4.1-rc3
The only modification I've made is to insert
@code
&lt;&lt;call XEmacs&gt;&gt;=
table = (
    ("X&amp;Emacs", "Alt+Shift+O", ("os.system","/usr/bin/gnuclient -q ", None)),
    ("X&amp;Emacs - noshow", "Ctrl+Shift+O", ("os.system","/mrc2/linux-bin/gnuclient-noshow ", None))
    )
@doc
as noted below.  A similar alteration should work for future
versions.

Note: this alteration is for XEmacs running under Linux, but a
similar command should work in the Windows environment.

I use the "gnuclient-noshow" selection to load the temporary open_with file in
the background.  It is a small bash shell script:
---
#!/bin/bash
gnuclient -eval "(find-file-noselect \"${1}\")"
---

To implement this, edit a copy of the open_with.py file that comes
with your version of Leo.  Move the original copy to a safe place,
and put your edited copy in the Leo plugins directory.  Check to see
it is included in "pluginsManager.txt" in that directory.
@ascskip on
@root "other/xemacs/open_with.py"
&lt;&lt; Open_With Plugin&gt;&gt;
@code
"""Create menu for Open With command and handle the resulting commands"""

import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

import os

if Tk: # Register the handlers...

    def on_idle (tag,keywords):
        a = g.app
        if g.app.killed: return
        for dict in a.openWithFiles:
            path = dict.get("path")
            c = dict.get("c")
            encoding = dict.get("encoding",None)
            v = dict.get("v")
            old_body = dict.get("body")
            if path and os.path.exists(path):
                try:
                    time = os.path.getmtime(path)
                    if time and time != dict.get("time"):
                        dict["time"] = time # inhibit endless dialog loop.
                        # The file has changed.
                        try:
                            # Update v from the changed temp file.
                            f=open(path)
                            s=f.read()
                            f.close()
                        except:
                            g.es("can not open " + g.shortFileName(path))
                            break
                        
                        # Convert body and s to whatever encoding is in effect.
                        body = v.bodyString()
                        body = g.toEncodedString(body,encoding,reportErrors=True)
                        s = g.toEncodedString(s,encoding,reportErrors=True) # 10/13/03
                        
                        conflict = body != old_body and body != s
                        
                        # Set update if we should update the outline from the file.
                        if conflict:
                            # See how the user wants to resolve the conflict.
                            g.es("conflict in " + g.shortFileName(path),color="red")
                            message = "Replace changed outline with external changes?"
                            result = g.app.gui.runAskYesNoDialog(c,"Conflict!",message)
                            update = result.lower() == "yes"
                        else:
                            update = s != body
                        
                        if update:
                            g.es("updated from: " + g.shortFileName(path),color="blue")
                            c.setBodyString(v,s,encoding)
                            c.selectVnode(v)
                            dict["body"] = s
                        elif conflict:
                            g.es("not updated from: " + g.shortFileName(path),color="blue")
                except:
                    g.es_exception() ## testing
                    pass
    def create_open_with_menu (tag,keywords):
    
        if  (tag in ("start2","open2") or
            (tag=="command2" and keywords.get("label")=="new")):
    
            # Entries in the following table are the tuple 
            # (commandName,shortcut,data).
            # 
            # - data is the tuple (command,arg,ext).
            # - command is one of "os.system", "os.startfile", "os.spawnl", 
            # "os.spawnv" or "exec".
            # 
            # Leo executes command(arg+path) where path is the full path to 
            # the temp file.
            # If ext is not None, the temp file has the extension ext,
            # Otherwise, Leo computes an extension based on what @language 
            # directive is in effect.
            
            idle_arg = "c:/python22/tools/idle/idle.py -e "
            
@doc
Here is where we insert the &lt; Call XEmacs &gt; code fragment defined above:
@code
            if 1: # Default table.


&lt;&lt; Call XEmacs &gt;&gt;
#               table = (
#                   # Opening idle this way doesn't work so well.
#                   # ("&amp;Idle",   "Alt+Shift+I",("os.system",idle_arg,".py")),
#                   ("&amp;Word",   "Alt+Shift+W",("os.startfile",None,".doc")),
#                   ("Word&amp;Pad","Alt+Shift+T",("os.startfile",None,".txt")))
#           elif 1: # Test table.
#               table = ("&amp;Word","Alt+Shift+W",("os.startfile",None,".doc")),
#           else: # David McNab's table.
#               table = ("X&amp;Emacs", "Ctrl+E", ("os.spawnl","/usr/bin/gnuclient", None)),
            
            c.frame.menu.createOpenWithMenuFromTable(table)

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":

        g.app.hasOpenWithMenu = True
        leoPlugins.registerHandler("idle", on_idle)
        leoPlugins.registerHandler(("start2","open2","command2"), create_open_with_menu)
    
        __version__ = "1.4" # Set version for the plugin handler.
        g.plugin_signon(__name__)

</t>
<t tx="ekr.20040331071919.32">@language python
@tabwidth-4
@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:14 CST 2004  michael@redpriest _OpenTree_Plugin__140660268.py"

This is a module that creates an "Open With" menu item that opens
Leo outline nodes in the tree below the current Leo node in the
XEmacs editor.I frequently have a small tree of Leo nodes which
contain code that is usually edited in the same session.

NOTE: I use the "gnuclient-noshow" selection to load the temporary
open_with file in the background.Leo calls a command with the
temporary file name at the end of the command, but the gnuclient
command needs to receive it enclosed in quotes and parentheses.The
solution is a small intermediary bash shell script called
"gnuclient-noshow":

- - -
#!/bin/bash
gnuclient- eval "(find-file-noselect \"${1}\")"
- - -

I would rather have this operate in the background, but Leo ' s
openWith always operates on the current node, and openWith has much
good error checking that I want to use.So the fast solution was to
have OpenTreeInXEmacs visibly traverse the tree.

@ascskip on
@root "other/xemacs/mod_xemacsopentree.py"
&lt;&lt; Open_Tree Plugin &gt;&gt;
@code

import leoPlugins

def OpenTreeInXEmacs (c):
    import leoCommands
    #XEmacsCommand = "/usr/bin/gnuclient -q "
    XEmacsCommand = "/mrc2/linux-bin/gnuclient-noshow "
    vnode = c.currentVnode() # get the current vnode.
    stopHere = vnode.nodeAfterTree()
    v = vnode
    while v != stopHere:
        c.openWith(data=("os.system",XEmacsCommand,None))
        v = v.threadNext()
        if (not v) or (v==stopHere):
            break
        c.selectVnode(v)
    c.selectVnode(vnode)


def CreateOpenTreeMenu (tag,keywords):

    """Create the 'Xemacs: Open Tree' menu item in the Open With menu."""


    if (tag=="open2" or
        (tag=="start2") or
        (tag=="command2" and keywords.get("label")=="new")):

        c = keyword.get('c')
        exportMenu = c.frame.menu.getMenu('Open With')
        newEntries = (
            ("-",None,None),
            ("XEmacs: Open nodes in sub-tree","None",OpenTreeInXEmacs),
        )
        c.frame.menu.createMenuEntries(exportMenu,newEntries,dynamicMenu=True)

if 1:
    leoPlugins.registerHandler(("start2","open2","command2"),CreateOpenTreeMenu)

    __version__ = ".4" # Set version for the plugin handler.
    g.plugin_signon(__name__)
@doc


@code
</t>
<t tx="ekr.20040331071919.33">@language python
@tabwidth -4
@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:15 CST 2004  michael@redpriest _Filename_modification__140661308.py"

This is a small modification to Leo (via a Python plugin module) so
that Leo will open the temporary files with a name that can be
easily recognized in an XEmacs buffer listing.

On Linux, Leo opens files in the temporary files directory, all
prefixed with "LeoTemp_", which makes the names difficult to tell
apart when you have many different nodes loaded in XEmacs.

This code replaces the openWithTempFilePath method of the LeoFrame
class with code that opens temporary files in a subdirectory of the
temporary files directory, called "username_Leo", and omits the
"LeoTemp" prefix.

For example, I'm now editing this Leo node in XEmacs as
    "/tmp/michael_Leo/_Filename_modification__138976348.py"
In the XEmacs buffer list, the filename is shown as
    "_Filename_modification__138976348.py"
and all the Leo buffer names start with a leading underscore, so
they are grouped together.

For general use, this code should be considerably more robust about
creating the Leo subdirectory and signaling errors, but it is just a
quick hack that works for me on my machines.

This is distributed with Leo version 4.1rc3, so I've updated it with
Ed Ream's modifications to match that distribution.

@ascskip on
@root "other/xemacs/mod_tempfname.py"
&lt;&lt; Filename modification &gt;&gt;
@code

"""Replace Commands.openWithTempFilePath so Leo opens temporary
files with a filename that begins with the headline text, and
located in a 'username_Leo' subdirectory of the temporary
directory. The 'LeoTemp' prefix is omitted.  This makes it easier to
see which temporary file is related to which outline node.""" #'

import leoGlobals as g
import leoPlugins

import leoCommands
import getpass
import os
import tempfile

def onStart (tag,keywords):

    # g.trace("replacing openWithTempFilePath")

    g.funcToMethod(openWithTempFilePath,leoCommands.Commands,"openWithTempFilePath")

def openWithTempFilePath (self,v,ext):

    """Return the path to the temp file corresponding to v and ext.

    Replaces the Commands method."""    

    try:
        leoTempDir = getpass.getuser() + "_" + "Leo"
    except:
        leoTempDir = "LeoTemp"
        g.es("Could not retrieve your user name.")
        g.es("Temporary files will be stored in: %s" % leoTempDir)

    td = os.path.join(os.path.abspath(tempfile.gettempdir()), leoTempDir)
    if not os.path.exists(td):
        os.mkdir(td)

    name = g.sanitize_filename(v.headString()) + '_' + str(id(v.t))  + ext
    path = os.path.join(td,name)
    return path

# Register the handlers...
leoPlugins.registerHandler("start2", onStart)

__version__ = "1.3"
g.plugin_signon(__name__)
</t>
<t tx="ekr.20040331071919.34">@language plain
@silent
@doc
@ascskip # Time-stamp: "Tue, Jan 13 09:58 CST 2004  michael@redpriest _Kill_Temporary_Buffers__140661388.txt"

If you've opened a number of Leo temporary buffers in XEmacs, this
XEmacs function will kill them for you.  Just set the tempdir
variable to whatever matches your local value.

XEmacs will prompt you about any buffers that have unsaved changes.

@ascskip on
@ascskip xemacs-lisp-mode-on
@root "other/xemacs/kill-temporary-buffers.el"
&lt;&lt; Kill Temporary Buffers &gt;&gt;
@code
;;
;;-     mwd-leo-kill-buffers
(defun mwd-leo-kill-buffers ()
  "Kill any buffers for files in my Leo temporary directory."
  (interactive)
  (let ((bl (buffer-list))
        (tempdir "/tmp/michael_Leo" )  ;; change this to your temporary directory.
        )
    (while bl
      (setq test-buffer (car bl))
      (setq bname (buffer-file-name test-buffer))
      (if (and bname (string-match tempdir bname))
          (kill-buffer test-buffer)
        )
      (setq bl (cdr bl))
      )
    )
  )



@doc
@ascskip xemacs-lisp-mode-off
</t>
<t tx="ekr.20040331071919.35">@language plain
@silent
@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:18 CST 2004  michael@redpriest _MMMmode__140663340.txt"

There is an editing mode for XEmacs called Multiple Major Modes,
which allows us to edit the temporary text conveniently: with all
the syntax highlighting, special keymaps, etc. available, even
though Leo nodes may contain both plain text and program code.

When the XEmacs cursor is in a section of plain text, all the plain
text facilities are available, and there is no syntax
highlighting. When the XEmacs cursor is in a section of code
(Python, XSL, whatever) XEmacs invokes the syntax highlighting,
special keymaps, etc. appropriate for that code.

indexterm:[Multiple Major Modes]
indexterm:[Multiple Major Modes,mmm-mode.el]
If you have XEmacs installed, and you have also installed the
Multiple Major Modes mmm-mode.el package, the following code will
customize mmm-mode for use while editing Leo temporary files.

NOTE: mmm-mode is already installed by default in most
distributions.

Installation: Load mmm-leo-config.el from your .init.el file, or
just load it manually to try it out.

I won't go through it all, but for example, when editing a temporary
Leo file that is in XEmacs Python mode, and/or has a ".py" suffix:

    - when your cursor is any text between the @doc and @code
      directives XEmacs will enter text-mode.  Otherwise (e.g. with
      the cursor after the @code directive), XEmacs will be in
      Python mode.
    - when your cursor is between text that says
      "xemacs -makefile-mode-on" and text that says
      "xemacs -makefile-mode-off", XEmacs will enter makefile-mode.
      (You key in those text markers to mark out the area you want
      as makefile-mode.  See the Leo2AsciiDoc.leo outline for examples,
      e.g the "Make File" section in the Leo2AsciiDoc Users Guide.)

      Otherwise, XEmacs will be in Python mode in that buffer.

Similarly, makefile-mode, xsl-mode and emacs-lisp-mode are added to
temporary Leo files that created with a ".txt" extension.      

A future project may be to create a Leo module to use in the
Leo "openWith" function that examines each node for these mmm-mode
markers and creates the temporary file with the proper extension.

@ascskip on
@ascskip xemacs-lisp-mode-on
@root "other/xemacs/mmm-leo-config.el"
&lt;&lt; MMM-mode &gt;&gt;
@code
;;-     mmm-mode                multiple modes
(require 'mmm-auto)
(require 'mmm-vars)

;   mmm-mode-on and mmm-mode-off turn it on and off in a buffer.
;   \c-c % \c-b re-parses the whole buffer

;   set mode to activate on mode or extension
(setq mmm-global-mode 'maybe)

; turn off gray background
(setq mmm-submode-decoration-level 0)

;   add embedded modes in python
(mmm-add-group
 'py-embedded-text
 '(
   (py-leo
    :submode text-mode
    :face mmm-code-submode-face
    :front "^@doc.*"
    :back "^@code"
    :insert ((?l py-leo-tag nil @ "@doc"
                 @ "\n\n" _ "\n\n" @ "@code" @))
    ; \c % l will insert the doc-code pair at point.
    )
   (py-doc
    :submode text-mode
    :face mmm-code-submode-face
    :front "^\"\"\".*"
    :back "^.+\"\"\""
    )
   (py-makefile
    :submode makefile-mode
    :face mmm-code-submode-face
    :front "xemacs-makefile-mode-on"
    :back "xemacs-makefile-mode-off"
    )
   )
 )
;   add embedded modes in text
(mmm-add-group
 'text-embedded
 '(
   (txt-makefile-mode
    :submode makefile-mode
    :face mmm-code-submode-face
    :front "xemacs-makefile-mode-on"
    :back "xemacs-makefile-mode-off"
    :insert ((?l text-embedded-tag nil @ "@doc"
                 @ "\n\n" _ "\n\n" @ "@code" @))
    ; \c % l will insert the doc-code pair at point.
    )
   (txt-xsl-mode
    :submode xsl-mode
    :face mmm-code-submode-face
    :front "xemacs-xsl-mode-on"
    :back "xemacs-xsl-mode-off"
    :insert ((?l text-embedded-tag nil @ "@doc"
                 @ "\n\n" _ "\n\n" @ "@code" @))
    ; \c % l will insert the doc-code pair at point.
    )
   (txt-lisp-mode
    :submode emacs-lisp-mode
    :face mmm-code-submode-face
    :front "xemacs-lisp-mode-on"
    :back "xemacs-lisp-mode-off"
    :insert ((?l text-embedded-tag nil @ "@doc"
                 @ "\n\n" _ "\n\n" @ "@code" @))
    ; \c % l will insert the doc-code pair at point.
    )
   )
 )
(mmm-add-mode-ext-class 'python-mode "\\.py\\'" 'py-embedded-text)
(mmm-add-mode-ext-class 'text-mode "\\.txt\\'" 'text-embedded)

@doc
@ascskip xemacs-lisp-mode-off
</t>
<t tx="ekr.20040331071919.36">@language plain
@silent
@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:20 CST 2004  michael@redpriest _Insert_indexterm__140664580.txt"

indexterm:[XEmacs, Indexing]
Indexing is tedious work, and it interferes with the readability of
the ascii text as well.  However, used sparingly, it helps the
reader.

When editing a Leo node (in an XEmacs buffer), this function copies
a highlighted word or phrase and inserts an AsciiDoc index code on a
new line immediately before the paragraph.  I try to keep markup out
of the way of the reader.  In this case, AsciiDoc requires that the
index code be part of the same block of text, and the first line of
the block is the least annoying place I can find.

For example, if I wanted to index the words "XEmacs buffer" above, I
would highlight them (usually by pressing M-@ a couple of times) and
then call this function (I have it bound to C-k C-h C-i).  At the
beginning of the paragraph, my text would say "\indexterm:[XEmacs
buffer]".

@ascskip on
@ascskip xemacs-lisp-mode-on
@root "other/xemacs/index-leo-region.el"
&lt;&lt; Insert indexterm &gt;&gt;
@code
(defun mwd-index-leo-region (start end)
  "preface paragraph with AsciiDoc index macro of region."
  (interactive "r")
  (save-excursion
    (copy-region-as-kill start end)
    (backward-paragraph)
    (insert "\nindexterm:[")
    (yank)
    (insert "]")
    )
  )

@doc
@ascskip xemacs-lisp-mode-off

</t>
<t tx="ekr.20040331071919.37">@language plain
@silent
@doc
@ascskip # Time-stamp: "Tue, Jan 13 10:56 CST 2004  michael@redpriest _Indent_Leo_comments__141202716.txt"

Leo derived files are sprinkled with comments, which Leo uses as
markers to be able to "untangle" files, i.e. import changes made to
a derived file back into the Leo outline.

Useful as they may be, the comments are an ugly distraction when
reading the source code.  One could have XEmacs flush them from the
file, but then the untangle feature is gone for that file.

This pair of XEmacs elisp functions moves them to the right, where
they aren't so distracting, and moves them back again if you should
want to untangle the file.

@ascskip on
@ascskip xemacs-lisp-mode-on
@root "other/xemacs/indent-leo-comments.el"
&lt;&lt; Indent Leo comments &gt;&gt;
@code
(defun mwd-leo-comments-indent ()
  "Indent Leo comments to make them less distracting."
  (interactive)
  (save-excursion
    (let* (
          (leading-spaces 40)
          (start-string (concat (make-string leading-spaces ? ) "\\1" ))
          (end-string (concat (make-string leading-spaces ? ) "\\1" ))
          )
      (goto-char (point-min))
      (while (search-forward-regexp "\\(^# &lt;&lt;\\)" nil t) (replace-match start-string))
      (goto-char (point-min))
      (while (search-forward-regexp "\\(^# -- end\\)" nil t) (replace-match end-string))
      )
    )
  )

(defun mwd-leo-comments-unindent ()
  "Reverse the effect of mwd-leo-comments-indent."
  (interactive)
  (save-excursion
      (goto-char (point-min))
      (while (search-forward-regexp "^\\(\\s-\\)+\\(# &lt;&lt;\\)" nil t) (replace-match "\\2" ))
      (goto-char (point-min))
      (while (search-forward-regexp "^\\(\\s-\\)+\\(# -- end\\)" nil t) (replace-match "\\2" ))
    )
  )
@doc
@ascskip xemacs-lisp-mode-off
</t>
<t tx="ekr.20040331071919.38">@language plain
@ascfile "doc/mod_asc_user.asc"
@ascconfig maxCodeLineLength 80
@doc
@ascskip # Time-stamp: "Mon, Jan 19 15:29 CST 2004  michael@redpriest Leo_AsciiDoc_Users_Guide_141652036.txt"

Preface
-------

Leo2AsciiDoc is a small Python program which has been
built to be used as a plugin module for the Leo outlining editor.

Leo2AsciiDoc enables the contents of Leo outlines to be published to HTML
or PDF via the DocBook set of publishing tools.  Plain text from the
Leo outline is transformed into a final result that has:

    - typeset body text, in which bulleted and numbered lists,
      variable lists, page numbers, URLs, index terms,and bold and
      italic text are automatically recognized.
    - typeset Headings
    - a Table of Contents
    - an Index containing any items marked by the user, and any
      Python classes or functions.

As you will see, there's not a lot involved in using the
Leo2AsciiDoc module.  It simply copies text from a Leo outline (or a
portion of a Leo outline) to a text file.  In turn that text file can
be automatically converted by the AsciiDoc program and a DocBook
system to properly typeset DocBook HTML, PDF or other formats.

If you keep your text plain, and use a few simple formatting
conventions, the final output can have typeset headings, bulleted
lists, indexing and cross-referencing, as well as many other
features.

---
Michael Dawson
Marshall Research
michael_dawson at marshallresearch dot com
---

*note*

Leo2AsciiDoc is suited for general text documents, most programming
documentation and most business documents.  Leo2AsciiDoc (being based on
DocBook) is not the choice for anyone needing detailed typographic
control of individual words or characters -- for example, typeset
equations.  In general, DocBook typesets blocks of text.

*note*

@code
</t>
<t tx="ekr.20040331071919.39">@doc
@ascskip # Time-stamp: "Mon, Jan 19 11:48 CST 2004  michael@redpriest Installation_140689076.txt"
Installation of this plugin is very straightforward, using Leo
version 4.1:

    - copy the python source code (mod_leo2ascd.py) to your Leo
      plugin directory (a subdirectory called "plugins" under your
      main Leo directory).
    - in that directory should be a text file called
      pluginsManager.txt, containing a list of all plugins that are
      to be loaded when Leo starts.  Add mod_leo2ascd.py to the
      list.
    - start or re-start Leo.
    - in the Leo Log Window you should see the Leo2AsciiDoc sign-on
      message "---mod_leo2asc 0.4-------".
    - in the Leo main menu "File; Export", there should be two menu
      items called something like "Export to AsciiDoc".

@code</t>
<t tx="ekr.20040331071919.40">@language plain
@doc
@ascskip # Time-stamp: "Thu, Oct 16 13:46 CST 2003  michael@redpriest Operation_140791428.txt"

Using Leo2AsciiDoc is as simple as choosing the Leo menu item: "File;
Export; Export All to AsciiDoc".  From there, you have the AsciiDoc
program and the DocBook system automatically convert your outline to
HTML or PDF (or to a manpage or a DocBook website.)

Step by step:

    - You need a Leo outline containing some plain text, or plain
      text and code.
    - You ensure that the top node in the outline (or part of the
      outline tree which you want to be a separate document) must
      have an @ascfile directive in the body text. The @ascfile
      directive is used to specify the filename in which the output
      text will be put.
    - You then use Leo's menu: "File; Export; Export All to
      AsciiDoc" (or one of the other Leo2AsciiDoc menu items) to
      have Leo2AsciiDoc automatically export the outline to a text file.
    - After that, you run the AsciiDoc program on the exported text
      file, and process it as a DocBook document.  Most often,
      people have a Make file set up to do this automatically.

In practice, people often want to use special features:

    - plain text formatting, sometimes referred to as "structured
      text" or "minimal markup"
    - Leo2AsciiDoc configuration options

The following sections cover this.  If you've downloaded the Leo2AsciiDoc
package, the mod_leo2asc.leo outline is available, and illustrates
all the features.  It is the outline from which all the Leo2AsciiDoc HTML
and PDF documentation and code were derived.

@code
</t>
<t tx="ekr.20040331071919.41">@doc
@ascskip # Time-stamp: "Mon, Jan 19 13:19 CST 2004  michael@redpriest Directives_140672364.txt"

The following are non-printing directives that you can insert into
your outline text to control Leo2AsciiDoc behaviour.  All must be at the
beginning of the line.

{amp}commat;ascfile::
    e.g: `@ascfile "doc/mod_asc_user.asc" `

    Ascfile is the equivalent of a Leo @root directive. Ascfile
    signals the start of a document and specifies the file name to
    receive the text.

    The default directory is the directory containing the Leo
    outline.  If you were editing an outline that resided in
    /home/me then the above ascfile directive would create the file
    mod_asc/user.asc in the directory /home/me/doc.

{amp}commat;ascignore::
    Ascignore causes Leo2AsciiDoc to ignore the outline node, and any
    sub-nodes. It must be placed before any line in the node which
    will print.

{amp}commat;ascskip::
    Causes Leo2AsciiDoc to skip the line.  If followed by the word "on",
    causes Leo2AsciiDoc to skip all succeeding document lines until an
    "{amp}commat;ascskip off" directive is read, or a code section is reached.

{amp}commat;ascexit::
    Causes Leo2AsciiDoc to exit the outline node without processing any
    further lines.  Sub-nodes will be processed.

{amp}commat;ascconfig::
    e.g. `{amp}commat;ascconfig maxCodeLineLength 70` -- see
    Configuration below. 
    

@code
</t>
<t tx="ekr.20040331071919.42">@doc
@ascskip # Time-stamp: "Mon, Jan 19 13:20 CST 2004  michael@redpriest Configuration_140673612.txt"

There are a few configuration settings which may be set in an
outline.  To take effect, they must be placed:

    - in the top node of the outline, or
    - the same node as an @ascfile directive.
    
Configuration settings in the top node of the outline are effective
for the whole outline, unless overridden by settings in sub-nodes.

maxCodeLineLength::
    e.g. `{amp}commat;ascconfig maxCodeLineLength 70` -- 
    sets the maximum length of code printout lines to 70 characters.
    Longer lines will be wrapped and a line continuation character
    displayed.

PrintHeadings::    
    e.g. `{amp}commat;ascconfig PrintHeadings off` -- turns off the
    export of outline node headings as section titles.  In that
    case, you must have correctly entered AsciiDoc section titles in
    the body text of your outline.

Readers of the code will note that there are other configuration
settings in the code. These will be used in future, and so I won't
document them yet.


@code</t>
<t tx="ekr.20040331071919.43">@language plain
@doc
@ascskip # Time-stamp: "Mon, Jan 19 13:22 CST 2004  michael@redpriest Markup_140672220.txt"

The point of using a system like AsciiDoc is to get a document that
is properly typeset, while writing only plain text with as little
embedded formatting instruction as possible.

For the most part, you simply write chunks of text, which become
typeset paragraphs.

I've tried to use most commonly used markup in the Leo outline that
contains all the Leo2AsciiDoc source and documentation, so that you
can see exactly how markup may be used.

@code</t>
<t tx="ekr.20040331071919.44">@doc
@ascskip # Time-stamp: "Mon, Jan 19 13:20 CST 2004  michael@redpriest Standard_AsciiDoc_Markup_140676540.txt"

This section illustrates a very small part of the standard AsciiDoc
markup.  However, AsciiDoc comes with extensive documentation of its
own, which any Leo2AsciiDoc user should read.


@code</t>
<t tx="ekr.20040331071919.45">@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:06 CST 2004  michael@redpriest Headings_141020668.txt"

indexterm:[Markup, Headings]
Leo2AsciiDoc will automatically create Headings from the headings of
your Leo outline.  You can turn this off (see Configuration), and
create your own headings in the body text of an outline node.  For
example, a Chapter heading is text at the left margin that has a
following line of dashes.  For example,

@code
 Operation
 ---------

@doc
is the heading of this chapter.  Chapter sub-sections have a
following line of tildes.  For example,

@code

 Markup
 ~~~~~~

@doc

is the heading of Section One of this chapter.  Section Two markup
is a following line of "^".  For example, 

@code

Standard AsciiDoc Markup
^^^^^^^^^^^^^^^^^^^^^^^^
@doc

is the heading of the section, which is a Section Two.

As I say, you normally don't need to do this, since Leo2AsciiDoc does all
this itself from the outline headings.


@code
</t>
<t tx="ekr.20040331071919.46">@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:06 CST 2004  michael@redpriest Lists_141018612.txt"

indexterm:[Markup, lists]
Bulleted lists start with a dash (or asterisk) followed by a space
or tab character.  I've extended this to allow leading spaces.  For
example,
    
@code
    - this is a list item
        * this is a sub-item
    - this is another list item
@doc

produces:

    - this is a list item
        * this is a sub-item
    - this is another list item


@code</t>
<t tx="ekr.20040331071919.47">@doc
@ascskip # Time-stamp: "Thu, Jan  8 14:07 CST 2004  michael@redpriest URLs_140994492.txt"

indexterm:[Markup, URL]
The URL address of a web page will be "hot" in the HTML or PDF
document, when terminated with square brackets:

@code

http://www.docbook.org[The official home page for DocBook: The Definitive  Guide.]

@doc

results in:

http://www.docbook.org[The official home page for DocBook: The Definitive Guide.]


@code</t>
<t tx="ekr.20040422072343">"""Create a context menu when right-clicking in the body pane."""

# Send bug reports to
# http://sourceforge.net/forum/forum.php?thread_id=980723&amp;forum_id=10228

&lt;&lt; version history &gt;&gt;
&lt;&lt; imports &gt;&gt;
__version__ = "0.10"

@others</t>
<t tx="ekr.20040422072343.1">def rc_help(c):
    
    """Highlight txt then rclick for python help() builtin."""
    
    if c.frame.body.hasTextSelection():

        newSel = c.frame.body.getSelectedText()

        # EKR: nothing bad happens if the status line does not exist.
        c.frame.clearStatusLine()
        c.frame.putStatusLine(' Help for '+newSel) 
    
        # Redirect stdout to a "file like object".
        sys.stdout = fo = g.fileLikeObject()
    
        # Python's builtin help function writes to stdout.
        help(str(newSel))
        
        # Restore original stdout.
        sys.stdout = sys.__stdout__

        # Print what was written to fo.
        s = fo.get() ; g.es(s) ; print s</t>
<t tx="ekr.20040422072343.2">def rc_dbody(c):

    if c.frame.body.hasTextSelection():
        c.frame.body.deleteTextSelection()
        c.frame.body.onBodyChanged("Delete")</t>
<t tx="ekr.20040422072343.3">def rc_nl(c):
    
    """Insert a newline at the current curser position."""

    c.frame.body.insertAtInsertPoint('\n')
    c.frame.body.onBodyChanged("Typing")</t>
<t tx="ekr.20040422072343.4">def rc_selectAll(c):
    
    """Select the entire log pane."""
    
    g.app.gui.setTextSelection(c.frame.log.logCtrl,"1.0","end")</t>
<t tx="ekr.20040422072343.5">def rClickbinder(tag,keywords):

    c = keywords.get('c')
    
    if c and c.exists:
        c.frame.log.logCtrl.bind  ('&lt;Button-3&gt;',c.frame.OnBodyRClick)
        # c.frame.body.bodyCtrl.bind('&lt;Button-3&gt;',c.frame.OnBodyRClick)</t>
<t tx="ekr.20040422072343.6"># EKR: it is not necessary to catch exceptions or to return "break".

def rClicker(tag,keywords):
    
    c = keywords.get("c")
    e = keywords.get("event")
    if not c or not c.exists or not e: return

    e.widget.focus()

    &lt;&lt; define callbacks &gt;&gt;
    if e.widget._name.startswith('body'):
        &lt;&lt; define commandList for body &gt;&gt;
        &lt;&lt; add entries for context sensitive commands in body &gt;&gt;
    else:
        &lt;&lt; define commandList for log pane &gt;&gt;
                
    rmenu = Tk.Menu(None,tearoff=0,takefocus=0)
    for (txt,cmd) in commandList:
        if txt == '-':
            rmenu.add_separator()
        else:
            rmenu.add_command(label=txt,command=cmd)

    #rmenu.tk_popup(e.x_root-23,e.y_root+13)
    rmenu.tk_popup(e.x_root+1,e.y_root-10)</t>
<t tx="ekr.20040422072343.7">commandList = [
    #('-||-|-||-',None),   #
    #('U',c.undoer.undo),  #no c.undoer
    #('R',undoer.redo),
    # ('-',None),
    ('Cut', c.frame.OnCutFromMenu), 
    ('Copy',c.frame.OnCopyFromMenu),
    ('Paste', c.frame.OnPasteFromMenu),
    ('Delete',rc_dbodyCallback),
    ('-',None),
    ('SelectAll',c.frame.body.selectAllText),
    ('-',None),
    ('Indent',c.indentBody),
    ('Dedent',c.dedentBody),
    ('-',None),
    #('Find Bracket',c.findMatchingBracket),
    #('Insert newline', rc_nlCallback),
    
    # this option seems not working, at least in win32
    # replaced with context-sensitive "pydoc help"  --Maxim Krikun
    # ('Help(txt)',rc_helpCallback),   #how to highlight 'txt' in the menu?
    
    ('Execute Script',c.executeScript)
    # ('-||-|-||-',None),   # 1st &amp; last needed because of freaky sticky finger
    ]</t>
<t tx="ekr.20040422072343.8">@ Context-sensitive rclick commands.

On right-click get the selected text, or the whole line containing cursor if no selection.
Scan this text for certain regexp pattern. For each occurrence of a pattern add a command,
which name and action depend on the text matched.

Example below extracts URL's from the text and puts "Open URL:..." th menu.

@c

&lt;&lt; get text and word from the body text &gt;&gt;

if 0:
    g.es("selected text: "+text)
    g.es("selected word: "+repr(word))

contextCommands=[]

&lt;&lt; add entry for open url &gt;&gt;
&lt;&lt; add entry for jump to section &gt;&gt;
if word:
    &lt;&lt; add epydoc help &gt;&gt;

if contextCommands:
    commandList.append(("-",None))
    commandList.extend(contextCommands)</t>
<t tx="ekr.20040422072343.9"></t>
<t tx="ekr.20040422072343.10">def crop(s,n=20,end="..."):

    """return a part of string s, no more than n characters; optionally add ... at the end"""
    
    if len(s)&lt;=n:
        return s
    else:
        return s[:n]+end # EKR</t>
<t tx="ekr.20040422072343.11">def getword(s,pos):

    """returns a word in string s around position pos"""

    for m in re.finditer("\w+",s):
        if m.start()&lt;=pos and m.end()&gt;=pos:
            return m.group()
    return None			
</t>
<t tx="ekr.20040422072343.12">def getdoc(thing, title='Help on %s', forceload=0):
    
    #g.trace(thing)

    if 1: # Both seem to work.

        # Redirect stdout to a "file like object".
        old_stdout = sys.stdout
        sys.stdout = fo = g.fileLikeObject()
        # Python's builtin help function writes to stdout.
        help(str(thing))
        # Restore original stdout.
        sys.stdout = old_stdout
        # Return what was written to fo.
        return fo.get()

    else:
        # Similar to doc function from pydoc module.
        from pydoc import resolve, describe, inspect, text, plain
        object, name = resolve(thing, forceload)
        desc = describe(object)
        module = inspect.getmodule(object)
        if name and '.' in name:
            desc += ' in ' + name[:name.rfind('.')]
        elif module and module is not object:
            desc += ' in module ' + module.__name__
        doc = title % desc + '\n\n' + text.document(object, name)
        return plain(doc)</t>
<t tx="ekr.20040422072343.13">scan_url_re="""(http|https|ftp)://([^/?#\s'"]*)([^?#\s"']*)(\\?([^#\s"']*))?(#(.*))?"""

for match in re.finditer(scan_url_re, text):
    
    #get the underlying text
    url=match.group()
    
    #create new command callback
    def url_open_command(*k,**kk):
        import webbrowser
        try:
            webbrowser.open_new(url)
        except:
            g.es("not found: " + url,color='red')

    #add to menu
    menu_item=( 'Open URL: '+crop(url,30), url_open_command)
    contextCommands.append( menu_item )</t>
<t tx="ekr.20040422072343.14">scan_jump_re="&lt;"+"&lt;[^&lt;&gt;]+&gt;"+"&gt;"

p=c.currentPosition()
for match in re.finditer(scan_jump_re,text):
    name=match.group()
    ref=g.findReference(c,name,p)
    if ref:
        # Bug fix 1/8/06: bind c here.
        # This is safe because we only get called from the proper commander.
        def jump_command(c=c,*k,**kk):
            c.beginUpdate()
            c.selectPosition(ref)
            c.endUpdate()
        menu_item=( 'Jump to: '+crop(name,30), jump_command)
        contextCommands.append( menu_item )
    else:
        # could add "create section" here?
        pass</t>
<t tx="ekr.20040422072343.15">def help_command(*k,**kk):
    # g.trace(word)
    try:
        doc=getdoc(word,"="*60+"\nHelp on %s")
        # It would be nice to save log pane position
        # and roll log back to make this position visible,
        # since the text returned by pydoc can be several 
        # pages long
        g.es(doc,color="blue")
        print doc
    except Exception, value:
        g.es(str(value),color="red")

menu_item=('Help on: '+crop(word,30), help_command)
contextCommands.append( menu_item )</t>
<t tx="ekr.20040422072343.16">commandList=[
    ('Cut', c.frame.OnCutFromMenu), 
    ('Copy',c.frame.OnCopyFromMenu),
    ('Paste', c.frame.OnPasteFromMenu),
    ('Select All', rc_selectAllCallback)]</t>
<t tx="ekr.20040422073911">text = c.frame.body.getSelectedText()
if text:
    word = text.strip()
else:
    ind0,ind1=c.frame.body.getTextSelection()
    n0,p0=ind0.split('.',2)
    n1,p1=ind1.split('.',2)
    assert n0==n1
    assert p0==p1
    text=c.frame.body.getTextRange(n0+".0",n1+".end")
    word=getword(text,int(p0))</t>
<t tx="ekr.20040422081253">@
0.1, 0.2: Created by 'e'.
0.3 EKR:
    - Converted to 4.2 code style. Use @file node.
    - Simplified rClickBinder, rClicker, rc_help.  Disabled signon.
    - Removed calls to registerHandler, "by" ivar, rClickNew, and shutdown code.
    - Added select all item for the log pane.
0.4 Maxim Krikun:
    - added context-dependent commands:
       open url, jump to reference, pydoc help
    - replaced rc_help with context-dependent pydoc help;
    - rc_help was not working for me :(
0.5 EKR:
    - Style changes.
    - Help sends output to console as well as log pane.
    - Used code similar to rc_help code in getdoc.
      Both kinds of code work for me (using 4.2 code base)
    - Simplified crop method.
0.6 EKR:
    - Use g.importExtension to import Tk.
0.7 EKR:
    - Use e.widget._name.startswith('body') to test for the body pane.
0.8 EKR:
- Added init function.
- Eliminated g.top.
0.9 EKR:
- Define callbacks so that all are accessible.
0.10 EKR:
- Removed call to str that was causing a unicode error.


0.10exe AGP:
    -changed popup coords
    </t>
<t tx="ekr.20040722134535"># Warning: these plugins are not ready for prime time.</t>
<t tx="ekr.20040722135402"></t>
<t tx="ekr.20040722135402.1"></t>
<t tx="ekr.20040722141148">@

You would typically not enable any of the following "plugins".

These plugins contain example code only.</t>
<t tx="ekr.20040828105233">@first # -*- coding: utf-8 -*-
@language python
@tabwidth -4

"""
Translate a few menu items into Simplified Chinese
本插件将部分Leo菜单翻译成简体中文
   By Zhang Le &lt;ejoy@xinhuanet.com&gt;
   
"""

# Chinese translation completed by Zhang Le, May 2004
# based on the french_fm.py

# NOTE: The accelerated key (&amp;) failed to work on Chinese text, probably because 
# the width of one Chinese character is 2 not 1, which confuses Tk. I'm not sure 
# whether this is a bug of Tk or a bug of Leo. Although I do not use &amp; in the 
# Chinese menu, Tk places an underline below the first character of each menu
# entry. Another bug in Tk?

# Note 2 (EKR):  The menu names themselves did not translate on my XP machine.
# All the headlines appear as "??".

import leoPlugins
import leoGlobals as g

@others

if not g.app.unitTesting: # Unpleasant for unit testing.

    # Register the handlers...
    leoPlugins.registerHandler("menu1", onMenu)
    
    __version__ = "1.1" # Set version for the plugin handler.
    g.plugin_signon(__name__)</t>
<t tx="ekr.20040828105233.1">def onMenu (tag,keywords):

    c = keywords.get("c")
    table = (
        @others
    )

    # Call the convenience routine to do the work.
    c.frame.menu.setRealMenuNamesFromTable(table)</t>
<t tx="ekr.20040828105233.2">("File","File文件"),
    ("New","新建"),
    ("Open...","打开"),
    ("Open With...","用程序打开..."),
    ("Close","关闭"),
    ("Save","保存"),
    ("Save As","另存为..."),
    ("Save To","另存到..."),
    ("Revert To Saved","恢复到保存的文件"),
    ("Recent Files...","最近访问的文件..."),
        ("Clear Recent Files","清除最近访问文件列表"),
    ("Read/Write...", "读取/写入..."),
        ("Read Outline Only", "只读取大纲"),
        ("Read @file Nodes", "读取 @file 结点"),
        ("Write Dirty @file Nodes", "保存改动的 @file 结点"),
        ("Write missing @file Nodes", "保存缺少的(missing) @file 结点"),
        ("Write Outline Only", "仅保存大纲"),
        ("Write @file Nodes", "保存 @file 结点"),
        ("Write 4.x Derived Files", "保存 4.x 版本的文件"),
        ("Write 3.x Derived Files", "保存 3.x 版本的文件"),
    ("Tangle...", "Tangle 操作..."),
        ("Tangle All", "全部 Tangle"),
        ("Tangle Marked", "只 Tangle 书签结点"),
        ("Tangle", "Tangle 当前结点"),
    ("Untangle...", "Untangle 操作..."),
        ("Untangle All", "全部 Untangle"),
        ("Untangle Marked", "只 Untangle 书签结点"),
        ("Untangle", "Untangle 当前结点"),
    ("Import...", "导入..."),
        ("Import Derived File", "导入生成的文件"),
        ("Import To @file", "导入到 @file"),
        ("Import To @root", "导入到 @root"),
        ("Import CWEB Files", "导入 CWEB 文件"),
        ("Import noweb Files", "导入 noweb 文件"),
        ("Import Flattened Outline", "导入平坦 (Flattened) 大纲文件 (MORE 格式)"),
    ("Export...", "导出..."),
        ("Export Headlines", "导出标题 (Headlines)"),
        ("Outline To CWEB", "导出大纲到 CWEB"),
        ("Outline To Noweb", "导出大纲到 Noweb"),
        ("Flatten Outline", "导出平坦 (Flattened) 大纲 (MORE 格式)"),
        ("Remove Sentinels", "删除导出文件中的特殊大纲标记 (Sentinelles)"),
        ("Weave", "导出为 Weave 格式 (Listing)"),
        ("Export all to AsciiDoc", "全部导出为 AsciiDoc 文件"),
        ("Export current tree to AsciiDoc", "将当前树导出为 AsciiDoc 文件"),
    ("Exit","退出"),
</t>
<t tx="ekr.20040828105233.3">("Edit","Edit编辑"),
    ("Undo Typing","撤销键入"),
    ("Undo Cut Node","撤销剪切结点"),
    ("Redo Typing","重做键入"),
    ("Can't Undo", "无法撤销"),
    ("Can't Redo", "无法重做"),
    ("Cut", "剪切"),
    ("Copy", "复制"),
    ("Paste", "粘贴"),
    ("Delete", "删除"),
    ("Select All", "全选"),
    ("Edit Body...", "编辑文本域..."),
        ("Extract Section", "Extract Section"),
        ("Extract Names", "Extract Names"),
        ("Extract", "Extract"),
        ("Convert All Blanks", "Convert All Blanks"),
        ("Convert All Tabs", "Convert All Tabs"),
        ("Convert Blanks", "Convert Blanks"),
        ("Convert Tabs", "Convert Tabs"),
        ("Insert Body Time/Date", "插入当前日期/时间"),
        ("Reformat Paragraph", "重新格式化段落"),
        ("Indent", "增加缩进"),
        ("Unindent", "减少缩进"),
        ("Match Brackets", "括号匹配"), #  &lt;({["), #EKR
    ("Edit Headline...", "编辑标题..."),
        ("Edit Headline", "编辑标题"),
        ("End Edit Headline", "结束编辑标题"),
        ("Abort Edit Headline", "放弃编辑标题"),
        ("Insert Headline Time/Date", "插入当前日期/时间"),
        ("Toggle Angle Brackets", "切换尖括号标记"),
    ("Find...", "查找..."),
        ("Find Panel", "查找对话框"),
        ("Find Next", "查找下一个"),
        ("Find Previous", "查找前一个"),
        ("Replace", "替换"),
        ("Replace, Then Find", "替换后查找"),
    ("Go To Line Number", "跳转到行..."),
    ("Execute Script", "执行Python脚本"),
    ("Set Font...", "设置字体..."),
    ("Set Colors...", "设置颜色..."),
    ("Show Invisibles", "显示不可见域"),
    ("Hide Invisibles", "隐藏不可见域"),
    ("Preferences", "偏好设置"),
</t>
<t tx="ekr.20040828105233.4">("Outline", "Outline大纲"),
    ("Cut Node", "剪切结点"),
    ("Copy Node", "拷贝结点"),
    ("Paste Node", "粘贴结点"),
    ("Delete Node", "删除结点"),
    ("Insert Node", "插入结点"),
    ("Clone Node", "克隆结点"),
    ("Sort Children", "排序孩子结点"),
    ("Sort Siblings", "排序兄弟结点"),
    ("Check Outline", "校验大纲"),
    ("Dump Outline", "大纲转储 (Dump)"),
    ("Hoist", "提升结点 (Hoist)"),
    ("De-Hoist", "下降结点 (De-Hoist)"),
    ("Expand/Contract...", "扩展/收缩"),
        ("Contract All", "全部收缩"),
        ("Contract Node", "收缩当前结点"),
        ("Contract Parent", "收缩父结点"),
        ("Expand Prev Level", "扩展到上一级"),
        ("Expand Next Level", "扩展到下一级"),
        ("Expand To Level 1", "扩展到第1级"),
        ("Expand To Level 2", "扩展到第2级"),
        ("Expand To Level 3", "扩展到第3级"),
        ("Expand To Level 4", "扩展到第4级"),
        ("Expand To Level 5", "扩展到第5级"),
        ("Expand To Level 6", "扩展到第6级"),
        ("Expand To Level 7", "扩展到第7级"),
        ("Expand To Level 8", "扩展到第8级"),
        ("Expand All", "扩展全部"),
        ("Expand Node", "扩展当前结点"),
    ("Move...", "移动..."),
        ("Move Down", "下移"),
        ("Move Left", "左移"),
        ("Move Right", "右移"),
        ("Move Up", "上移"),
        ("Promote", "Promote"),
        ("Demote", "Demote"),
    ("Mark/Unmark...", "书签功能..."),
        ("Mark", "标记书签"),
        ("Unmark", "删除书签"),
        ("Mark Subheads", "标记子标题"),
        ("Mark Changed Items", "标记已修改的结点"),
        ("Mark Changed Roots", "标记已修改的根结点 (Roots)"),
        ("Mark Clones", "标记克隆"),
        ("Unmark All", "删除所有书签"),
    ("Go To...", "跳转到..."),
        ("Go Back", "后退"),
        ("Go Forward", "前进"),
        ("Go To Next Marked", "跳转到下一个书签"),
        ("Go To Next Changed", "跳转到下一个已修改结点"),
        ("Go To Next Clone", "跳转到下一个克隆结点"),
        ("Go To First Node", "跳转到第一个结点"),
        ("Go To Last Node", "跳转到最后一个结点"),
        ("Go To Parent", "跳转到父结点"),
        ("Go To Prev Sibling", "跳转到上一个兄弟结点"),
        ("Go To Next Sibling", "跳转到下一个兄弟结点"),
        ("Go To Prev Visible", "跳转到上一个可见结点"),
        ("Go To Next Visible", "跳转到下一个可见结点"),
        ("Go To Prev Node", "跳转到上一结点"),
        ("Go To Next Node", "跳转到下一结点"),</t>
<t tx="ekr.20040828105233.5">("Plugins", "Plugins插件"),
    ("chinese", "Chinese (汉化)"),
</t>
<t tx="ekr.20040828105233.6">("Window", "Window窗口"),
    ("Equal Sized Panes", "使各面板大小相等"),
    ("Toggle Active Pane", "切换激活面板"),
    ("Toggle Split Direction", "切换面板分割方向"),
    ("Cascade", "级联排列窗体"),
    ("Minimize All", "全部最小化"),
    ("Open Compare Window", "打开文件比较窗口..."),
    ("Open Python Window", "打开Python集成环境(IDLE)..."),
</t>
<t tx="ekr.20040828105233.7">("Help", "Help帮助"),
    ("About Leo...", "关于Leo..."),
    ("Online Home Page", "访问在线主页"),
    ("Open Online Tutorial", "访问在线教程"),
    ("Open Offline Tutorial", "访问离线教程 (CHM文件)"),
    ("Open LeoDocs.leo", "打开 LeoDocs.leo"),
    ("Open LeoConfig.leo", "打开 LeoConfig.leo"),
    ("Apply Settings", "应用设置")</t>
<t tx="ekr.20040915073259"></t>
<t tx="ekr.20040918165427.4">@nocolor

Developers
By: jasonic ( Jason Cunliffe ) 
 @dictionary   
2003-08-21 07:51

Auto-completion dictionary files would be excellent.
Ideally each Leo language extension could just point to a separate .dict file. 

Hopefully we can build some Leo plugin utilities to generate these .dict files by parsing any file you'd like to use a 'source' for Leo dictionary. They might need manual cleanup, but vcould be big timesaver, especially for XML formats and the like. Great to be able to sahre these easily. 

Interesting uses for Leo dictionaries beyond just autocompletion. 
I am thinking they might open the door to some powerful macro/template behavior. 

For example, you load a special dictionary to help certain kinds of repetitive formatted content. CSS and XSLT could be good candidates, but also any kind of mild databases or lists. Documentation.

So first we need basic dicts for Leo supported languages: Python, Perl, Javascript etc..

Then we need to consider that any Leo Node could have its own dictionary defined inline..

@dictionary filepath-to-custom-leo-dict

With collaborative LeoN this would be very useful because connected Leo sessions could invoke each other's dictionaries!!

- Jason  
</t>
<t tx="ekr.20041001210557"></t>
<t tx="ekr.20041009112303"></t>
<t tx="ekr.20041019072632"></t>
<t tx="ekr.20041030092101">@ Notes by EKR:  The dyna plugin is a remarkable body of work by 'e'.  Have fun with it.

You may download the latest version at: http://rclick.netfirms.com/dyna_menu.py.html
</t>
<t tx="ekr.20041103052443"># Execute this in a script button.

import string

@others

if 1:
    &lt;&lt; set nameList to the list of functions in leoGlobals.py &gt;&gt;
else:
    p = g.findNodeAnywhere("@file leoGlobals.py")
    nameList = findFunctionsInTree(p)

    nameList.sort() ; g.enl()
    for name in nameList: g.es("'%s'," % name)
    
    s = "%d functions in leoGlobals.py" % len(nameList)
    print s ; g.es(s)


p = c.currentPosition()
g.enl() ; g.enl()
count = prependNamesInTree(c,p,nameList,"g.",replace=True) # Just prints if replace==False.
s = "%d --- done --- " % count
print s ; g.es(s)</t>
<t tx="ekr.20041103052443.1">def findFunctionsInTree(p):
    
    nameList = []
    for p in p.self_and_subtree_iter():
        names = findDefs(p.bodyString())
        if names:
            for name in names:
                if name not in nameList:
                    nameList.append(name)
    return nameList</t>
<t tx="ekr.20041103052443.2">def findDefs(body):
    
    lines = body.split('\n')
    names = []
    for s in lines:
        i = g.skip_ws(s,0)
        if g.match(s,i,"class"):
            return [] # The classes are defined in a single node.
        if g.match(s,i,"def"):
            i = g.skip_ws(s,i+3)
            j = g.skip_c_id(s,i)
            if j &gt; i:
                name = s[i:j]
                if g.match(name,0,"__init__"): 
                    return [] # Disallow other class methods.
                names.append(name)
    return names</t>
<t tx="ekr.20041103052443.3">def prependNamesInTree(c,p,nameList,prefix,replace=False):
    
    assert(len(prefix) &gt; 0)
    ch1 = string.letters + '_'
    ch2 = string.letters + string.digits + '_'
    def_s = "def " ; def_n = len(def_s)
    prefix_n = len(prefix)
    total = 0
    c.beginUpdate()
    for p in p.self_and_subtree_iter():
        count = 0 ; s = p.bodyString()
        printFlag = False
        if s:
            for name in nameList:
                i = 0 ; n = len(name)
                while 1:
                    &lt;&lt; look for name followed by '(' &gt;&gt;
            if count and replace:
                if 0:
                    &lt;&lt; print before and after &gt;&gt;
                c.setBodyString(p,s)
                p.setDirty()
        g.es("%3d %s" % (count,p.headString()))
        total += count
    c.endUpdate()
    return total</t>
<t tx="ekr.20041103052443.4">i = s.find(name,i)
if i == -1:
    break
elif g.match(s,i-1,'.'):
    i += n # Already an attribute.
elif g.match(s,i-prefix_n,prefix):
    i += n # Already preceded by the prefix.
elif g.match(s,i-def_n,def_s):
    i += n # preceded by "def"
elif i &gt; 0 and s[i-1] in ch1:
    i += n # Not a word match.
elif i+n &lt; len(s) and s[i+n] in ch2:
    i += n # Not a word match.
else:
    j = i + n
    j = g.skip_ws(s,j)
    if j &gt;= len(s) or s[j] != '(':
        i += n
    else: # Replace name by prefix+name
        s = s[:i] + prefix + name + s[i+n:]
        i += n ; count += 1
        # g.es('.',newline=False)
        if 1:
            if not printFlag:
                printFlag = True
                # print p.headString()
            print g.get_line(s,i-n)</t>
<t tx="ekr.20041103052443.5">print "-"*10,count,p.headString()
print "before..."
print p.bodyString()
print "-"*10,"after..."
print s</t>
<t tx="ekr.20041103052443.6">nameList = (
'alert',
'angleBrackets',
'appendToList',
'callerName',
'CheckVersion',
'choose',
'clearAllIvars',
'clear_stats',
'collectGarbage',
'computeLeadingWhitespace',
'computeWidth',
'computeWindowTitle',
'createTopologyList',
'create_temp_name',
'disableIdleTimeHook',
'doHook',
'dump',
'ecnl',
'ecnls',
'enableIdleTimeHook',
'enl',
'ensure_extension',
'es',
'esDiffTime',
'es_error',
'es_event_exception',
'es_exception',
'escaped',
'executeScript',
'file_date',
'findNodeAnywhere',
'findTopLevelNode',
'findNodeInTree',
'findReference',
'find_line_start',
'find_on_line',
'flattenList',
'funcToMethod',
'getBaseDirectory',
'getOutputNewline',
'getTime',
'get_Sherlock_args',
'get_directives_dict',
'get_leading_ws',
'get_line',
'get_line_after',
'getpreferredencoding',
'idleTimeHookHandler',
'importFromPath',
'initScriptFind',
'init_sherlock',
'init_trace',
'isUnicode',
'isValidEncoding',
'is_c_id',
'is_nl',
'is_special',
'is_ws',
'is_ws_or_nl',
'joinLines',
'listToString',
'makeAllNonExistentDirectories',
'makeDict',
'match',
'match_c_word',
'match_ignoring_case',
'match_word',
'module_date',
'openWithFileName',
'optimizeLeadingWhitespace',
'os_path_abspath',
'os_path_basename',
'os_path_dirname',
'os_path_exists',
'os_path_getmtime',
'os_path_isabs',
'os_path_isdir',
'os_path_isfile',
'os_path_join',
'os_path_norm',
'os_path_normcase',
'os_path_normpath',
'os_path_split',
'os_path_splitext',
'pause',
'plugin_date',
'plugin_signon',
'printDiffTime',
'printGc',
'printGcRefs',
'printGlobals',
'printLeoModules',
'print_bindings',
'print_stats',
'readlineForceUnixNewline',
'redirectStderr',
'redirectStdout',
'removeLeadingWhitespace',
'removeTrailingWs',
'reportBadChars',
'restoreStderr',
'restoreStdout',
'sanitize_filename',
'scanAtEncodingDirective',
'scanAtFileOptions',
'scanAtLineendingDirective',
'scanAtPagewidthDirective',
'scanAtRootOptions',
'scanAtTabwidthDirective',
'scanDirectives',
'scanError',
'scanf',
'set_delims_from_language',
'set_delims_from_string',
'set_language',
'shortFileName',
'skip_blank_lines',
'skip_block_comment',
'skip_braces',
'skip_c_id',
'skip_heredoc_string',
'skip_leading_ws',
'skip_leading_ws_with_indent',
'skip_line',
'skip_long',
'skip_matching_delims',
'skip_nl',
'skip_non_ws',
'skip_parens',
'skip_pascal_begin_end',
'skip_pascal_block_comment',
'skip_pascal_braces',
'skip_pascal_string',
'skip_php_braces',
'skip_pp_directive',
'skip_pp_if',
'skip_pp_part',
'skip_python_string',
'skip_string',
'skip_to_char',
'skip_to_end_of_line',
'skip_to_semicolon',
'skip_typedef',
'skip_ws',
'skip_ws_and_nl',
'splitLines',
'stat',
'stdErrIsRedirected',
'stdOutIsRedirected',
'toEncodedString',
'toUnicode',
'toUnicodeFileEncoding',
'top',
'trace',
'trace_tag',
'update_file_if_changed',
'utils_rename',
'windows',
'wrap_lines')</t>
<t tx="ekr.20041110104350"></t>
<t tx="ekr.20041114102139">@nocolor</t>
<t tx="ekr.20041114102139.1">- Several plugins show the docstring, so please take care to do a good job of
describing what the plugin does and how to use it.

- Please put the following immediately following the plugin's docstring.

    @language python
    @tabwidth -4

- There is no need to use sections if they are empty.

- The code should test whether modules have been imported only if those modules
may not be available on all platforms.

- Use following three lines only if your plugin uses a gui.

    if g.app.gui is None: 
        g.app.createTkGui(__file__)
    if g.app.gui.guiName() == "tkinter":
        ...

- Please use g.plugin_signon as shown, not leoPlugins.signon.</t>
<t tx="ekr.20041114102139.2">Please use the general format as shown in &lt;&lt; imports &gt;&gt;.  In partular:

- Please do _not_ assume that modules like Tkinter, Pmw, etc. are always available.
  Use g.importExtension.

- Good Python style is to put each import on a separate line.

- Please abbreviate Tkinter as Tk.  Please do NOT abbreviate Pmw or leoPlugins.

- Please do NOT use either of the following kinds of imports.
    from m import *
    from m import x,y,z

- Do not import leoNodes unless your plugin creates nodes directly.</t>
<t tx="ekr.20041114103913">Most of the comments in the style guide are comments _about_ the style guide.
You would replace these comments with your own, or eliminate them entirely in
your plugin.</t>
<t tx="ekr.20041114103913.1">PLEASE define each function or method in a separate node! To make this work,
just put @others in the root of your plugin as shown. Note that @others may be
nested, as shown in class myClass.</t>
<t tx="ekr.20041211035618"></t>
<t tx="ekr.20050101090207.2">import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter')

import re
import sys
</t>
<t tx="ekr.20050101090717">"""
mnplugins.py

mnplugins shows how to :
define new Commands  "insertOK" + "insertUser"
create Usermenu with new Commands

new Commands:
insertOK: 
    insert 'OK' in headline and a stamp in the first bodyline
    are there childnodes without 'OK' verhindern OK in actual node
    (insertOK on iconrclick2 too)

insertUser : Shift-F6
    insert a &lt;user/date/time&gt; stamp at the current location in bodytext
"""</t>
<t tx="ekr.20050101090717.1">import leoGlobals as g
import leoPlugins

import leoCommands
import time

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)</t>
<t tx="ekr.20050111122605"></t>
<t tx="ekr.20050128070307"></t>
<t tx="ekr.20050217093214">@nocolor</t>
<t tx="ekr.20050227071948"></t>
<t tx="ekr.20050227071948.1">
- move the clone marker to the same place as the blue square
  content indicator. They can overlap.  Make room for annotations.
  



</t>
<t tx="ekr.20050227071948.2">
copy icons from freemind.

expandable box of icons at the head of a headline.
but manipulation vnode's iconx and icony positions.
vnode.computeIcon &amp; setIcon

icons in popup menus too ?

</t>
<t tx="ekr.20050227071948.3">
There seems to be a colour selector in leo.
</t>
<t tx="ekr.20050227071948.4"></t>
<t tx="ekr.20050227071948.5">
He haven't thought about it.
</t>
<t tx="ekr.20050227071948.6"></t>
<t tx="ekr.20050227071948.7"></t>
<t tx="ekr.20050227071948.8"></t>
<t tx="ekr.20050227071948.9"></t>
<t tx="ekr.20050227071948.10">
font
size
style
</t>
<t tx="ekr.20050227071948.11"></t>
<t tx="ekr.20050227071948.12"></t>
<t tx="ekr.20050227071948.13"></t>
<t tx="ekr.20050227071948.15"></t>
<t tx="ekr.20050227071948.16"></t>
<t tx="ekr.20050227071948.17">
Store semantics instead of colours.  Semantics then map to colours.


headline colours are reseted by the tree select and unselect methods.
maybe need to override them via the after (re)draw hook.


Offending Methods are all in leoTkinterTree.py
setNormalLabelState (self,v): # selected, editing
setDisabledLabelState (self,v): # selected, disabled
setUnselectedLabelState (self,v): # not selected.


</t>
<t tx="ekr.20050227071948.18">
Different coloured arrows for different priorities.

VeryHigh Red
High Orange
* Medium Green
Low Blue  (whatever)
Done  (tick)
</t>
<t tx="ekr.20050227071948.19">
archtetype based vnode attributes, not colour.
</t>
<t tx="ekr.20050227071948.20"></t>
<t tx="ekr.20050227071948.21">
The colouring conflicts.
</t>
<t tx="ekr.20050227071948.22"></t>
<t tx="ekr.20050227071948.23"></t>
<t tx="ekr.20050227071948.24">Not always predictable.

src/leoTkinterTree.py: menu.post(event.x_root, event.y_root)

</t>
<t tx="ekr.20050227071948.27">
# XXX merge: my model, coad &amp; de luca and holy trinity

# change colours: only foreground !
colour_table = {
    'interface': ["black", "OliveDrab2"],
    'logic':  ("black", "LightSkyBlue2"),
    'data':  ("black", "SandyBrown"),
    }

# Leo nodes.  Background hilite ?
Dead @ignore nodes + Documentat nodes  =&gt; Grey out
@File nodes, sub tree root

# Archetype Colouring

# Holy Trinity
Interface
Logic/Transform Centers/Functions
Data  =&gt; Description

# Coad and De Luca  --- Contrast against their meta-model
# It is a hiearchy going up from Description.
Description/Attributes/Data Catalog:  Purple
Party/Place/Thing:  Green
Role/Participation:  Yellow (Khaki or straw)
Moment/Interval/Event: Pink
Interface: White

# Me
Entity =&gt; Place or thing
  Core  =&gt;  Thing
  Interface =&gt;
  
Relationship (Loading and wiring code) =&gt; Moment(Init)
     =&gt; Special moment
     
* Interaction  =&gt; Moment/Interval + more !

# Unified : 5 Categories Max!!
Attributes, Data, Description, Lookup Tables.   =&gt; Brown
Entity Core, Place, Thing, Party    =&gt; Green
Logic, Pure Functions               =&gt; Blue
Role/Interface/Participation/Trait  =&gt; Straw/Khaki
Dynamic Stuff, Moment/Interaction   =&gt; Pinkish

</t>
<t tx="ekr.20050227071948.28">3. Various drawing hooks. I've restored the drawing hooks that used to exists. These are so-called "stub" hooks. The entries of these hooks in leoDocs.leo and leoPlugins.leo are as follows:
 
 tag argument keys in keywords
 (hook name) overrides when called dictionary argument
 --------- --------- ----------- -------------------
 ...
 "draw-outline-box" yes start of drawBox tree,p,v,x,y (note 6)
 "draw-outline-icon" yes start of tree.drawIcon tree,p,v,x,y (note 6)
 "draw-outline-node" yes start of tree.drawNode tree,p,v,x,y (note 6)
 "draw-outline-text-box" yes start of tree.drawText tree,p,v,x,y (note 6)
 "draw-sub-outline" yes start of tree.drawTree tree,p,v,x,y,h,level (note 6)
 ...
 
 These probably work exactly as the old hooks did, though I didn't use the old (4.0?) code as a base. The only change is the new p keyword argument. In all cases v = p.v. I probably should a p keyword argument to most other hooks, and I'm lazy...
 
 Warning: all these hooks "override" the existing code, which doesn't get executed if the hook returns anything except None. This means that the hook had better return what the "host" code returns, and this has changed recently to support user icons, and may change in the future as needed.
 
 For example, here is the code in drawNode
 
 data = g.doHook("draw-outline-node",tree=tree,p=p,v=v,x=x,y=y)
 if data is not None: return data
 
 At present, drawNode typically returns what return force_draw_node returns, which is a tuple (h,xw). This is needed to support icons of various sizes.
 
 In short, I'm not real sure how useful these hooks are going to be, or how stable.
 

</t>
<t tx="ekr.20050227071948.29">
add the colour menu to rclickhead1


 "draw-outline-box" yes start of drawBox tree,p,v,x,y (note 6)
    It works, but not sure when it is called.

 "draw-outline-icon" yes start of tree.drawIcon tree,p,v,x,y (note 6)
    The box obscures it.  If True is return, rlick wont work anymore.

 "draw-outline-node" yes start of tree.drawNode tree,p,v,x,y (note 6)
    This calls -icon and -box ?
 "draw-outline-text-box" yes start of tree.drawText tree,p,v,x,y (note 6)
    Does not obscure the box area !!

 "draw-sub-outline" yes start of tree.drawTree tree,p,v,x,y,h,level (note 6)
     Use this for head highlighting ? Probally called after the node is draw
     but before drawing the children.
yay ! they work with the CVS version.

@c

#registerHandler("draw-outline-box", draw0)
#registerHandler("draw-outline-node", draw0)
#registerHandler("draw-outline-text-box", draw0)

#registerHandler("iconrclick1",show_colour_menu)
</t>
<t tx="ekr.20050227072121"></t>
<t tx="ekr.20050303051035">@

Note: the newButtons.py now has templates for the following plugin nodes.
    
- init: A generic init function.
- init(tk): An init function for a plugin that uses Tk (or Pmw).
- &lt;&lt; imports &gt;&gt;:  The &lt;&lt;imports&gt;&gt; section.
- &lt;&lt; version history &gt;&gt;: The &lt;&lt;version history&gt;&gt; section.</t>
<t tx="ekr.20050303051035.2">&lt;&lt; docstring &gt;&gt;

__version__ = '0.0'
&lt;&lt; version history &gt;&gt;

&lt;&lt; imports &gt;&gt;

@others</t>
<t tx="ekr.20050303051035.3">'''This docstring should be a clear, concise description of
what the plugin does and how to use it.
'''
</t>
<t tx="ekr.20050303051035.4">@killcolor
@

Put notes about each version here.</t>
<t tx="ekr.20050303051035.5">import leoGlobals as g
import leoPlugins

Pmw = g.importExtension('Pmw',    pluginName=__name__,verbose=True,required=True)
Tk  = g.importExtension('Tkinter',pluginName=__name__,verbose=True,required=True)

# Whatever other imports your plugins uses.</t>
<t tx="ekr.20050303051101">def init ():
    
    ok = Pmw and Tk
    
    if ok:
        if g.app.gui is None:
            g.app.createTkGui(__file__)
            
        ok = g.app.gui.guiName() == "tkinter"

        if ok:
            if 1: # Use this if you want to create the commander class before the frame is fully created.
                leoPlugins.registerHandler('before-create-leo-frame',onCreate)
            else: # Use this if you want to create the commander class after the frame is fully created.
                leoPlugins.registerHandler('after-create-leo-frame',onCreate)
            g.plugin_signon(__name__)
        
    return ok</t>
<t tx="ekr.20050303051150">def onCreate (tag, keys):
    
    c = keys.get('c')
    if not c: return
    
    thePluginController = pluginController(c)</t>
<t tx="ekr.20050303051222">class pluginController:
    
    @others</t>
<t tx="ekr.20050303051222.1">def __init__ (self,c):
    
    self.c = c
    # Warning: hook handlers must use keywords.get('c'), NOT self.c.</t>
<t tx="ekr.20050303080042"></t>
<t tx="ekr.20050303080042.1">[Main]

RefreshInterval = 60
ColdColour = blue
HotColour = red
HitsToHeatUp = 2
</t>
<t tx="ekr.20050303080236">@killcolor

- Crashes if .ini file does not exist.</t>
<t tx="ekr.20050306071540">def onStart2 (tag, keywords):
    
    """
    Showing how to define a global hook that affects all commanders.
    """

    import leoTkinterFrame
    log = leoTkinterFrame.leoTkinterLog
    
    # Replace frame.put with newPut (not shown).
    g.funcToMethod(newPut,log,"put")</t>
<t tx="ekr.20050306071629">&lt;&lt; docstring &gt;&gt;

__version__ = '0.0'
&lt;&lt; version history &gt;&gt;

&lt;&lt; imports &gt;&gt;

@others</t>
<t tx="ekr.20050306071629.1">'''This docstring should be a clear, concise description of
what the plugin does and how to use it.
'''
</t>
<t tx="ekr.20050306071629.2">@killcolor
@

Put notes about each version here.</t>
<t tx="ekr.20050306071629.3">import leoGlobals as g
import leoPlugins

# Whatever other imports your plugins uses.</t>
<t tx="ekr.20050306071629.4">def init ():
    
    ok = True # This might depend on imports, etc.
    
    if ok:
        leoPlugins.registerHandler('start2',onStart2)
        g.plugin_signon(__name__)
        
    return ok</t>
<t tx="ekr.20050306072156">It is usually best _not_ to catch exceptions in plugins:
doHook catches all exceptions and disables further calls to plugins.

If a plugin catches exceptions during startup it should do one of the following:
    
- raise the exception again.
- provide an init function at the top level that reports the failure.</t>
<t tx="ekr.20050306081349"></t>
<t tx="ekr.20050328101812"> 
        
        
        </t>
<t tx="ekr.20050328101812.1"></t>
<t tx="ekr.20050328101812.2"></t>
<t tx="ekr.20050328101812.3"></t>
<t tx="ekr.20050329082101"></t>
<t tx="ekr.20050329082101.1">@nocolor</t>
<t tx="ekr.20050329082101.2">The AutoTrees plugin is a helper plugin designed to make it very easy to write "hanlder" plugins to manage dynamic content in Leo outlines. 

AutoTrees provides 

- convenient handler base classes which can be specialized for particular uses
- a manager to turn handlers on and off
- a set of example handlers to show the kinds of things that are possible

AutoTrees doesn't do anything that you cannot do in other ways, but it does provide a consistent way of adding dynamic content. This means that individual plugin writers don't have to rewrite all the same kinds of code each time and also makes it easier to maintain Leo, since it standardizes the way that certain classes of plugin interact with the Leo core.

</t>
<t tx="ekr.20050329082101.3">I'm a plugin writer and I want to write a plugin to display dynamic content - ie content not directly contained in the .leo or derived files, eg

- email messages 
- news feeds
- news groups
- documentation
- remote files
- statistics
- file system data
- data base records

You can do this as a standard plugin, but as an AutoTrees handler you,

- don't need to write code that interacts with the tree (this is done for you)
- get centralized management
- can still do everything else you could as a normal plugin

</t>
<t tx="ekr.20050329082101.4">AutoTrees is itself a plugin. When it starts it,

1. Scans the leo\plugins\trees folder to find handlers
2. Activates specific handlers (this is managed via a plugin manager type window)
3. Waits for clicks and double-clicks on special nodes

To create an AutoTree node, you add a node with @auto-my_handler. The @auto tells the plugin to go and look for the "my_handler" handler, if it is enabled. The handler is then called and this is then used to populate the node body and child nodes below this node.

eg, for an @auto-rss node, the node headline is "@auto-rss http://myurl/news.xml". The handler goes to the URL mentioned and downloads the news stories. It then creates child nodes for each story and populates the bodies. 

The handler doesn't have to worry about interacting with the Leo tree view, it just returns a tree object. 

</t>
<t tx="ekr.20050329082101.5">The best way is to use the existing examples as templates. Look at the "test" handler first as this is the "Hello world" of trees.

</t>
<t tx="ekr.20050329082101.6">@nocolor</t>
<t tx="ekr.20050329082101.7">Just some simple testing nodes</t>
<t tx="ekr.20050329082101.8"></t>
<t tx="ekr.20050329082101.9">this is one</t>
<t tx="ekr.20050329082101.10">this is two !!!</t>
<t tx="ekr.20050329082101.11">this is three</t>
<t tx="ekr.20050329082101.12"></t>
<t tx="ekr.20050329082101.13"></t>
<t tx="ekr.20050329082101.14"></t>
<t tx="ekr.20050329082101.15">Reads a remote news service.

@auto-rss &lt;url to news service&gt;

Requires feedparser installed:
    http://sourceforge.net/projects/feedparser/</t>
<t tx="ekr.20050329082101.16">title

summary_detail</t>
<t tx="ekr.20050329082101.40">title (slash_section, category)

summary_detail

link</t>
<t tx="ekr.20050329082101.51">title (modified)

link</t>
<t tx="ekr.20050329082101.52">Python 2.4.1 (release candhttp://www.python.org/2.4.1/index.htmlate 1) (2005-03-10)

http://www.python.org/2.4.1/index.html</t>
<t tx="ekr.20050329082101.53">Greg Stein, of Google and Apache Software Foundation, to deliver keynote at PyCon (2005-03-06)

http://www.python.org/pycon/2005/keynotes.html</t>
<t tx="ekr.20050329082101.54">New RSS feed for python-dev summaries (2005-02-24)

http://www.python.org/dev/summary/channews.rdf</t>
<t tx="ekr.20050329082101.55">Guhttp://www.sdforum.org/SDForum/Templates/CalendarEvent.aspx?CID=1547&amp;mo=2&amp;yr=2005o van Rossum speaking in Palo Alto (2005-02-17)

http://www.sdforum.org/SDForum/Templates/CalendarEvent.aspx?CID=1547&amp;mo=2&amp;yr=2005</t>
<t tx="ekr.20050329082101.56">Python 2.3.5 (final) (2005-02-08)

http://www.python.org/2.3.5/index.html</t>
<t tx="ekr.20050329082101.57">Security advisory for SimpleXMLRPCServer.py. (2005-02-03)

http://python.org/security/PSF-2005-001/</t>
<t tx="ekr.20050329082101.58">Deadline for OSCON proposals (2005-02-01)

http://mail.python.org/pipermail/python-announce-list/2005-January/003683.html</t>
<t tx="ekr.20050329082101.59">PyCon abstracts now available (2005-01-23)

http://www.python.org/moin/PyConDC2005/Presentations</t>
<t tx="ekr.20050329082101.60">PyCon preliminary schedule now available (2005-01-20)

http://www.python.org/pycon/2005/schedule.html</t>
<t tx="ekr.20050329082101.61">PSF has awarded three grants (2004-12-30)

http://www.python.org/psf/grants/index.html</t>
<t tx="ekr.20050329082101.62">Python for Nokia Series 60 now available (2004-12-23)

http://www.forum.nokia.com/main/0,,034-821,00.html</t>
<t tx="ekr.20050329082101.63">Python 2.4 (final) (2004-11-30)

http://www.python.org/2.4/index.html</t>
<t tx="ekr.20050329082101.64">PyZine issue 7 (2004-11-23)

http://www.pyzine.com/Issue007/</t>
<t tx="ekr.20050329082101.65">PyCon 2005 Call for Proposals (2004-10-23)

http://www.python.org/pycon/2005/cfp.html</t>
<t tx="ekr.20050329082101.66">Cameron Laird receives the Frank Willison Award (2004-10-18)

http://press.oreilly.com/pub/pr/1237</t>
<t tx="ekr.20050329082101.67">Reads a remote file

@auto-remote &lt;url to file&gt;

Requires pyCurl:
    http://pycurl.sourceforge.net/</t>
<t tx="ekr.20050329082101.68">&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;BBC - Error 404: Page not found&lt;/title&gt;
&lt;meta name="description" content="Error 404 - page not found" /&gt;
&lt;meta name="keywords" content="" /&gt;
&lt;meta name="created" content="20040506" /&gt;
&lt;meta name="updated" content="20040506" /&gt;
&lt;base href="http://www.bbc.co.uk" /&gt;
&lt;style&gt;
body {margin:0; padding:0;}
em {color:#900;}
p, ul {font-size:80%}
h4,h3,h2,h1,p, ul {font-family: verdana,arial,helvetica,sans-serif;}
h4,h3 {font-size:100%}
h4,h1 {margin:0}
div.main {padding:8px;margin:0px;width:770;}
form {margin:0;padding:0;}
&lt;/style&gt;
&lt;/head&gt;
&lt;body bgcolor="#ffffff" link="#333366" text="#000000" vlink="#333366" alink="#000000" marginheight="0" marginwidth="0"&gt;

&lt;!-- toolbar 1.4 toolbar.page 770 666666 --&gt;&lt;table width="100%" cellpadding="0" cellspacing="0" border="0"&gt;&lt;tr&gt;&lt;td colspan="2" style="background-color:#828282;" &gt;&lt;a name="top"&gt;&lt;img src="/f/t.gif" width="590" height="2" alt="" /&gt;&lt;/a&gt;&lt;/td&gt;&lt;td style="background-color:#828282;"&gt;&lt;img src="/f/t.gif" width="1" height="2" alt="" /&gt;&lt;/td&gt;&lt;/tr&gt;&lt;form action="http://www.bbc.co.uk/cgi-bin/search/results.pl"&gt;&lt;tr&gt;&lt;td style="border-left:2px solid #828282;background-color:#999999;" width="54"&gt;&lt;a href="http://www.bbc.co.uk/go/toolbar/-/"&gt;&lt;img src="/images/logo04.gif" width="50" height="20" alt="BBC" border="0" hspace="2" vspace="5" /&gt;&lt;/a&gt;&lt;/td&gt;&lt;td style="background:#999999;" align="right"&gt;&lt;table cellpadding="0" cellspacing="0" border="0" style="float:right;"&gt;&lt;tr&gt;&lt;td style="background:#999999;"&gt;&lt;font size="1"&gt;&lt;b&gt;&lt;a href="http://www.bbc.co.uk/go/toolbar/text/-/" style="color:#ffffff;text-decoration:none;font-family:verdana,arial,helvetica,sans-serif;padding:1px 4px;"&gt;Home&lt;/a&gt;&lt;/b&gt;&lt;/font&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/v.gif) repeat-y;" width="6"&gt;&lt;br /&gt;&lt;/td&gt;&lt;td&gt;&lt;font size="1"&gt;&lt;b&gt;&lt;a href="/go/toolbar/-/tv/" style="color:#ffffff;text-decoration:none;font-family:verdana,arial,helvetica,sans-serif;padding:1px 4px;"&gt;TV&lt;/a&gt;&lt;/b&gt;&lt;/font&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/v.gif) repeat-y;" width="6"&gt;&lt;br /&gt;&lt;/td&gt;&lt;td&gt;&lt;font size="1"&gt;&lt;b&gt;&lt;a href="/go/toolbar/-/radio/" style="color:#ffffff;text-decoration:none;font-family:verdana,arial,helvetica,sans-serif;padding:1px 4px;"&gt;Radio&lt;/a&gt;&lt;/b&gt;&lt;/font&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/v.gif) repeat-y;" width="6"&gt;&lt;br /&gt;&lt;/td&gt;&lt;td&gt;&lt;font size="1"&gt;&lt;b&gt;&lt;a href="/go/toolbar/-/talk/" style="color:#ffffff;text-decoration:none;font-family:verdana,arial,helvetica,sans-serif;padding:1px 4px;"&gt;Talk&lt;/a&gt;&lt;/b&gt;&lt;/font&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/v.gif) repeat-y;" width="6"&gt;&lt;br /&gt;&lt;/td&gt;&lt;td&gt;&lt;font size="1"&gt;&lt;b&gt;&lt;a href="/go/toolbar/-/whereilive/" style="color:#ffffff;text-decoration:none;font-family:verdana,arial,helvetica,sans-serif;padding:1px 4px;"&gt;Where&amp;nbsp;I&amp;nbsp;Live&lt;/a&gt;&lt;/b&gt;&lt;/font&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/v.gif) repeat-y;" width="6"&gt;&lt;br /&gt;&lt;/td&gt;&lt;td&gt;&lt;nobr&gt;&lt;font size="1"&gt;&lt;b&gt;&lt;a href="/go/toolbar/-/a-z/" style="color:#ffffff;text-decoration:none;font-family:verdana,arial,helvetica,sans-serif;padding:1px 4px;"&gt;A-Z&amp;nbsp;Index&lt;/a&gt;&lt;/b&gt;&lt;/font&gt;&lt;/nobr&gt;&lt;/td&gt;&lt;td style="background:#666666 url(/images/sl3.gif) no-repeat;" width="8"&gt;&lt;br /&gt;&lt;/td&gt;&lt;td style="background:#666666 url(/images/st.gif) repeat-x 0 0;"&gt;&lt;input type="text" id="bbcpageSearchbox" name="q" size="6" style="margin:3px 0 0;font-family:arial,helvetica,sans-serif;width:100px;" title="BBC Search" /&gt;&lt;/td&gt;&lt;td style="background:#666666 url(/images/st.gif) repeat-x;"&gt;&lt;input type="image" src="/images/srchb.gif" name="go" value="go" alt="Search" width="64" height="25" border="0" /&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/sra.gif) no-repeat;" width="1"&gt;&lt;img src="/f/t.gif" width="1" height="30" alt="" /&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/td&gt;&lt;td style="background:#999999 url(/images/srb.gif) no-repeat;"&gt;&lt;img src="/f/t.gif" width="1" height="1" alt="" /&gt;&lt;input type="hidden" name="uri" value="/news.html" /&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/form&gt;&lt;tr&gt;&lt;td colspan="2" style="background-color:#000000;"&gt;&lt;img src="/f/t.gif" width="770" height="1" alt="" /&gt;&lt;/td&gt;&lt;td width="100%" style="background-color:#000000;"&gt;&lt;img src="/f/t.gif" width="1" height="1" alt="" /&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;!-- end toolbar 1.4 --&gt;

&lt;table cellspacing="0" cellpadding="8" border="0" width="770" bgcolor="#cccccc"&gt;&lt;tr&gt;&lt;td width="335"&gt;&lt;font size="-2" face="arial,helvetica"&gt;TUESDAY&lt;br /&gt;29th March 2005&lt;br /&gt;&lt;a href="/cgi-bin/education/betsie/parser.pl"&gt;Text only&lt;/a&gt; &lt;/font&gt;&lt;/td&gt;&lt;td width="435"&gt;&lt;h1&gt;404&lt;/h1&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;
&lt;div class="main"&gt;
&lt;div align="center"&gt;
&lt;h2&gt;Page not found&lt;/h2&gt;
&lt;p&gt;Unfortunately the following page was not available:&lt;br /&gt;
&lt;em&gt;http://www.bbc.co.uk/news.html&lt;/em&gt;&lt;/p&gt;
&lt;/div&gt;
&lt;h3&gt;This might be because:&lt;/h3&gt;
&lt;ul&gt;&lt;li&gt;You may have typed the web address incorrectly. Please check the address and spelling ensuring that it does &lt;b&gt;not&lt;/b&gt; contain capital letters or spaces&lt;/li&gt;
&lt;li&gt;It is possible that the page you were looking for may have been moved, updated or deleted.&lt;/li&gt;&lt;/ul&gt;

&lt;h3&gt;Please try the following options instead:&lt;/h3&gt;

&lt;form action="/cgi-bin/search/results.pl"&gt;
&lt;table cellpadding="4" cellspacing="2" border="0" align="center" bgcolor="#000000"&gt;
&lt;tr&gt;&lt;td bgcolor="#99ccff"&gt;&lt;h4&gt;Search bbc.co.uk&lt;/h4&gt;&lt;/td&gt;&lt;/tr&gt;
&lt;tr&gt;&lt;td bgcolor="#ffffcc"&gt;&lt;input type="text" name="q" size="45" /&gt;&amp;nbsp;&lt;input type="submit" value="Go" /&gt;&lt;/td&gt;&lt;/tr&gt;
&lt;/table&gt;
&lt;/form&gt;

&lt;ul&gt;
&lt;li&gt;Return to the &lt;a href="/"&gt;bbc.co.uk Home Page&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Use our &lt;a href="/a-z/"&gt;site index&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;If you still encounter problems then please try the &lt;a href="/help/"&gt;help&lt;/a&gt; section.&lt;/li&gt;
&lt;/ul&gt;

&lt;/div&gt;
&lt;!-- inc.footer.page --&gt;&lt;br clear="all" /&gt;&lt;table width="770" cellpadding="0" cellspacing="0" border="0"&gt;&lt;tr&gt;&lt;td width="110"&gt;&lt;img src="/furniture/tiny.gif" alt="" width="110" height="1"&gt;&lt;/td&gt;&lt;td width="10"&gt;&lt;img src="/furniture/tiny.gif" alt="" width="10" height="1"&gt;&lt;/td&gt;&lt;td align="center" width="100%"&gt;&lt;font face="arial, helvetica, sans-serif" size="1"&gt;&lt;a href="/terms/"&gt;Terms of Use&lt;/a&gt; | &lt;a href="/privacy/"&gt;Privacy&lt;/a&gt;&lt;/font&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;!-- end inc.footer.page --&gt;

&lt;/body&gt;
&lt;/html&gt;
</t>
<t tx="ekr.20050329082101.69">Produces documentation for a module

@auto-doc &lt;module name&gt;</t>
<t tx="ekr.20050329082101.70"></t>
<t tx="ekr.20050329082101.71">Base class for Docutils components.</t>
<t tx="ekr.20050329082101.72"></t>
<t tx="ekr.20050329082101.73">tuple() -&gt; an empty tuple
tuple(sequence) -&gt; tuple initialized from sequence's items

If the argument is a tuple, the return value is the same object.</t>
<t tx="ekr.20050329082101.74">
        Is `format` supported by this component?

        To be used by transforms to ask the dependent component if it supports
        a certain input context or output format.
        </t>
<t tx="ekr.20050329082101.75"></t>
<t tx="ekr.20050329082101.76">No documentation for OPTCRE</t>
<t tx="ekr.20050329082101.77">No documentation for SECTCRE</t>
<t tx="ekr.20050329082101.78">Create a new section in the configuration.

        Raise DuplicateSectionError if a section by the specified name
        already exists.
        </t>
<t tx="ekr.20050329082101.79">tuple() -&gt; an empty tuple
tuple(sequence) -&gt; tuple initialized from sequence's items

If the argument is a tuple, the return value is the same object.</t>
<t tx="ekr.20050329082101.80">dict() -&gt; new empty dictionary.
dict(mapping) -&gt; new dictionary initialized from a mapping object's
    (key, value) pairs.
dict(seq) -&gt; new dictionary initialized as if via:
    d = {}
    for k, v in seq:
        d[k] = v
dict(**kwargs) -&gt; new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)</t>
<t tx="ekr.20050329082101.81">
    Parser for command-line and library use.  The `settings_spec`
    specification here and in other Docutils components are merged to build
    the set of command-line options and runtime settings for this process.

    Common settings (defined below) and component-specific settings must not
    conflict.  Short options are reserved for common settings, and components
    are restrict to using long options.
    </t>
<t tx="ekr.20050329082101.82">str(object) -&gt; string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.</t>
<t tx="ekr.20050329082101.83">tuple() -&gt; an empty tuple
tuple(sequence) -&gt; tuple initialized from sequence's items

If the argument is a tuple, the return value is the same object.</t>
<t tx="ekr.20050329082101.84">dict() -&gt; new empty dictionary.
dict(mapping) -&gt; new dictionary initialized from a mapping object's
    (key, value) pairs.
dict(seq) -&gt; new dictionary initialized as if via:
    d = {}
    for k, v in seq:
        d[k] = v
dict(**kwargs) -&gt; new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)</t>
<t tx="ekr.20050329082101.85">tuple() -&gt; an empty tuple
tuple(sequence) -&gt; tuple initialized from sequence's items

If the argument is a tuple, the return value is the same object.</t>
<t tx="ekr.20050329082101.86">list() -&gt; new list
list(sequence) -&gt; new list initialized from sequence's items</t>
<t tx="ekr.20050329082101.87">list() -&gt; new list
list(sequence) -&gt; new list initialized from sequence's items</t>
<t tx="ekr.20050329082101.88">dict() -&gt; new empty dictionary.
dict(mapping) -&gt; new dictionary initialized from a mapping object's
    (key, value) pairs.
dict(seq) -&gt; new dictionary initialized as if via:
    d = {}
    for k, v in seq:
        d[k] = v
dict(**kwargs) -&gt; new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)</t>
<t tx="ekr.20050329082101.89">str(object) -&gt; string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.</t>
<t tx="ekr.20050329082101.90">
    A facade encapsulating the high-level logic of a Docutils system.
    </t>
<t tx="ekr.20050329082101.91">str(object) -&gt; string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.</t>
<t tx="ekr.20050329082101.92">str(object) -&gt; string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.</t>
<t tx="ekr.20050329082101.93">
Command-line and common processing for Docutils front-end tools.

Exports the following classes:

- `OptionParser`: Standard Docutils command-line processing.
- `Values`: Runtime settings; objects are simple structs
  (``object.attribute``).
- `ConfigParser`: Standard Docutils config file processing.
</t>
<t tx="ekr.20050329082101.94">
I/O classes provide a uniform API for low-level input and output.  Subclasses
will exist for a variety of input/output mechanisms.
</t>
<t tx="ekr.20050329082101.95">
This package contains Docutils parser modules.
</t>
<t tx="ekr.20050329082101.96">
    Set up &amp; run a `Publisher`.  For command-line front ends.

    Parameters:

    - `reader`: A `docutils.readers.Reader` object.
    - `reader_name`: Name or alias of the Reader class to be instantiated if
      no `reader` supplied.
    - `parser`: A `docutils.parsers.Parser` object.
    - `parser_name`: Name or alias of the Parser class to be instantiated if
      no `parser` supplied.
    - `writer`: A `docutils.writers.Writer` object.
    - `writer_name`: Name or alias of the Writer class to be instantiated if
      no `writer` supplied.
    - `settings`: Runtime settings object.
    - `settings_spec`: Extra settings specification; a `docutils.SettingsSpec`
      subclass.  Used only if no `settings` specified.
    - `settings_overrides`: A dictionary containing program-specific overrides
      of component settings.
    - `enable_exit`: Boolean; enable exit status at end of processing?
    - `argv`: Command-line argument list to use instead of ``sys.argv[1:]``.
    - `usage`: Usage string, output if there's a problem parsing the command
      line.
    - `description`: Program description, output for the "--help" option
      (along with command-line option descriptions).
    </t>
<t tx="ekr.20050329082101.97">
    Set up &amp; run a `Publisher`.  For programmatic use with file-like I/O.

    Parameters:

    - `source`: A file-like object (must have "read" and "close" methods).
    - `source_path`: Path to the input file.  Opened if no `source` supplied.
      If neither `source` nor `source_path` are supplied, `sys.stdin` is used.
    - `destination`: A file-like object (must have "write" and "close"
      methods).
    - `destination_path`: Path to the input file.  Opened if no `destination`
      supplied.  If neither `destination` nor `destination_path` are supplied,
      `sys.stdout` is used.
    - `reader`: A `docutils.readers.Reader` object.
    - `reader_name`: Name or alias of the Reader class to be instantiated if
      no `reader` supplied.
    - `parser`: A `docutils.parsers.Parser` object.
    - `parser_name`: Name or alias of the Parser class to be instantiated if
      no `parser` supplied.
    - `writer`: A `docutils.writers.Writer` object.
    - `writer_name`: Name or alias of the Writer class to be instantiated if
      no `writer` supplied.
    - `settings`: Runtime settings object.
    - `settings_spec`: Extra settings specification; a `docutils.SettingsSpec`
      subclass.  Used only if no `settings` specified.
    - `settings_overrides`: A dictionary containing program-specific overrides
      of component settings.
    - `enable_exit`: Boolean; enable exit status at end of processing?
    </t>
<t tx="ekr.20050329082101.98">
    Set up &amp; run a `Publisher`, and return the string output.
    For programmatic use with string I/O.

    For encoded string output, be sure to set the "output_encoding" setting to
    the desired encoding.  Set it to "unicode" for unencoded Unicode string
    output.  Here's how::

        publish_string(..., settings_overrides={'output_encoding': 'unicode'})

    Similarly for Unicode string input (`source`)::

        publish_string(..., settings_overrides={'input_encoding': 'unicode'})

    Parameters:

    - `source`: An input string; required.  This can be an encoded 8-bit
      string (set the "input_encoding" setting to the correct encoding) or a
      Unicode string (set the "input_encoding" setting to "unicode").
    - `source_path`: Path to the file or object that produced `source`;
      optional.  Only used for diagnostic output.
    - `destination_path`: Path to the file or object which will receive the
      output; optional.  Used for determining relative paths (stylesheets,
      source links, etc.).
    - `reader`: A `docutils.readers.Reader` object.
    - `reader_name`: Name or alias of the Reader class to be instantiated if
      no `reader` supplied.
    - `parser`: A `docutils.parsers.Parser` object.
    - `parser_name`: Name or alias of the Parser class to be instantiated if
      no `parser` supplied.
    - `writer`: A `docutils.writers.Writer` object.
    - `writer_name`: Name or alias of the Writer class to be instantiated if
      no `writer` supplied.
    - `settings`: Runtime settings object.
    - `settings_spec`: Extra settings specification; a `docutils.SettingsSpec`
      subclass.  Used only if no `settings` specified.
    - `settings_overrides`: A dictionary containing program-specific overrides
      of component settings.
    - `enable_exit`: Boolean; enable exit status at end of processing?
    </t>
<t tx="ekr.20050329082101.99">
This package contains Docutils Reader modules.
</t>
<t tx="ekr.20050329082101.100">This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

exitfunc -- if sys.exitfunc exists, this routine is called when Python exits
  Assigning to sys.exitfunc is deprecated; use the atexit module instead.

stdin -- standard input file object; used by raw_input() and input()
stdout -- standard output file object; used by the print statement
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

exc_type -- type of exception currently being handled
exc_value -- value of exception currently being handled
exc_traceback -- traceback of exception currently being handled
  The function exc_info() should be used instead of these three,
  because it is thread-safe.

Static objects:

maxint -- the largest supported integer (the smallest is -maxint-1)
maxunicode -- the largest supported character
builtin_module_names -- tuple of module names built into this interpreter
version -- the version of this interpreter as a string
version_info -- version information as a tuple
hexversion -- version information encoded as a single integer
copyright -- copyright notice pertaining to this interpreter
platform -- platform identifier
executable -- pathname of this Python interpreter
prefix -- prefix used to find the Python library
exec_prefix -- prefix used to find the machine-specific Python library
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in __builtin__._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exc_clear() -- clear the exception state for the current thread
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
setcheckinterval() -- control how often the interpreter checks for events
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
</t>
<t tx="ekr.20050329082101.101">
This package contains Docutils Writer modules.
</t>
<t tx="ekr.20050329082101.102"></t>
<t tx="ekr.20050329082101.103">Reads messages from a news server. Only does the last 10 as this is very slow ... it is only meant as an example. 

@auto-news &lt;news server name&gt;/&lt;news group name&gt;

</t>
<t tx="ekr.20050329082101.104">

Given some Python source, is there any tool which can tell the mimimum 
level of Python required to run that source? If I distribute some code, 
I need to be able to say which level of Python users require to run it.

-- 
Steve Toledo-Brown
Speaking for myself only.
Humans please use domain uk.ibm.com</t>
<t tx="ekr.20050329082101.105">

Disclaimer #1: I am a Python newbie, and I appreciate the vast
documentation at python.org -- some of which I expect has the answer to
my question if I can find it.

I am working on a custom computational fluid dynamics code.  I will
create one or more compiled Python modules in C/C++ to provide new
types and functions for manipulating those types.  I have a *lot* of
data.  Efficiency requires that the new data structures be shared
freely within the scope of the module, without directly exposing the
data to the standard Python runtime environment.

Stated another way, I need the data to persist in virtual memory across
seprate invocations of functions in the module(s) and to be accessible
only through methods explicitly provided by the module(s).

How can I do this?  What are some good examples to study?

Disclaimer #2: I am a aware that strong opinions exist about closing
off data from users.  But it's a requirement for this application.  I
don't like it, but I need the job!

Thanks for your time
CatManDo
</t>
<t tx="ekr.20050329082101.106">

Anand S Bisen wrote:
&gt; Hello
&gt; 
&gt; I have been developing a code that works pretty well on my python 2.3 
&gt; and now when i am running it on my server where it is programmed to run 
&gt; it's giving me errors. I have been using __contains__ method and it 
&gt; fails on python 2.2
&gt; 
&gt; For example
&gt; 
&gt; (Python 2.3)
&gt;  &gt;&gt; x="Hello World"
&gt;  &gt;&gt; print x.__contains__("Hello")
&gt; True
&gt; 
&gt; (Python 2.2)
&gt; 
&gt;  &gt;&gt;&gt; x="Hello world"
&gt;  &gt;&gt;&gt; print x.__contains__("Hello")
&gt; 
&gt; Traceback (most recent call last):
&gt;  File "&lt;stdin&gt;", line 1, in ?
&gt; TypeError: 'in &lt;string&gt;' requires character as left operand
&gt; 
&gt; 
&gt; Is there any woraround for this or what am i doing wrong in 2.2 ?
&gt; 
&gt; Thanks
&gt; 
Any use of double-underscores is an indication that magic is at work. In 
this case the __contains__ method is intended to be called by the 
interpreter when you write

     x in s

The __contains__ method was extended for strings in 2.3 so that 
construct could be used as a test to see whether s contained x as a 
substring. Before that, as the error message explains, it will only test 
to see whether a single character is contained in the string (by analogy 
with

     1 in [3, 4, 5, 2]

in case you are interested).

So you'll need to use the .find() string method and say

     if x.find("Hello") != -1:
         ... you found "Hello"

because your ISP appears to be using an older version of Python than you.

regards
  Steve
-- 
Meet the Python developers and your c.l.py favorites March 23-25
Come to PyCon DC 2005                      http://www.pycon.org/
Steve Holden                           http://www.holdenweb.com/</t>
<t tx="ekr.20050329082101.107">


"Zhang Le" &lt;sigu4wa02@sneakemail.com&gt; wrote in message 
news:1109952846.225378.136210@o13g2000cwo.googlegroups.com...
&gt; Hi,
&gt;  I did a small benchmark of matrix-vector multiply operation using
&gt; Numeric module. I'm a bit suprised to find matrix*col-vector is much
&gt; faster than row-vector*matrix. I wonder whether other people have
&gt; observed this fact too,

Yes, common knowledge in numerical analysis community.  Using the faster 
direction for a particular system as much as possible is part of tuning 
linear algebra software.

&gt; and why?

I presume that Numeric, like Python, stores matrices by row.  So M*v 
multiplies contiguous rows by a contiguous vector.  Multiplying a vector by 
non-contiguous columns requires requires skipping thru the matrix, which 
may require more computation and generate more cache misses and page 
faults.

Terry  J. Reedy


</t>
<t tx="ekr.20050329082101.108">

I just read in the 'What's New in Python 2.4' document that the None
data type was converted to a constant:
http://python.org/doc/2.4/whatsnew/node15.html

"""
# None is now a constant; code that binds a new value to the name
"None" is now a syntax error.
"""

So, what's the implications of this?  I find the lack of explanation a
little puzzling, since I've written code that compares a variable's
type with the 'None' type.  For example, a variable would be
initialized to 'None' and if it went through a loop unchanged, I could
determine this at the end by using a conditional type(var) ==
type(None).  What will type(None) return now?
</t>
<t tx="ekr.20050329082101.109">

On Fri, 4 Mar 2005 22:35:48 +0100, andrea_gavana@tin.it
&lt;andrea_gavana@tin.it&gt; wrote:
&gt; Hello NG,
&gt; 
&gt;     I was wondering if there is a way to obtain, from a list of floats,
&gt; a list of integers without loops. Probably is a basic question, but I can't
&gt; find an answer... I have had my eyes blinded by Matlab for years, but now
&gt; that I discovered Python+wxPython there seems to be no limit on what one
&gt; can do with these 2 tools. Anyway, following the Matlab style, I would like
&gt; to do something like this:
&gt; 
&gt; matrix = [1.5, 4.3, 5.5]
&gt; integer_matrix = int(matrix)       (float for Matlab)

You're going to have to use loops. I don't know how Matlab can do it
without them, unless it maintains the matrix as a list of floats and
simply *views* it as a list of ints. More likely, it simply hides the
loop away from you. Anyway, here's some ways to do it:

preferable: int_matrix = [int(x) for x in matrix]
old way: int_matrix = map(int, matrix)
explicit:
int_matrix = []
for x in matrix:
    int_matrix.append(int(x))

Any of these methods should be neither really slow nor really fast,
but the list comprehension should be the fastest (I think). Anyway, if
you're going to be doing lots of large matrices, and want some of your
old matlab stuff, check out numpy and numarray at
http://numeric.scipy.org/ .

Also, somebody was recently posting on here about a python &lt;-&gt; matlab
bridge that they developed; you should search the archives for that
(it was in february, I think).

And, finally, when doing scientific stuff, I found IPython
(http://ipython.scipy.org/) to be an invaluable tool. It's a much
improved Python interpreter.

Peace
Bill Mill
bill.mill at gmail.com

&gt; 
&gt; (In Matlab, "integer_matrix" is always a double anyway, here I would like
&gt; only to show the vector-matrix operation).
&gt; 
&gt; Obviously, Python complains about:
&gt; 
&gt; Traceback (most recent call last):
&gt;   File "&lt;interactive input&gt;", line 1, in ?
&gt; TypeError: int() argument must be a string or a number
&gt; 
&gt; I would like to avoid loops because, having been blinded by Matlab vector-matrix
&gt; abilities (and corresponding SLOW for-while loops operations), I tend to
&gt; think that also Python will be slow if I use loops.
&gt; 
&gt; Does anyone have a suggestion (or maybe could anyone show me that I'm wrong
&gt; about loops?)
&gt; 
&gt; Thanks you a lot.
&gt; 
&gt; Andrea.
&gt; 
&gt; --
&gt; http://mail.python.org/mailman/listinfo/python-list
&gt;</t>
<t tx="ekr.20050329082101.110">news-server.houston.rr.com/comp.lang.python</t>
<t tx="ekr.20050329082101.111">

This was happening to me for a while but stopped. I think it has to do with 
your mail server. Perhaps you could find another. If you are at a company, 
you might want to talk to your sysadmin and see if he can change the mail 
program. How did you get this latest message through? You know, with the 
proper email client you can have identities and such that have "from" and 
"return addresses" that are completely unrelated to the mail server you are 
using, if you would rather the mail list did not know about your most favored 
address.

James

On Friday 04 March 2005 01:56 pm, phil wrote:
&gt; everything I post to this list bounces awaiting moderator
&gt; approval, due to suspicious header.
&gt; COuld someone tell me what's wrong.  I'm on lots of list
&gt; with no problem.

-- 
James Stroud, Ph.D.
UCLA-DOE Institute for Genomics and Proteomics
Box 951570
Los Angeles, CA 90095</t>
<t tx="ekr.20050329082101.112">news-server.houston.rr.com/comp.lang.python</t>
<t tx="ekr.20050329082101.113">news-server.houston.rr.com/comp.lang.python</t>
<t tx="ekr.20050329082101.114"></t>
<t tx="ekr.20050329082101.146"></t>
<t tx="ekr.20050329092553">Hundreds die in Indonesia quake

Hundreds are believed to have died in Indonesia after a strong earthquake which sparked fears of a tsunami.</t>
<t tx="ekr.20050329092553.1">Ousted Kyrgyz preshttp://news.bbc.co.uk/1/hi/world/asia-pacific/4391139.stment defiant

Ousted Kyrgyz leader Askar Akayev says he remains the "sole legitimate preshttp://news.bbc.co.uk/1/hi/world/asia-pacific/4391139.stment" of his country.</t>
<t tx="ekr.20050329092553.2">Hair 'good source of stem cells'

Scientists have found hair follicles are a plentiful source of stem cells, which can become body tissue.</t>
<t tx="ekr.20050329092553.3">Ashdown sacks top Bosnian Croat

The top administrator in Bosnia, Lord Ashdown, sacks the Croat member of Bosnia's joint preshttp://news.bbc.co.uk/1/hi/world/europe/4390635.stmency.</t>
<t tx="ekr.20050329092553.4">Splits paralyse Iraqi parliament

Iraq's parliament reconvenes, but remains deadlocked over the formation of a new government.</t>
<t tx="ekr.20050329092553.5">Mongolians protest for new poll

Activists in Mongolia call for fresh elections, 
in an action apparently inspired by the situation in Kyrgyzstan.</t>
<t tx="ekr.20050329092553.6">Libya's Bulgarian medics appeal

Six medics appeal against the death sentence imposed in Libya for deliberately infecting children with HIV.</t>
<t tx="ekr.20050329092553.7">Schiavo rivals 'agree to autopsy'

Terri Schiavo's husband and parents seek to discover the extent of her brain-damage after her death.</t>
<t tx="ekr.20050329092553.8">Would-be sex tourist, 87, jailed

An octogenarian US man is jailed for 20 years for trying to travel to the Philippines for sex with young girls.</t>
<t tx="ekr.20050329092553.9">Golf: Funk claims Players title

Fred Funk's final-round 70 gives him victory in the lucrative Players Championship at Sawgrass.</t>
<t tx="ekr.20050329092553.10">Cricket: Series win for Aussies

Australia beat New Zealand by nine wickets in the third Test to wrap up a 2-0 series win.</t>
<t tx="ekr.20050329092553.11">Angola says virus 'under control'

Angola says an outbreak of the deadly Marburg virus is under control as DR Congo takes precautions.</t>
<t tx="ekr.20050329092553.12">Mugabe criticises MDC 'traitors'

Preshttp://news.bbc.co.uk/1/hi/world/africa/4391087.stment Mugabe condemns opposition supporters as traitors, as parliamentary elections draw near.</t>
<t tx="ekr.20050329092553.13">Ex-US diplomats round on Bolton

Dozens of former US diplomats urge Congress to block the appointment of John Bolton as UN ambassador.</t>
<t tx="ekr.20050329092553.14">Brazil quits loan accord with IMF

Brazil announces it will not renew a $41.75bn loan accord with the International Monetary Fund.</t>
<t tx="ekr.20050329092553.15">Japanese economy hit by weak data

An unexpected rise in Japan's jobless rate and falls in household spending and retail sales hit Japanese stocks.</t>
<t tx="ekr.20050329092553.16">Donors pledge $40m for KR trials

A UN-supported Khmer Rouge tribunal, due to try Cambodia's rulers from the 1970s, could open soon.</t>
<t tx="ekr.20050329092553.17">Three Romanians missing in Iraq

Three Romanian journalists are missing, feared khttp://news.bbc.co.uk/1/hi/world/middle_east/4389391.stmnapped, in Iraq after one called on a mobile.</t>
<t tx="ekr.20050329092553.18">Wolfowitz 'to meet EU officials'

Paul Wolfowitz, the US's controversial nomination to head the World Bank, is expected to meet with EU officials on Wednesday, reports say.</t>
<t tx="ekr.20050329092553.19">Knesset rejects Gaza referendum

Israel's parliament rejects an attempt by opponents of the planned Gaza pullout to force a referendum.</t>
<t tx="ekr.20050329092553.20">Militants to attend PLO meeting

Islamic Jihad is to sit in on a meeting of the top Palestinian decision-making body for the first time.</t>
<t tx="ekr.20050329092553.21">South Asia cancels tsunami alerts

India and Sri Lanka withdraw the tsunami alerts issued after an earthquake hit the coast of Indonesia.</t>
<t tx="ekr.20050329092553.22">Devastation as Afghan dam bursts

A dam has burst in south-eastern Afghanistan killing at least six people and causing whttp://news.bbc.co.uk/1/hi/world/south_asia/4391251.stmespread devastation, officials say.</t>
<t tx="ekr.20050329092553.23">Kyrgyzstan's friendly revolution

The BBC's Ian MacWilliam reports from Kyrgyzstan on an unusual people's revolution.</t>
<t tx="ekr.20050329092553.24">Followup on MS and Brazil in NY Times (mainpage, microsoft)

putko was one of dozens to submit a story running on the NY Times about Open Source and Brazil. The choice quote is "We're not going to spend taxpayers' money on a program so that Microsoft can further consolhttp://slashdot.org/article.pl?sid=05/03/29/1359253&amp;from=rssate its monopoly..."

http://slashdot.org/article.pl?shttp://slashdot.org/article.pl?sid=05/03/29/1359253&amp;from=rss=05/03/29/1359253&amp;from=rss</t>
<t tx="ekr.20050329092553.25">A9.com with Syndicated Search (mainpage, internet)

joeykiller writes "Search Engine Watch reports that Amazon now lets you add your own search to their A9 search engine. Users can opt-in to use additional search engines in addition to A9.com's own when searching. Amazon has chosen to use an extension of RSS 2.0 for this, and hopes that this format will enable search syndication in the same way RSS dhttp://slashdot.org/article.pl?sid=05/03/29/1337250&amp;from=rss for content. Several add-on searches are available already, among them New York Times, Wikipedia and NASA."

http://slashdot.org/article.pl?shttp://slashdot.org/article.pl?sid=05/03/29/1337250&amp;from=rss=05/03/29/1337250&amp;from=rss</t>
<t tx="ekr.20050329092553.26">What's Next At Apple (apple, apple)

pinqkandi writes "Business 2.0 is running a fascinating article on what might be coming up in Apple's future. Beshttp://apple.slashdot.org/article.pl?sid=05/03/29/132202&amp;from=rsses speculation, some interesting statistics are included, such as how the iPod should create equal revenue to the Mac for Apple in 2006, if not surpassing it. A good read for the Apple lover or loather."

http://apple.slashdot.org/article.pl?shttp://apple.slashdot.org/article.pl?sid=05/03/29/132202&amp;from=rss=05/03/29/132202&amp;from=rss</t>
<t tx="ekr.20050329092553.27">Berkeley Grads' Identity Data Stolen (yro, privacy)

yali writes "Dhttp://yro.slashdot.org/article.pl?sid=05/03/29/036237&amp;from=rss you get a graduate degree from Berkeley? Or maybe you just applied but dhttp://yro.slashdot.org/article.pl?sid=05/03/29/036237&amp;from=rssn't go there? If so, your http://yro.slashdot.org/article.pl?sid=05/03/29/036237&amp;from=rssentity may have been stolen. A laptop was stolen containing names, social security numbers, birthdates, and addresses of grad students, alumni, and applicants. University police suspect that the thief just wanted the laptop, but the irony of California's mandatory notification law is that the thief may now know they have something even more valuable. Berkeley has set up a website with information on the breach."

http://yro.slashdot.org/article.pl?shttp://yro.slashdot.org/article.pl?sid=05/03/29/036237&amp;from=rss=05/03/29/036237&amp;from=rss</t>
<t tx="ekr.20050329092553.28">South Korean Gov't. Advocates Linux (linux, linuxbiz)

Anonymous Coward writes "Korea has now taken the plunge on the Linux operating system, and is now starting to advocate Linux for use in government and public sector applications. South Korea's Ministry of Information and Communications announced the move today, which will result in decreased Microsoft market share in the region." According to the article, Korea's Ministry of Information and Communication "will provhttp://linux.slashdot.org/article.pl?sid=05/03/29/0322248&amp;from=rsse a total of 3 billion won (US$2.95 million) for government agencies which want to use the Linux and other open-source computer programs this year."

http://linux.slashdot.org/article.pl?shttp://linux.slashdot.org/article.pl?sid=05/03/29/0322248&amp;from=rss=05/03/29/0322248&amp;from=rss</t>
<t tx="ekr.20050329092553.29">MS, EU Agree on Name for Windows Sans Media Player (mainpage, windows)

An anonymous reader writes "Microsoft has agreed with European Union antitrust regulators on a new name for Windows software sold in Europe. Officials at the U.S. software giant sahttp://slashdot.org/article.pl?sid=05/03/28/1951251&amp;from=rss they had accepted the European Union's offer to call the European version of Windows sold without Media Player "Windows XP Home Edition N" - with "N" standing for "not with media player." Microsoft's "XP Professional Edition" will also include the "N" for versions sold without the media player. The prior nme for the OS was Windows XP Reduced Media Edition." News.com also mentions the choice.

http://slashdot.org/article.pl?shttp://slashdot.org/article.pl?sid=05/03/28/1951251&amp;from=rss=05/03/28/1951251&amp;from=rss</t>
<t tx="ekr.20050329092553.30">Blackbox (Finally) Updated (mainpage, gui)

mpeg4codec writes "OSNews reported earlier this month that the lightweight Blackbox window manager has been updated to 0.70. Among the new features are EWMH compliance, anti-aliased fonts, unicode support, and backwards compatibility with previous versions' styles. Of course, it brings you all these new features (well, some are optional) while retaining its small binary size, small memory footprint, and short list of dependencies. I for one think it's about time."

http://slashdot.org/article.pl?shttp://slashdot.org/article.pl?sid=05/03/29/0253245&amp;from=rss=05/03/29/0253245&amp;from=rss</t>
<t tx="ekr.20050329092553.31">Your Face On the Big Screen (mainpage, ent)

blamanj writes "In another case of SciFi becoming reality, you can now star in an animated film as your FutureCast (tm) face-scan is edited into the picture in real-time. John Brunner, in his Hugo-winning novel, Stand on Zanzibar predicted a similar development in television, lampooning people sitting at home while watching travologues of themselves 'on vacation.' Brunner, in addition to being an excellent writer, had some spot-on predictions of a virus-laden Internet in Shockwave Rhttp://slashdot.org/article.pl?sid=05/03/29/0123247&amp;from=rsser. Fortunately, the predictions of his eco-dystopia The Sheep Look Up have not come to pass. Yet."

http://slashdot.org/article.pl?shttp://slashdot.org/article.pl?sid=05/03/29/0123247&amp;from=rss=05/03/29/0123247&amp;from=rss</t>
<t tx="ekr.20050329092553.32">Ars Technica Builds Make Magazine's Steadicam (hardware, hardhack)

An anonymous reader writes "Make magazine has been out for a little over a month now and was given high marks in a Slashdot review. Ars Technica has taken their review one step further by building the $14 steadicam project and testing it out. (be sure to check out the QuickTime vhttp://hardware.slashdot.org/article.pl?sid=05/03/29/0056206&amp;from=rsseo at the end to see their results...)"

http://hardware.slashdot.org/article.pl?shttp://hardware.slashdot.org/article.pl?sid=05/03/29/0056206&amp;from=rss=05/03/29/0056206&amp;from=rss</t>
<t tx="ekr.20050329092553.33">New Photovoltaics Made with Titanium Foil (science, tech)

Memorize writes "A company called Daystartech has released a new type of photovoltaic cell which, unlike almost all the cells currently in use, does not silicon. This is based on a thin titanium film. Given the current shortage of solar-grade silicon, and all-time high oil prices, maybe titanium solar panels are here at the right time. The questions are, will they release it as a consumer solar product, and what will be the price per kilowatt hour?"

http://science.slashdot.org/article.pl?shttp://science.slashdot.org/article.pl?sid=05/03/28/2320211&amp;from=rss=05/03/28/2320211&amp;from=rss</t>
<t tx="ekr.20050402080206">@

This is LeoN-0.0.1 as created by Rodrigo Benenson, very slightly reorganized form.

An important project for Leo's long-term development.

See leo/doc/LeoN for important research papers that form the basis of this project.</t>
<t tx="ekr.20050402080206.1">@killcolor

Read the docustrings in the code.

Run the code LeoN.py to test it. 

You need to read sun98acheiving.pdf to understand what is all this stuff about.  This and other .pdf files are now in the leo/doc/LeoN folder.

Rodrigo Benenson. 2003. LeoN project. &lt;rodrigob@elo.utfsm.cl&gt;</t>
<t tx="ekr.20050402080206.2">@language plain

LeoN is Leo over the Network.

LeoN is Collaborative Leo.

Leo is http://leo.sf.net

@language plain

Leo over network requirements
-----------------------------

This is my résumé of the Requirements and design issues for Leo over the Network. (LeoN).

First in sake of simplicity a N-clients/One server architecture is imposed, being much more easy to design and implement.
Also it's required that the code could be as most Plugin as possible and as most python Modules independent as possible (one and only one instalation required).

Now, the list presented approximately in the logic order of implementation:

&lt;Step one, Merging&gt;

&lt;Step two, Publishing&gt;

&lt;Step three, Interacting by turns&gt;

&lt;&lt;Step four, Realtime interaction&gt;&gt;

Please comment this document.

RodrigoB. </t>
<t tx="ekr.20050402080206.3">Step four, "Realtime interaction":
- There should be a way that multiple online users edit on realtime the same Node.
This is the final step and is truly difficult. Probably this code should be merged from a parallel (but related) project.
(Guy X,Y,Z having a code party.)

- The client should show the editors cursors and edition on realtime.
Adquire the status, of Hydra Open Source, Multiplatform, Clone.
(Guy X,Y,Z enjoying the code party.)

Some features were intentionally omited:
- Versioning system. (there exists better solutions)
- Voice chat. (there exists parallel solutions)


</t>
<t tx="ekr.20050402080206.4">The realtime edition  could be implemented initially on a lock/unlock fashion automatized on a per line basis, very much like an online CVS editor...

The complications should be left to a parallel project, or maybe to another community (search, propose and merge/translate)

@nocolor</t>
<t tx="ekr.20050402080206.5">29/06/03

Hi!

It's time to news again. This last weeks were my final exams weeks but LeoN devellopment is going on as planned.

The last two weeks where focused on the Gui control, intercepting the whole list of actions that the user can do into the collaborative outline. There still some importants events to manage, but I think almost the base code is there. As mentioned this stage is absolutelly non trivial nor little; and is characterised to be some how frustating ("Tk marks are before or bellow a charater? Event occurs before or after effects?", and similars) and slow (because you have to test by hand the gui to debug it). The important elements missing will be done at the time it becomes strictly necessary.


The LeoN code is already pretty big and relativelly complex (3500 raw lines count) and there is a big list of things to do. Anyway no one said it would be easy.
Somes days ago I drafted the code base for Step4, hopefully the more important piece of code, due of it reusability and because I think it will give to LeoN an important sparky effect (near realtime multiuser text edition).


So now the actual plan is:
- Focus the next two weeks on the implementation of Step4 and his unit tests.
- Release the Step4 code. (because it is usefull without Leo and could be used in parallel projects)
- Integrate Step4 and Step(2,3) (one week)
- Move the code over Leo 3.1x  and Twisted 1.0.6 (which unfortunelly changed some classes used in LeoN (cred module)) (horizont: one week)
- After that I will focus strictly on finishing the usability elements and (if everything go fine) will start the releases iterations. This stage will have at least the following milestones:
	- Finish and debug the interface hooks (this can be long...)
	- Implement server persistence (should be easy)
	- Implement the admin interface (should be boring)
	- Implement Clones (two weeks if things go fine)
	- Improve the LeoN web views (implement more than one view  model?)
	- Allow as easy as possible instalations

Of course the releases will be all alpha during a probably long period until the devellopers are happy and then we will switch to beta and when everyone will be happy : the first stable Release !

I'm pretty impacient to finish the vapourware status of LeoN, we have the luck that the timing are acceptable, and Leo has some importants things to do before LeoN will become the first priority. This will give me the time to work on the mentioned plan.

RodrigoB.</t>
<t tx="ekr.20050402080206.6">As said, it is times to news. Briefly.

about step4
-----------

The code is ready and running since wednesday (mercredi) on the morning, but until now I'm  grumbling-grumbling with the code to get it working as supposed; I have found some minor bugs and solved some conceptuals problems and bugs. Debugging code of someelse algorithm is notoriously harder than working on your own ideas but the work give his fruits and each day we are one step nearer to us dreams.
Most of the hard problems are due to some ambiguities or not so clear ideas in the papers, so I have to crunch my brain to guess the correct way to manage the presented abstractions (or apply a 'guess, try, evaluate' strategy).

Due to this problems, and after five days of debugging work I will delay the code release until I get the unit test passed, this should not take more than a week more (I hope so, but you never know if the actual bug is or not the last one).


what is next
------------

- Finish debug of step4
- Implement and test the one server various clients collaborative editing (a special case of the above class)
- move codebase to 3.12b* and twisted 1.0.6
- merge step2, step3, step4 
- start the release of the code snapshots.
- start working on last frozen elements and on the Todo List:
	- hooks installations and debug (starting by node renaming)
	- admin interface
	- server side persistence 
	- clone support
	- cut and paste (with download interface)
	- better web server views
	- design a web plugin system ?
	- debugging, debugging
	- as easy as possible instalations
	- work on the design of LeoN2 features

I will stay working on a two weeks devellopment cycles, and post news at the end of each cycle.


RodrigoB.</t>
<t tx="ekr.20050402080206.7">@nocolor

25/06/03 Copying of the main algorithms into the code. RodrigoB.
01/07/03 Programming. RodrigoB.
02/07/03 Programming. RodrigoB.
05/07/03 Reading about the garbage collector stuff. RodrigoB.
07/07/03 Programming. RodrigoB.
08/07/03 Programming, operations herit from dict, support splitted ops, working on tests, syntax debugging. RodrigoB.
09/07/03 Implementing operations relations, starting debug iterations based on unittests.
		 Added another parameters form for receive_operation. RodrigoB.
10/07/03 Debugging conceptual aspects; management of timestamps on transformed operations. minor bugs fixed. Splitted special cases appears.RodrigoB.
12/07/03 Searching bugs. bugfixes. RodrigoB.
13/07/03 Implementing the garbage collector. Searching bugs. bugfixes. Testing garbage collector. RA problems. RodrigoB.
14/07/03 (vive la France!) Testing an idea (__eq__). Little edit to the root docustring. RodrigoB.
15/07/03 Hunting the Last Bug. Eureka. First successful execution. Code cleanup. Using unittest module. Release 1. RodrigoB.

Todo

- Find a good TestConcurrentEditable2 to test LostInformation cases

- LI is absolutelly not verified
- Find the Recover_LI specifications.
- Find a better way to quit the ambiguities on the 'if else {}' operation pertenence. (save_RA, save_LI conditions ?)

- collect garbage do not work anymore exactly like in the example. (is this a problem ?)

- Implement ConcurrentEditableServer
- Implement the  client-server tests

- Debug.

@color
@language python

</t>
<t tx="ekr.20050724100334">c.prettyPrintPythonNode()</t>
<t tx="ekr.20050817115636.2">import sys
sys.path.append(r'c:\reportlab_1_20') 

if 1: # This dependency could easily be removed.
    # Used only for tracing and error reporting.
    import leoGlobals as g
    
try:
    # from reportlab.lib.enums import *
    # from reportlab.platypus import *
    
    # Formatting imports...
    import docutils
    import reportlab.platypus
    import reportlab.platypus.para
    import stylesheet # To do: get this a better way.
    
    # General imports...
    import StringIO
    import time
    import types
except ImportError:
    pass



</t>
<t tx="ekr.20050817115636.4">class Writer (docutils.writers.Writer):
	
	&lt;&lt; class Writer declarations &gt;&gt;

	@others</t>
<t tx="ekr.20050817115636.5">supported = ('pdf','rlpdf')
"""Formats this writer supports."""

settings_spec = (
    'PDF-Specific Options',
    None,
    (
        # EKR: added this entry.
    (   'Specify a stylesheet URL, used verbatim.  Overrides '
        '--stylesheet-path.  Either --stylesheet or --stylesheet-path '
        'must be specified.',
        ['--stylesheet'],
        {'metavar': '&lt;URL&gt;', 'overrides': 'stylesheet_path'}),
         
    (   'Specify a stylesheet file, relative to the current working '
        'directory.  The path is adjusted relative to the output HTML '
        'file.  Overrides --stylesheet.',
        ['--stylesheet-path'],
        {'metavar': '&lt;file&gt;', 'overrides': 'stylesheet'}),

    (   'Format for footnote references: one of "superscript" or '
        '"brackets".  Default is "brackets".',
        ['--footnote-references'],
        {'choices': ['superscript', 'brackets'], 'default': 'brackets',
        'metavar': '&lt;FORMAT&gt;'}),
    )
)

output = None
"""Final translated form of `document`."""</t>
<t tx="ekr.20050817115636.6">def __init__(self):

    docutils.writers.Writer.__init__(self)

    # self.translator_class = PDFTranslator</t>
<t tx="ekr.20050817115636.7">def translate(self):
    
    '''Do final translation of self.document into self.output.'''
    
    if 1: # Production code.
        visitor = PDFTranslator(self,self.document)
    else: # Use intermediate file, and dummy pdf translator.
        # We can modify the intermediate file by hand to test proposed code generation.
        try:
            filename = 'intermediateFile.txt'
            s = file(filename).read()
            # g.trace('creating .pdf file from %s...' % filename)
            visitor = dummyPDFTranslator(self,self.document,s)
        except IOError:
            # g.trace('can not open %s' % filename)
            return

    # Create a list of paragraphs using Platypus.
    self.document.walkabout(visitor)
    story = visitor.as_what()
    
    if 0: # Not useful: story is a list of reportlab.platypus.para.Para objects.
        # Use the trace in createParagraph instead.
        g.trace('story','*'*40)
        print story        
    
    # Generate self.output.  Gets sent to reportlab.
    self.output = self.createPDF_usingPlatypus(story)
    # Solve the newline problem by brute force.
    self.output = self.output.replace('\n\r','\n')
    self.output = self.output.replace('\r\n','\n')
    if 0: # This is the actual .pdf output returned from doc.build(story)
        # doc is a Platypus (and this reportlab) document.
        g.trace('output','*'*40)
        lines = g.splitLines(self.output)
        g.printList(lines)</t>
<t tx="ekr.20050817115636.8">def createPDF_usingPlatypus (self,story):

    out = StringIO.StringIO()

    doc = reportlab.platypus.SimpleDocTemplate(out,
        pagesize=reportlab.lib.pagesizes.A4)

    doc.build(story)

    return out.getvalue()</t>
<t tx="ekr.20050817115636.9">def lower(self):

    return 'pdf'</t>
<t tx="ekr.20050817120850.1">@first #! /usr/bin/env python

&lt;&lt; docstring &gt;&gt;

# Note: you must copy this file to the Python/Lib/site-packages/docutils/writers folder.

@language python
@tabwidth -4

&lt;&lt; about this code &gt;&gt;
&lt;&lt; copyright &gt;&gt;
&lt;&lt; version history &gt;&gt;
&lt;&lt; to do &gt;&gt;

__version__ = '0.4'
__docformat__ = 'reStructuredText'
&lt;&lt; imports &gt;&gt;

@others</t>
<t tx="ekr.20050817120850.10">class PDFTranslator (docutils.nodes.NodeVisitor):

	@others

    depart_comment = invisible_visit
    visit_substitution_definition = visit_comment
    depart_substitution_definition = depart_comment
    visit_figure = visit_comment
    depart_figure = depart_comment

    visit_sidebar = invisible_visit
    visit_warning = invisible_visit
    visit_tip = invisible_visit
    visit_tbody = invisible_visit
    visit_thead = invisible_visit
    visit_tgroup = invisible_visit
    visit_table = invisible_visit
    visit_title_reference = invisible_visit
    visit_transition = invisible_visit
    visit_pending = invisible_visit
    depart_pending = invisible_visit
    depart_transition = invisible_visit
    depart_title_reference = invisible_visit
    depart_table = invisible_visit
    depart_tgroup = invisible_visit
    depart_thead = invisible_visit
    depart_tbody = invisible_visit
    depart_tip = invisible_visit
    depart_warning = invisible_visit
    depart_sidebar = invisible_visit</t>
<t tx="ekr.20050817120850.11">def __init__(self, writer,doctree):

    self.writer = writer
    self.settings = settings = doctree.settings
    self.styleSheet = stylesheet.getStyleSheet()
    docutils.nodes.NodeVisitor.__init__(self, doctree) # Init the base class.
    self.language = docutils.languages.get_language(doctree.settings.language_code)
    
    self.in_docinfo = False
    self.head = [] # Set only by meta() method.  
    self.body = [] # The body text being accumulated.
    self.foot = []
    self.sectionlevel = 0
    self.context = []
    
    self.story = []
    self.bulletText = '\267'
        # maybe move this into stylesheet.
        # This looks like the wrong glyph.

    if 0: # no longer used.
        self.topic_class = ''
        self.bulletlevel = 0
</t>
<t tx="ekr.20050817120850.12">def as_what(self):

    return self.story
</t>
<t tx="ekr.20050817120850.13">def encode(self, text):

    """Encode special characters in `text` &amp; return."""
    if type(text) is types.UnicodeType:
        text = text.replace(u'\u2020', u' ')
        text = text.replace(u'\xa0', u' ')
        text = text.encode('utf-8')
    #text = text.replace("&amp;", "&amp;amp;")
    #text = text.replace("&lt;", '"')
    #text = text.replace('"', "(quot)")
    #text = text.replace("&gt;", '"')
    # footnotes have character values above 128 ?
    return text
</t>
<t tx="ekr.20050817120850.14">def createParagraph (self,text,style='Normal',bulletText=None):

    if type(text) in (types.ListType,types.TupleType):
        text = ''.join([self.encode(t) for t in text])

    if not style.strip(): ### EKR
        style = 'Normal'
        
    if 0:
        s = text.split('&gt;')
        s = '&gt;\n'.join(s)
        print
        if 1: # just print the text.
            print s
        else:
            g.trace('%8s\n\n%s' % (style,s))
        print

    style = self.styleSheet [style]
    
    try:
        self.story.append(
            reportlab.platypus.para.Paragraph (
                self.encode(text), style,
                bulletText = bulletText,
                context = self.styleSheet))
    except Exception:
        g.es_print('Exception in createParagraph')
        g.es_exception()
        self.dumpContext()
        raise</t>
<t tx="ekr.20050817120850.15"># The suffix is always '\n' except for a cant-happen situation.

def starttag (self,node,tagname,suffix='\n',caller='',**attributes):
    
    # g.trace(repr(attributes))
    atts = {}
    for (name,value) in attributes.items():
        atts [name.lower()] = value
    for att in ('class',): # append to node attribute
        if node.has_key(att):
            if atts.has_key(att):
                atts [att] = node [att] + ' ' + atts [att]
    for att in ('id',): # node attribute overrides
        if node.has_key(att):
            atts [att] = node [att]
    
    attlist = atts.items() ; attlist.sort()
    parts = [tagname]
    # Convert the attributes in attlist to a single string.
    for name, value in attlist:
        # g.trace('attlist element:',repr(name),repr(value))
        if value is None: # boolean attribute
            parts.append(name.lower().strip())
        elif isinstance(value,types.ListType):
            values = [str(v) for v in value]
            val = ' '.join(values).strip()
            parts.append('%s="%s"' % (
                name.lower(), self.encode(val)))
        else:
            parts.append('%s="%s"' % (
                name.lower(),self.encode(str(value).strip())))

    val = '&lt;%s&gt;%s' % (' '.join(parts),suffix)
    # g.trace('%-24s %s' % (caller,val))
    return val</t>
<t tx="ekr.20050817120850.18">def visit_admonition(self, node, name):
    pass

def depart_admonition(self):
    pass
</t>
<t tx="ekr.20050817120850.20">def visit_attention(self, node):

    self.visit_admonition(node, 'attention')

def depart_attention(self, node):

    self.depart_admonition()
</t>
<t tx="ekr.20050817120850.22">def visit_author(self, node):
    self.visit_docinfo_item(node, 'author')

def depart_author(self, node):
    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.24">def visit_address(self, node):
    self.visit_docinfo_item(node, 'address')

def depart_address(self, node):
    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.26">def visit_version(self, node):
    self.visit_docinfo_item(node, 'version')

def depart_version(self, node):
    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.28">def visit_system_message(self, node):
    pass

def depart_system_message(self, node):
    pass
</t>
<t tx="ekr.20050817120850.30">def visit_term (self,node):

    self.push(kind='dt')

    self.body.append(
        self.starttag(node,'dt',suffix='',caller='visit_term'))

def depart_term (self,node):

    self.pop('dt')</t>
<t tx="ekr.20050817120850.32">def visit_authors(self, node):
    pass

def depart_authors(self, node):
    pass
</t>
<t tx="ekr.20050817120850.34">def visit_block_quote(self, node):
    pass
    
def depart_block_quote(self, node):
    pass</t>
<t tx="ekr.20050817120850.36">def visit_bullet_list(self, node):
    
    self.push(kind='ul',start=len(self.body))

    # At present self.bulletText is a constant.
    self.body.append('&lt;ul bulletText="%s"&gt;' % self.bulletText)

def depart_bullet_list(self, node):
    
    b = self.pop('ul')

    self.body.append('&lt;/ul&gt;')
    
    if not self.inContext('ul'):
        self.putTail(b.start)</t>
<t tx="ekr.20050817120850.39">def visit_caption(self, node):
    pass

def depart_caption(self, node):
    pass
</t>
<t tx="ekr.20050817120850.40">def visit_caution(self, node):
    self.visit_admonition(node, 'caution')

def depart_caution(self, node):
    self.depart_admonition()
</t>
<t tx="ekr.20050817120850.42">def visit_citation(self, node):
    pass

def depart_citation(self, node):
    pass
</t>
<t tx="ekr.20050817120850.44">def visit_citation_reference(self, node):
    pass

def depart_citation_reference(self, node):
    pass
</t>
<t tx="ekr.20050817120850.46">def visit_classifier(self, node):
    pass

def depart_classifier(self, node):
    pass
</t>
<t tx="ekr.20050817120850.48">def visit_colspec(self, node):
    pass

def depart_colspec(self, node):
    pass
</t>
<t tx="ekr.20050817120850.50">def visit_contact(self, node):
    
    self.visit_docinfo_item(node, 'contact')

def depart_contact(self, node):

    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.52">def visit_copyright(self, node):
    
    self.visit_docinfo_item(node, 'copyright')

def depart_copyright(self, node):

    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.54">def visit_danger(self, node):
    
    self.visit_admonition(node, 'danger')

def depart_danger(self, node):

    self.depart_admonition()
</t>
<t tx="ekr.20050817120850.56">def visit_date(self, node):
    
    self.visit_docinfo_item(node, 'date')

def depart_date(self, node):
    
    self.depart_docinfo_item()

</t>
<t tx="ekr.20050817120850.58">def visit_definition(self, node):
    
    self.push(kind='dd')

    self.body.append('&lt;/dt&gt;')
    self.body.append(
        self.starttag(node,'dd',caller='visit_destination'))

def depart_definition(self, node):
    
    self.pop('dd')
    self.body.append('&lt;/dd&gt;')</t>
<t tx="ekr.20050817120850.60">def visit_definition_list(self, node):
    
    self.push(kind='dl',start=len(self.body))
    
    self.body.append(self.starttag(node, 'dl'))

def depart_definition_list(self, node):
    
    b = self.pop('dl')

    self.body.append('&lt;/dl&gt;')

    if not self.inContext('dl'):
        self.putTail(b.start)
</t>
<t tx="ekr.20050817120850.62">def visit_definition_list_item(self, node):
    pass

def depart_definition_list_item(self, node):
    pass</t>
<t tx="ekr.20050817120850.64">def visit_description(self, node):
    pass

def depart_description(self, node):
    pass
</t>
<t tx="ekr.20050817120850.66"></t>
<t tx="ekr.20050817120850.68">def visit_docinfo_item(self, node, name):
    
    self.body.append(
        '&lt;para style="DocInfo"&gt;&lt;b&gt;%s: &lt;/b&gt;' % (
            self.language.labels[name]))

def depart_docinfo_item(self):
    
    self.body.append('&lt;/para&gt;')
</t>
<t tx="ekr.20050817120850.70">def visit_doctest_block(self, node):
    
    self.visit_literal_block(node)

def depart_doctest_block(self, node):
    
    self.depart_literal_block(node)

</t>
<t tx="ekr.20050817120850.72">def visit_line_block(self, node):
    self.visit_literal_block(node)

def depart_line_block(self, node):
    self.depart_literal_block(node)
</t>
<t tx="ekr.20050817120850.74">def visit_document(self, node):
    pass
    
def depart_document(self, node):
    pass</t>
<t tx="ekr.20050817120850.76">def visit_emphasis(self, node):
    
    self.push(kind='i')
    
    self.body.append('&lt;i&gt;')

def depart_emphasis(self, node):
    
    self.pop('i')

    self.body.append('&lt;/i&gt;')
</t>
<t tx="ekr.20050817120850.78">def visit_entry(self, node):
    pass

def depart_entry(self, node):
    pass
</t>
<t tx="ekr.20050817120850.80">def visit_enumerated_list(self, node):
    
    self.push(kind='ol',start=len(self.body))

    self.body.append('&lt;ol&gt;')

def depart_enumerated_list(self, node):
    
    b = self.pop('ol')

    self.body.append('&lt;/ol&gt;')

    if not self.inContext('ol'):
        self.putTail(b.start)</t>
<t tx="ekr.20050817120850.82">def visit_error(self, node):
    self.visit_admonition(node, 'error')

def depart_error(self, node):
    self.depart_admonition()</t>
<t tx="ekr.20050817120850.84">def visit_field(self, node):
    
    self.body.append('&lt;para&gt;')

def depart_field(self, node):

    self.body.append('&lt;/para&gt;')
</t>
<t tx="ekr.20050817120850.86">def visit_field_argument(self, node):
    pass

def depart_field_argument(self, node):
    pass
</t>
<t tx="ekr.20050817120850.88">def visit_field_list(self, node):
    
    self.push(kind='&lt;para&gt;',start=len(self.body))

def depart_field_list(self, node):
    
    b = self.pop('&lt;para&gt;')
    
    self.body.append('&lt;/para&gt;')
    
    self.putTail(b.start)</t>
<t tx="ekr.20050817120850.90">def visit_field_name(self, node):

    self.body.append('&lt;b&gt;')

def depart_field_name(self, node):

    self.body.append(': &lt;/b&gt;')</t>
<t tx="ekr.20050817120850.92">def visit_field_body(self, node):
    pass

def depart_field_body(self, node):
    pass
</t>
<t tx="ekr.20050817120850.94">def visit_footnote(self, node):
    
    self.push(kind='footnotes',context=[])

    self.footnote_backrefs(node)

def depart_footnote(self, node):
    
    self.pop('footnotes')

    self.footnote_backrefs_depart(node)
</t>
<t tx="ekr.20050817120850.95">@ Bug fixes, EKR 8/22/05:
    - Get attributes from node.attributes, not node.
    - The proper key is 'ids', not 'id'
Warning: this does not work for auto-numbered footnotes.
@c

def footnote_backrefs (self,node):
    
    '''Create b.link and b.setLink for visit/depart_label.'''
    
    # self.dumpNode(node,tag='backrefs-node')
    
    b = self.peek('footnotes')
    a = node.attributes ; backrefs = a.get('backrefs',[]) # EKR.

    # Set b.setLink.
    b.setLink = self.starttag(
        {},'setLink','',destination=a['ids']) # EKR.

    # Set b.links.
    b.links = []
    if self.settings.footnote_backlinks:
        for backref in backrefs:
            b.links.append(
                self.starttag(
                    {},'link',suffix='',destination=backref))</t>
<t tx="ekr.20050817120850.96">def footnote_backrefs_depart(self, node):

    if not self.context and self.body:
        self.createParagraph(self.body)
        self.body = []
</t>
<t tx="ekr.20050817120850.98">@ Bug fixes, EKR 8/22/05:
    - Get attributes from node.attributes, not node.
    - The proper key is 'ids', not 'id'
@c

def visit_footnote_reference (self,node):
    
    '''Generate code for a footnote reference.'''
    
    # self.dumpNode(node,tag='footnote-ref-node')

    markup = [] # The terminating markup to be supplied by depart_footnote_reference.
    a = node.attributes # EKR.
    if self.settings.footnote_backlinks and a.get('ids'):
        self.body.append(
            self.starttag(node,'setLink','',destination=a['ids']))
        markup.append('&lt;/setLink&gt;')
    
    if   node.hasattr('refid'):   href = a ['refid']
    elif node.hasattr('refname'): href = self.document.nameids [a ['refname']]
    else:                         href = ''
    # g.trace('href:',href)

    format = self.settings.footnote_references
    if format == 'brackets':
        suffix = '[' ; markup.append(']')
    elif format == 'superscript':
        suffix = '&lt;super&gt;' ; markup.append('&lt;/super&gt;')
    else: # shouldn't happen
        suffix = None

    if suffix:
        self.body.append(
            self.starttag(node,'link',suffix,destination=href))
        markup.append('&lt;/link&gt;')

    markup.reverse()
    self.push(kind='footnote-ref',markup=markup)</t>
<t tx="ekr.20050817120850.99">def depart_footnote_reference(self, node):
    
    b = self.pop('footnote-ref')
    
    for z in b.markup:
        self.body.append(z)</t>
<t tx="ekr.20050817120850.100">def visit_hint(self, node):
    self.visit_admonition(node, 'hint')

def depart_hint(self, node):
    self.depart_admonition()
</t>
<t tx="ekr.20050817120850.102">def visit_image(self, node):
    pass

def depart_image(self, node):
    pass
</t>
<t tx="ekr.20050817120850.105">def visit_important(self, node):
    self.visit_admonition(node, 'important')

def depart_important(self, node):
    self.depart_admonition()
</t>
<t tx="ekr.20050817120850.106">def visit_interpreted(self, node):
    pass

def depart_interpreted(self, node):
    pass
</t>
<t tx="ekr.20050817120850.108">def visit_label(self, node):
    
    b = self.inContext('footnotes')
    if b:
        self.body.append(b.setLink)
        self.body.append('&lt;/setLink&gt;')
        # Start all links.
        for link in b.links:
            self.body.append(link)
        self.body.append('[')

def depart_label(self, node):
    
    b = self.inContext('footnotes')
    if b:
        self.body.append(']')
        # End all links.
        for link in b.links:
            self.body.append('&lt;/link&gt;')
        # Who knows why this is here...
        self.body.append('   ')</t>
<t tx="ekr.20050817120850.110">def visit_legend(self, node):
    pass

def depart_legend(self, node):
    pass
</t>
<t tx="ekr.20050817120850.112">def visit_list_item(self, node):
    
    self.push(kind='li')
    
    self.body.append('&lt;li&gt;')

def depart_list_item(self, node):
    
    self.pop('li')

    self.body.append('&lt;/li&gt;')
</t>
<t tx="ekr.20050817120850.114">def visit_literal(self, node):
    
    self.push(kind='literal')
    
def depart_literal(self, node):
    
    self.pop('literal')</t>
<t tx="ekr.20050817120850.116">def visit_literal_block(self, node):
    
    self.story.append(
        reportlab.platypus.Preformatted(
            node.astext(),self.styleSheet['Code']))

    raise docutils.nodes.SkipNode

def depart_literal_block(self, node):
    pass</t>
<t tx="ekr.20050817120850.118">def visit_meta(self, node):
    
    g.trace(**node.attributes)

    self.head.append(
        self.starttag(node, 'meta', **node.attributes))

def depart_meta(self, node):

    pass</t>
<t tx="ekr.20050817120850.120">def visit_note(self, node):
    
    self.visit_admonition(node, 'note')

def depart_note(self, node):

    self.depart_admonition()
</t>
<t tx="ekr.20050817120850.122">def visit_option(self, node):
    pass

def depart_option(self, node):
    pass
</t>
<t tx="ekr.20050817120850.124">def visit_option_argument(self, node):
    pass

def depart_option_argument(self, node):
    pass
</t>
<t tx="ekr.20050817120850.126">def visit_option_group(self, node):
    pass

def depart_option_group(self, node):
    pass
</t>
<t tx="ekr.20050817120850.128">def visit_option_list(self, node):
    
    self.push(kind='option-list',start=len(self.body))

def depart_option_list(self, node):
    
    b = self.pop('option-list')

    if not self.inContext('option_list'):
        self.putTail(b.start)
        </t>
<t tx="ekr.20050817120850.130">def visit_option_list_item(self, node):
    pass

def depart_option_list_item(self, node):
    pass
</t>
<t tx="ekr.20050817120850.132">def visit_option_string(self, node):
    pass

def depart_option_string(self, node):
    pass
</t>
<t tx="ekr.20050817120850.134">def visit_organization(self, node):
    
    self.visit_docinfo_item(node, 'organization')

def depart_organization(self, node):

    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.138">def visit_problematic(self, node):
    pass

def depart_problematic(self, node):
    pass
</t>
<t tx="ekr.20050817120850.140">def visit_raw(self, node):

    if node.has_key('format') and node['format'] == 'html':
        self.body.append(node.astext())

    raise docutils.nodes.SkipNode
</t>
<t tx="ekr.20050817120850.141">def visit_target (self,node):

    if not (
        node.has_key('refuri') or
        node.has_key('refid') or
        node.has_key('refname')
    ):
        href = ''
        if node.has_key('id'):
            href = node ['id']
        elif node.has_key('name'):
            href = node ['name']
        self.body.append("%s%s" % (
            self.starttag(node,'setLink',suffix='',
                destination=href,caller='visit_targtet'),
            '&lt;/setLink&gt;'))
    raise docutils.nodes.SkipNode

def depart_target (self,node):
    pass</t>
<t tx="ekr.20050817120850.143">def visit_reference (self,node):

    markup = [] ; caller = 'visit_reference'

    if node.has_key('refuri'):
        href = node ['refuri']
        self.body.append(
            self.starttag(node,'a',suffix='',href=href,caller=caller))
        markup.append('&lt;/a&gt;')
    else:
        if node.has_key('id'):
            self.body.append(
                self.starttag({},'setLink','',
                    destination=node['id'],caller=caller))
            markup.append('&lt;/setLink&gt;')
        if node.has_key('refid'):
            href = node ['refid']
        elif node.has_key('refname'):
            href = self.document.nameids [node ['refname']]
        self.body.append(
            self.starttag(node,'link','',destination=href,caller=caller))
        markup.append('&lt;/link&gt;')

    self.push(kind='a',markup=markup)
</t>
<t tx="ekr.20050817120850.144">def depart_reference(self, node):
    
    b = self.pop('a')

    for s in b.markup:
        self.body.append(s)</t>
<t tx="ekr.20050817120850.145">def visit_revision(self, node):

    self.visit_docinfo_item(node, 'revision')

def depart_revision(self, node):

    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.147">def visit_row(self, node):
    pass

def depart_row(self, node):
    pass
</t>
<t tx="ekr.20050817120850.149">def visit_section(self, node):
    
    self.sectionlevel += 1

def depart_section(self, node):

    self.sectionlevel -= 1
</t>
<t tx="ekr.20050817120850.151">def visit_status(self, node):
    
    self.visit_docinfo_item(node, 'status')

def depart_status(self, node):

    self.depart_docinfo_item()
</t>
<t tx="ekr.20050817120850.153">def visit_strong(self, node):
    
    self.push(kind='b')

    self.body.append('&lt;b&gt;')

def depart_strong(self, node):
    
    self.pop('b')

    self.body.append('&lt;/b&gt;')

</t>
<t tx="ekr.20050817120850.155">def visit_subtitle(self, node):
    
    self.push(kind='subtitle',start=len(self.body))

def depart_subtitle(self, node):
    
    b = self.pop('subtitle')

    self.putTail(b.start,b.style)
</t>
<t tx="ekr.20050817120850.157">def visit_title (self,node):

    caller='visit_title'
    start = len(self.body) ; markup = []
    isTopic = isinstance(node.parent,docutils.nodes.topic)
    isTitle = self.sectionlevel == 0
    
    # Set the style.
    if isTopic:   style = 'topic-title'
    elif isTitle: style = 'title'
    else:         style = "h%s" % self.sectionlevel

    ## The old code was equivalent to: if style != 'title'.
    if 0:
        self.dumpNode(node.parent,tag='node.parent')
        self.dumpNode(node,tag='node')
    # Bug fix: 8/21/05: changed 'id' to 'ids'.
    if node.parent.hasattr('ids'):
        self.body.append(
        self.starttag({},'setLink','',
            destination=node.parent['ids'],caller=caller))
        markup.append('&lt;/setLink&gt;')
    if node.hasattr('refid'):
        self.body.append(
        self.starttag({},'setLink','',
            destination=node['refid'],caller=caller))
        markup.append('&lt;/setLink&gt;')

    self.push(kind='title',markup=markup,start=start,style=style)</t>
<t tx="ekr.20050817120850.158">def depart_title (self,node):

    b = self.pop('title')

    for z in b.markup:
        self.body.append(z)
        
    self.putTail(b.start,style=b.style)</t>
<t tx="ekr.20050817120850.159">def unimplemented_visit(self, node):
    
    raise NotImplementedError(
        'visiting unimplemented node type: %s' % node.__class__.__name__)
</t>
<t tx="ekr.20050817120850.160">def visit_topic (self,node):

    if node.hasattr('id'):
        self.push(kind='topic-id',markup='&lt;/setLink&gt;')
        self.body.append(self.starttag({},'setLink',
            suffix='',destination=node['id'],caller='visit_topic'))

def depart_topic (self,node):

    if node.hasattr('id'):
        b = self.pop('topic-id')
        self.body.append(b.markup)

</t>
<t tx="ekr.20050817120850.162">def visit_generated(self, node):
    pass

def depart_generated(self, node):
    pass
</t>
<t tx="ekr.20050817120850.164">def invisible_visit(self, node):
    
    """Invisible nodes should be ignored."""
    pass</t>
<t tx="ekr.20050817120850.165">def visit_comment(self, node):

    raise docutils.nodes.SkipNode
</t>
<t tx="ekr.20050817122915">'''This NOT a Leo plugin: this is a docutils writer for .pdf files.  

That file uses the reportlab module to convert html markup to pdf.

The original code written by Engelbert Gruber.

Rewritten by Edward K. Ream for the Leo rst3 plugin.
'''
</t>
<t tx="ekr.20050817124859">#####################################################################################
#
#	Copyright (c) 2000-2001, ReportLab Inc.
#	All rights reserved.
#
#	Redistribution and use in source and binary forms, with or without modification,
#	are permitted provided that the following conditions are met:
#
#		*	Redistributions of source code must retain the above copyright notice,
#			this list of conditions and the following disclaimer. 
#		*	Redistributions in binary form must reproduce the above copyright notice,
#			this list of conditions and the following disclaimer in the documentation
#			and/or other materials provided with the distribution. 
#		*	Neither the name of the company nor the names of its contributors may be
#			used to endorse or promote products derived from this software without
#			specific prior written permission. 
#
#	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#	IN NO EVENT SHALL THE OFFICERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#	INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
#	TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#	OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
#	IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
#	IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
#	SUCH DAMAGE.
#
#####################################################################################</t>
<t tx="ekr.20050817124859.1">@

- Added 'c:\reportlab_1_20' to sys.path.

- Obtained this file and stylesheet.py from
  http://docutils.sourceforge.net/sandbox/dreamcatcher/rlpdf/

- Put stylesheet.py in docutils/writers directory.
  This is a stylesheet class used by the file.

- Made minor mods to stop crashes.
    - Added support for the '--stylesheet' option.
        - This may be doing more harm than good.
    - Changed the following methods of the PDFTranslator class:
        - createParagraph
        - depart_title</t>
<t tx="ekr.20050817132814"></t>
<t tx="ekr.20050817135706">def visit_Text (self,node):

    self.push(kind='#text')

    self.body.append(node.astext())

def depart_Text (self,node):

    self.pop('#text')</t>
<t tx="ekr.20050817135706.1"></t>
<t tx="ekr.20050817142135">def visit_paragraph(self, node):
    
    self.push(kind='p',start=len(self.body))
    
def depart_paragraph(self, node):
    
    b = self.pop('p')
    
    if not self.context and self.body:
        self.putTail(b.start)</t>
<t tx="ekr.20050817142135.1"></t>
<t tx="ekr.20050817165745">@nocolor
@others</t>
<t tx="ekr.20050817165745.1">@

- Removed '\r' characters in Writer.translate.
- Created self.push and self.pop.
- Rewrote visit/depart_title.  The code now is clear and works properly.

To do:
    The code in several places uses x in self.context.
    This won't work when g.Bunches are on the context stack,
    so we shall need a method that searches the bunches on the stack.</t>
<t tx="ekr.20050818022030">def push (self,**keys):
    
    self.context.append(Bunch(**keys))
    
def pop (self,kind):
    
    bunch = self.context.pop()
    assert bunch.kind == kind,\
        'wrong bunch kind popped.  Expected: %s Got: %s' % (
            kind, bunch.kind)

    return bunch
    
def peek (self,kind):
    
    bunch = self.context[-1]
    assert bunch.kind == kind,\
        'peek at wrong bunch.  Expected: %s Got: %s' % (
            kind, bunch.kind)
    return bunch</t>
<t tx="ekr.20050818033610">@

- Fixed bug in visit_reference: added self.push(b).
- Added putHead, putTail utilities.
- Simplified most of the code.
- Reorganized node handlers so that it is clear what the important methods are.
- Almost all the grunt work is done.</t>
<t tx="ekr.20050818081715">def dumpContext (self):
    
    print ; print '-' * 40
    print 'Dump of context'
        
    i = 0
    for bunch in self.context:
        print '%2d %s' % (i,bunch)
        i += 1</t>
<t tx="ekr.20050818083045">def inContext (self,kind):
    
    '''Return the most recent bunch having the indicated kind, or None.'''
    
    i = len(self.context) - 1

    while i &gt;= 0:
        bunch = self.context[i]
        if bunch.kind == kind:
            return bunch
        i -= 1
        
    return None</t>
<t tx="ekr.20050818084920">def putHead (self,start,style='Normal',bulletText=None):
    
    self.createParagraph(self.body[:start],
        style=style,bulletText=bulletText)

    self.body = self.body[start:]


def putTail (self,start,style='Normal',bulletText=None):
    
    self.createParagraph(self.body[start:],
        style=style,bulletText=bulletText)

    self.body = self.body[:start]
</t>
<t tx="ekr.20050818090152"></t>
<t tx="ekr.20050818090152.1"></t>
<t tx="ekr.20050818090907"></t>
<t tx="ekr.20050818094118.1">def visit_docinfo(self, node):
    
    self.push(kind='docinfo',start=len(self.body))
    self.in_docinfo = True

def depart_docinfo(self, node):
    
    b = self.pop('docinfo')
    self.putHead(b.start)
    self.in_docinfo = False</t>
<t tx="ekr.20050818094118.2"></t>
<t tx="ekr.20050818094954"></t>
<t tx="ekr.20050818094954.1"></t>
<t tx="ekr.20050818095347">@

All grunt work completed:

- Moved Bunch class into this file (so no dependencies on leoGlobals.py).

- Simplified calls to self.push

- Finish all simple methods.

- Better dumps in createParagraph.</t>
<t tx="ekr.20050818103031">@nocolor

@others

@

- Bullets show up as a black 2 ball.

- More flexible handling of style sheets.

- Auto-footnote numbering does not work.

- Test rST raw: pdf feature.</t>
<t tx="ekr.20050818103441">@ From The Python Cookbook:  Often we want to just collect a bunch of stuff together, naming each item of the bunch; a dictionary's OK for that, but a small do-nothing class is even handier, and prettier to use.

Create a Bunch whenever you want to group a few variables:

    point = Bunch(datum=y, squared=y*y, coord=x)

You can read/write the named attributes you just created, add others, del some of them, etc:
    if point.squared &gt; threshold:
        point.isok = True
@c

class Bunch (object):
    
    """A class that represents a colection of things.
    
    Especially useful for representing a collection of related variables."""
    
    def __init__(self,**keywords):
        self.__dict__.update (keywords)
        
    def __repr__(self):
        return self.toString()

    def ivars(self):
        return self.__dict__.keys()
        
    def keys(self):
        return self.__dict__.keys()
        
    def toString(self):
        tag = self.__dict__.get('tag')
        entries = ["%s: %s" % (key,str(self.__dict__.get(key)))
            for key in self.ivars() if key != 'tag']
        if tag:
            return "Bunch(tag=%s)...\n%s\n" % (tag,'\n'.join(entries))
        else:
            return "Bunch...\n%s\n" % '\n'.join(entries)

    # Used by new undo code.
    def __setitem__ (self,key,value):
        '''Support aBunch[key] = val'''
        return operator.setitem(self.__dict__,key,value)
        
    def __getitem__ (self,key):
        '''Support aBunch[key]'''
        return operator.getitem(self.__dict__,key)
        
    def get (self,key,theDefault=None):
        return self.__dict__.get(key,theDefault)
        
bunch = Bunch</t>
<t tx="ekr.20050818105023"></t>
<t tx="ekr.20050818105023.1"></t>
<t tx="ekr.20050818130249"></t>
<t tx="ekr.20050819055746">c.save()</t>
<t tx="ekr.20050819055746.1">@

- Added dummyPDFTranslator class.

- Added support for this dummy class to Writer.translate.</t>
<t tx="ekr.20050819072001">def dumpNode (self,node,tag=''):
    
    &lt;&lt; define keys to be printed &gt;&gt;
    
    d = node.__dict__
    
    nkeys = d.keys() ; nkeys.sort()
    
    print ; print '-' * 30
    print 'dump of node %s\n' % (g.choose(tag,'(%s)' % tag,''))
    
    print 'class',node.__class__
    
    for nkey in nkeys:
        if nkey in keys:
            val = d.get(nkey)
            print nkey,':',g.toString(val,verbose=False,indent='\t')
            
    print ; print 'done', '-' * 25</t>
<t tx="ekr.20050819072001.1">keys = (
    #'anonymous_refs'
    #'anonymous_targets'
    'attributes'
    'autofootnote_refs'
    'autofootnote_start'
    'autofootnotes'
    #'children'
    #'citation_refs'
    #'citations'
    #'current_line'
    #'current_source'
    #'decoration'
    #'document'
    'footnote_refs'
    'footnotes'
    'id_start'
    'ids'  # keys are sectinon names, values are section objects or reference objects.
    'indirect_targets'
    'nameids' # This might be what we want: keys are section names, values are munged names.
    #'nametypes'
    #'parse_messages'
    #'rawsource'
    'refids'
    'refnames'
    #'reporter'
    #'settings'
    #'substitution_defs'
    #'substitution_names'
    #'substitution_refs'
    #'symbol_footnote_refs'
    #'symbol_footnote_start'
    #'symbol_footnotes'
    #'tagname'
    #'transform_messages'
    #'transformer',
)</t>
<t tx="ekr.20050820092312">def createParagraphsFromIntermediateFile (self,s,story,visitor):
    
    if 0: # Not needed now that putParaFromIntermediateFile is in the visitor.
        self.styleSheet = visitor.styleSheet
        self.encode = visitor.encode
    
    out = StringIO.StringIO()

    doc = reportlab.platypus.SimpleDocTemplate(out,
        pagesize=reportlab.lib.pagesizes.A4)

    # The 'real' code is doc.build(story)
    self.buildFromIntermediateFile(s,story,visitor)

    return out.getvalue()</t>
<t tx="ekr.20050820092312.1">def putParaFromIntermediateFile (self,lines,style):

    bulletText = None
    text = '\n'.join(lines)
    
    # g.trace(style,repr(text))
    
    style = self.styleSheet [style]

    self.story.append(
        reportlab.platypus.para.Paragraph (
            self.encode(text), style,
            bulletText = bulletText,
            context = self.styleSheet))</t>
<t tx="ekr.20050820094818">def buildFromIntermediateFile (self):
    
    'Synthesize calls to reportlab.platypus.para.Paragraph from an intermediate file.'
    
    lines = g.splitLines(self.contents)
    para = [] # The lines of the next paragraph.

    for line in lines:
        if line:
            if line.startswith('createParagraph:'):
                if para:
                    self.putParaFromIntermediateFile(para,style)
                    para = []
                style = line[len('createParagraph:'):].strip()
            elif line.startswith('starttag:') or line.startswith('..'):
                pass
            else:
                para.append(line)
    if para:
        self.putParaFromIntermediateFile(para,style)</t>
<t tx="ekr.20050820100547">class dummyPDFTranslator (docutils.nodes.NodeVisitor):

	@others</t>
<t tx="ekr.20050820101355">def __init__(self, writer,doctree,contents):

    self.writer = writer
    self.contents = contents
    self.story = []
    
    # Some of these may be needed, even though they are not referenced directly.
    self.settings = settings = doctree.settings
    self.styleSheet = stylesheet.getStyleSheet()
    docutils.nodes.NodeVisitor.__init__(self, doctree) # Init the base class.
    self.language = docutils.languages.get_language(doctree.settings.language_code)</t>
<t tx="ekr.20050820101355.1">def visit_document(self, node):

    self.buildFromIntermediateFile()
    
    raise docutils.nodes.SkipNode
    
def depart_document(self, node):
    
    pass</t>
<t tx="ekr.20050820101522">def encode(self, text):

    """Encode special characters in `text` &amp; return."""
    
    if type(text) is types.UnicodeType:
        text = text.replace(u'\u2020', u' ')
        text = text.replace(u'\xa0', u' ')
        text = text.encode('utf-8')

    return text

</t>
<t tx="ekr.20050820103029">def as_what(self):

    return self.story
</t>
<t tx="ekr.20050820112549">@

- First working version.

</t>
<t tx="ekr.20050821153838">def pdfMunge (self,s):
    
    '''Duplicate the munging done (somewhere in docutils) of section names.
    
    This allows us to use the nameids attribute in the document element.'''
    
    s = s.lower.replace('\t',' ')

    while s != s.replace('  ',' '):
        s = s.replace('  ',' ')
    
    return s.replace(' ','-')</t>
<t tx="ekr.20050822065754">@

- Completed the conversion to using Bunches on the context stack.
    - Added peek method.
    - In context now searches from top of context stack and returns a Bunch.
    - Rewrote the footnote logic to use bunches:
        - footnote_backrefs sets b.setLink and b.links.  Much clearer code.
        - visit/depart_label uses b.setLink and b.links to generate code.
- The code now passes a minimal test of footnote code.

- WARNING: auto-footnote numbering does not work.  I doubt it ever did.  I feel under no obligation to make it work.</t>
<t tx="ekr.20050822123348">@
I. Bugs and bug fixes

This file, leo_pdf.py, is derived from rlpdf.py. It is intended as a replacement
for it. The copyright below applies only to this file, and to no other part of
Leo.

This code fixes numerous bugs that must have existed in rlpdf.py. That code was
apparently out-of-date. For known bugs in the present code see the 'to do'
section.

II. New and improved code.

This code pushes only Bunch's on the context stack. The Bunch class is slightly
adapted from the Python Cookbook.

Pushing only Bunches greatly simplifies the code and makes it more robust: there
is no longer any need for one part of the code to pop as many entries as another
part pushed. Furthermore, Bunch's can have as much internal structure as needed
without affecting any other part of the code.

The following methods make using Bunch's trivial: push, pop, peek, inContext.
inContext searches the context stack for a Bunch of the indicated 'kind'
attribute, returning the Bunch if found.

The following 'code generator' methods were heavily rewritten:
visit/depart_title, visit/depart_visit_footnote_reference, footnote_backrefs
and visit/depart_label.

III. Passing intermediateFile.txt to reportlab.

You can use an 'intermediate' file as the input to reportlab. This can be highly
useful: you can see what output reportlab will accept before the code generators
can actually generate it.

The way this works is as follows:
1. Run this code as usual, with the trace in PDFTranslator.createParagraph
enabled. This trace will print the contents of each paragraph to be sent to
reportlab, along with the paragraph's style.

2. Take the resulting console output and put it in the file called
intermediateFile.txt, in the same folder as the original document.

3. At the start of Writer.translate, change the 'if 1:' to 'if: 0'. This causes
the code to use the dummyPDFTranslator class instead of the usual PDFTranslator
class.

4. *Rerun* this code. Because of step 3, the code will read
intermediateFile.txt and send it, paragraph by paragraph, to reportlab. The
actual work is done in buildFromIntermediateFile. This method assumes the output
was produced by the trace in PDFTranslator.createParagraph as discussed
in point 2 above.

IV. About tracing and debugging.

As mentioned in the imports section, it is not necessary to import leoGlobals.
This file is part of Leo, and contains debugging stuff such as g.trace and
g.toString. There are also g.splitLines, g.es_exception, etc. used by debugging
code.

The trace in PDFTranslator.createParagraph is extremely useful for figuring out
what happened. Various other calls to g.trace are commented out throughout the
code. These were the way I debugged this code.

Edward K. Ream:  Aug 22, 2005.</t>
<t tx="ekr.20050822125824">@

- Added 'about this code' section.</t>
<t tx="ekr.20050822172321"></t>
<t tx="ekr.20050822172321.1">@ Minor improvements to documentation.</t>
<t tx="ekr.20050825101321">def init ():
    
    '''This file may be distributed in Leo's plugin folder, but this file is NOT
    a Leo plugin!
    
    The init method returns None to tell Leo's plugin manager and unit tests to
    skip this file.'''
    
    return None</t>
<t tx="ekr.20050825101903">@

- Added warning to docstring that this is not a valid Leo plugin.

- Added init function that always returns False.  This helps Leo's unit tests.</t>
<t tx="ekr.20051025144116">c.spellCommands.openSpellTab()</t>
<t tx="ekr.20060108122501"></t>
<t tx="ekr.20060108122501.1">def init ():
    
    if Tk: # OK for unit tests.
    
        if g.app.gui is None:
            g.app.createTkGui(__file__)
    
        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler("after-create-leo-frame",rClickbinder)
            leoPlugins.registerHandler("bodyrclick1",rClicker)
            g.plugin_signon(__name__)
            
    return Tk is not None</t>
<t tx="ekr.20060109114710">c.openLeoSettings()</t>
<t tx="ekr.20060110123700">def rc_helpCallback(c=c):       rc_help(c)
def rc_dbodyCallback(c=c):      rc_dbody(c)
def rc_nlCallback(c=c):         rc_nl(c)
def rc_selectAllCallback(c=c):  rc_selectAll(c)</t>
<t tx="ekr.20060110125615"></t>
<t tx="ekr.20060513122450.1">@nocolor
@ 			X C++ Compiler nodes----
PLEASE SEE http://xccnode.sourceforge.net/
 The xcc_nodes.py plugins simplify c++ syntax and integrate compiling and debuging tools.

To start debugging, create a node whose headline is::

    @xcc projectname

or::

    @xcc projectname.ext

The optional extension (*.ext) set the kind of project the node will build.
An empty extension is equivalent to the '.exe' extension.

As soon as "@xcc" is written in the headline the plugin creates an empty configuration.

    if ext == cpp,
        inflate name.cpp
        the node will attempt to build an executable
    if ext == h,
        inflate name.h
        the node will attempt to check the syntax of the header
    if ext == exe,
        this is equivalent to no ext at all
        inflate name.h and name.cpp
        the node will attempt to build an executable
    if ext == dll,
        inflate name.h and name.cpp
        the node will attempt to build a dynamic link library
    if ext == lib,
        inflate name.h and name.cpp
 			the node will attempt to build a static link library

Creating programs

The "@xcc" node support Leo's @others syntax but **not**  section references.
 	The actual code is written in the children of the main node and the code generation is
 	affected by headlines.

 	Here are the rules: (see examples for good understanding)
- The '@' rule: If a headline starts with "@", the node and its children are ignored.

- The semicolon rule: If a headline ends with ";" and another compatible rule is trigered in the
 same headline, the rule will be written in the source if there is one.

**//**: If a headline start with "//", all its body and children are commented out as follows::
    /*headline
        body text
        and
        childs
        */

This rule is compatible with the ';' rule.

- The function rule: If a headline ends with ")", the headline is used as funtion prototype.
  The body and children are encased automatically in the opening and closing curly brace.

  The class and function rules are disabled while in a function rule.
  The function rule is compatible with the semicolon rule, except that if there is a
  header in the project the function will always be declared in the header and
  defined in the	source, appending "!" prevents declaration in header for global functions.

- The class rule: If a headline starts with "class", a class is declared and opening and
  closing curly brace are automatically written, all the children of this node are class members,
  the functions are correctly dispatched between header and source (access specifier is
   appended if needed).

- The "Default" rule: If a headline doesn't match any of the preceeding rules,
  its headline is written as a comment and the body and childs written "as is" as follows::

    //headline
        body text
        and all children.

This rule is compatible with the semicolon rule.

-&gt; Config Panel reference:
	-&gt; options : generally the most used options.
		-&gt; Create files : Request that files should be inflated.
		-&gt; Compile : Request that the project should be built using the configured compiler.
			-&gt; Seek first error : Attempt to locate the first error encountered.
		-&gt; Execute : Request to run the built exe.
			-&gt; Connect to pipe : Interface the built exe pipe to the node interface, exe is simply spwned if unchecked.
		-&gt; Debug : Request to run the built exe with the configured debugger (overide the "Execute" option).
			-&gt; Seek breapoints : Detect and "Goto" encountered breakpoints.
		-&gt; Xcc verbose : Special verbose mode usefull to config the debugger and widely used when coding the plugin
 		-&gt; Filter output : Filter compiler and debugger ouput, showing only error and warning
		-&gt; Colorize log : Colorize the output if checked, allowing easyer browsing.

- by Alexis Gendron Paquette</t>
<t tx="ekr.20060513122450.2">@nocolor
@ 

*** Most flaw can be worked around by using "default" node(or rule) and writing all	code inside it.
 (default rule -&gt; comment out headline &amp; write body "as is")

- line number refresh isnt 100% accurate when editing text in the body.
- Breakpoints can only be Added/deleted, Enabling/Disabling isnt supported yet.
- code auto dispath feature wont work as expected with template class and function.
- class is the only structural keyword supported in the tree to date, union, struct and enum dont trigger any rule.
- DLL debugging is untested to date, it surely dont work.
- Untested on Linux, see linPause and aPause functions.</t>
<t tx="ekr.20060513122450.3">@nocolor
@

- C/C++ code/project importer/merger
- Display external files if needed.(external error or similar)
- "Browse Info" management allowing declaration/references to be searched and displayed.
- Automation of precompiled headers, possibly using a "#PCH" node.
- in the debugger regular expression/task list:
    reg exp:
        if a group named "FOO" is returned by the regular
        expression, then the "_FOO_" variable is supported
        by the corresponding "Task" line.
    Task:
        Apart from those defined by the corresponding regular	expression,
</t>
<t tx="ekr.20060513122450.4"># from leoPlugins import *
# from leoGlobals import *
import leoPlugins
import leoGlobals as g

# from Tkinter import *
import Tkinter as Tk
import traceback
import os,sys,thread,threading,time,string,re
import tkFileDialog,tkMessageBox,tkSimpleDialog
import pickle,base64,zlib</t>
<t tx="ekr.20060513122450.5">@others

path_sym = "\\"</t>
<t tx="ekr.20060513122450.7">self.XCC_INITED = False

self.ACTIVE_NODE = None
self.ACTIVE_DICT = None
self.ACTIVE_PROCESS = None

self.SELECTED_NODE = None
self.SELECTED_DICT = None

self.LOCATE_CHILD = True
self.CHILD_NODE = None
self.CHILD_DICT = {}
self.CHILD_LINE = None
self.CHILD_EXT = None

self.Parser = None</t>
<t tx="ekr.20060513122450.8">self.NAME = ""
self.EXT = ""
self.HDR_EXT = ""
self.SRC_EXT = ""
self.BIN_EXT = ""
self.ABS_PATH = ""
self.REL_PATH = ""
self.CWD = ""
self.PARSE_ERROR = ""
self.PARSE_ERROR_NODE = None
self.CPPEXTS = ["h","cpp","c","dll","lib","exe"]</t>
<t tx="ekr.20060513122450.10">self.FIRST_ERROR = False
self.CPL = {}
self.COMPILE = False
self.LINK = False
self.OUTEXT = ""

self.DEBUG = False
self.EXECUTE = False
self.CPL_ERR_REGEXP = None
self.LKR_ERR_REGEXP = None
self.SEEK_FIRST_ERROR = False

self.EOL = ""</t>
<t tx="ekr.20060513122450.11">self.DBG = None

self.DEBUGGER = ""
self.TARGET_PID = ""

self.DBG_RUNNING = False
self.DBG_PROMPT = False
self.DBG_PROMPT_REGEXP = None

self.DBG_TASK = []
self.DBG_SD = []
self.DBG_RD = []
self.PROMPT_RD = []

self.DBG_STEPPING = False
self.WATCH_TASK = None

#	pipe char buffering
self.OutBuff = ""
self.ErrBuff = ""</t>
<t tx="ekr.20060513122450.12">self.EXE = None</t>
<t tx="ekr.20060513122450.13">self.FILTER_OUTPUT = False
self.VERBOSE = False
self.OPTS = {}</t>
<t tx="ekr.20060513122450.14">self.Config = ConfigClass(self)
self.BreakBar = BreakbarClass(self)
self.Dasm = DasmClass(self)
self.Watcher = WatcherClass(self)
self.DocEdit = DocEditClass(self)
self.ToolBar = ToolbarClass(self) # must be created after BreakBar.
</t>
<t tx="ekr.20060513122450.16">#binary mapping: 00 0000 (6bit)MSB-&gt;LSB
# b0:mark
# b1:doc
# b2:content
# b3:clone
# b4-5:type : class func or comment
MARK_MARK = 1
DOC_MARK = 2
CONTENT_MARK = 4
CLONE_MARK = 8

FUNC_MARK = 0
CLASS_MARK = 16
</t>
<t tx="ekr.20060513122450.17">Go_e = "S\'x\\xdam\\x8e\\xcbn\\x830\\x14D\\xf7\\xfcLk \\xb2\\xbc\\xe8\\xe2\\xda@\\xc4\\xd32\\xe0\\x90.!J\\xa1\\x04\\x02\\x04K\\x80\\xbf\\xbeV\\xd6\\x1d\\xe9\\xe8\\x8cf5\\xf9\\xe7p\\xe6\\xde\\xd0\\xf9\\x00\\x02R\\x01\\xc0\\x9b\\xbb\\xa3\\xf0\\xfdd@\\nWH5\\x95\\xe9\\x956\\xd6+\\xe6\\x844\\xdcl|\\xbf]\\x03\\xfd\\xb2\\t\\xc16r\\x96j \\xa7\\xe3f\\xe9\\xb9\\x90\\xea\\xfbH\\xb1[\\xf8\\xfa\\xa90v2\\xadG\\xf5\\xc2v\\xd6\\x7f\\x18\\x88\\x01\\x8d\\xaa\\xef\\x83\\xb9v\\x1es\\xdc\\xc1?a\\xdb[\\xd6\\xfb\\x11@X\\t(\\x19\\xdd\\xc35\\xa6\\xd4\\x83)\\x8d\\x1fG\\xeb\\x8a\\x98uB\\xa2K\\xd2\\xb5\\xc0#\\xf8\\xcd\\xe5xI\\x8ap\\x95\\xb1\\xdf\\x8b\\x15_\\x9eT\\xf8\\xac\\xf4X\\\'\\xd7\\xf9,\\xc0\\x92u\\x11\\xc0\\x81\\xf2i\\xd8\\xdbtIR\\xdaJw\\x9aD\\xbb\\xf1(b%\"\\xf5\\x02b\\x8b\\x7f\\x80n\\xa2E]\\xe1f~\\x00\\xe0\\xad_\\xd6\\x1f\\x96\\x88[)\'\np0\n."</t>
<t tx="ekr.20060513122450.18">StepIn_e = "S\'x\\xda\\x95\\xd0Ms\\x820\\x10\\x06\\xe0;\\x7f\\xa5\\x17\\x15\\xa6\\x0e\\x87\\x1e6\\x100|\\x9a\\xa4\\x0c\\xda\\x9bP\\x0b\\x02\\x82\"\\x18\\xf0\\xd77\\xe1\\xdaS3\\xf3dg\\x92\\xec\\xbb3a\\xab\\xc6\\x8d\\xed\\xa6\\xc4\\x00\\x14\\xa2\\x04 \\xce\\xae\\xfa\\x98\\x9d\\xf5a{^\\x0f\\xdbTy\\r\\x99\\x12+S\\xbe\\x95R\\xf3)\\r\\xd9\\xc6|J\\xb2\\xae\\xe5\\x93\\xb5\\xa6\\xb6\\xfe\\xb4\\x19n\\xa7\\xb4QZo\\xce\\x95\\xc6\\xe3\\x89Ry&lt;\\xac\\xc8\\xac\\xe0\\x92\\xf0\\xc52I\\xca\\xf5\\xe1\\x95\\xeb\\xd1\\xe2\\xa4G\\xbd&amp;sTV\\x7f\\xdcD\\x95\\x92\\xaa\\x84\\xfa\\xe6\\xf3\\xfaf\\xd1\\xda\\xb3h\\x85\\xa7\\x90\\xab\\x03\\x99\\xc3\\xea/\\x97\\x01\\xc5P\\x10\\x0b\\xfe.\\r\\xfe\\xb3,\\xb1\\x94\\xe5K\\x00H\\x05\\xb0\\xb7\\xd0D\\x1e&gt;\\x02{\\xee\\xb8v\\x7f \\x01\\xc4A\\x05\\x159\\x8f^\\xd4\\xe8\\xb8+\\xef\\xcfQ5O\\x06\\xd0\\x10\\x17yq\\xddU\\xc4H(B(\\x19-\\x87N\\x82\\xcb\\x8e\\x82\\xf8c\\x8f\\x8aU\\xe8\\x072\\x9b\\x89\\x1d\\x08m\\x15\\xbb\\xc8f\\xc2\\xb7\\xf6\\xcc\\xeb.\\x07\\x84\\xcb\\x90\\xec\\x03Q\\xd0\\xb1\\xa4\\x989\\xf7\\x9f\\x16\\xdek,\\x1b&gt;\\x9b\\xef\\xc0\\xb6\\x8f\\x1d=\\xc4\\xed\\xe5M\\x0e\\xe1\\x8c^Z\\xe4|\\xd2 j\\x10\\x1a\\xf8.\\xd3J\\xd1\\xcd\\x1e\\xb2\\rJb\\xd4\\x82i:\\x85 `?&gt;\\xb4_\\xa4j\\x9b\\xc9\'\np0\n."</t>
<t tx="ekr.20060513122450.19">StepOver_e = "S\'x\\xda\\x95\\xd0Mo\\x830\\x0c\\x06\\xe0;\\xbf\\xa6|hh\\x87\\x1e\\x9c\\x10h`@\\x03\\xed(\\xbbA\\x86\\xc2\\x97J\\x05l\\x01~\\xfdHw\\x9f\\xb4Wz\\xec\\x8b-YN\\x0e\\xbd\\x17;}M\\x00\\x18DW\\x80\\xc8\\xae\\xf4\\xd9\\xce\\x94m.\\x95XY\\xb8\\xad\\xb8\\xca7\\xbf\\xed\\xb2We.\\rE\\xdfGuM\\x95\\xb1\\xccf\\xe5Q\\x18\\xf3\\xb8{\\x14Y\\xaf\\xdc\\x83\\x8c\\xdf\\xfd\\x95\\xf7\\xfez\\xed\\xe9\\x1a\\xb6t%5M\\x9f*s\\xb6+3\\xda\\xf8\\xae0#\\xb56j\\xb9\\xfe\\xbbz\\xed\\xfdTI\\xbbG\\x90v&gt;f\\xed\\xf0\\x12\\xb7d\\t\\x93\\xee\\xc3K\\x80\\x11\\x10\\x14\\xc3\\xdf\\xd1\\xe0?\\xc1\\xf2\\xd9\\x9e/\\x01\\xa0\\x8d\\x847\\x8c\\x16:\\x05\\x08\\xe1uJ\\xb5\\xb1\\xc3IN]$\\x98\\x90\\\'\\x1f\\xa4\\xcc\\xc3\\xc0\\x850\\x8c\\x9a\\xba\\xa6A\\xec\\x92U\\xcf\\xc0At\\x10\\x11r\\x93\\xeb\\x019\\xc8bS\\x02\\x08\\x1f\\x863\\x96\\xcc\\xea.\\x1e\\x08\\xbd8a4hy\\x00\\x143\\xdf\\xee\\xef\\xb5\\xe0\\xd4\\xa3h\\xab\\x9c\\xf2\\xaba\\xef\\x1e\\xc6\\x84I\\xcag!\\xac\\x98\\x9cH\\xcbo\\x13\\x069Y\\xa9?b\\x03\\xce\\xedV[\\xc5%\\xac\\x97O\\xc2\\xb1!)\\xb9]4Q\\x87\\xab\\xe77\\xc2\\xca\\xf4\\xb30\\xf9\\xdb~\"\\xc4\\xf2x\\xd4~\\x00\\\'\\xed\\x9a\\xd0\'\np0\n."</t>
<t tx="ekr.20060513122450.20">StepOut_e = "S\"x\\xda\\x95\\xd0\\xddn\\x820\\x14\\xc0\\xf1{\\x9eF\\xc5\\x8c\\xedb\\x17\\xa7\\xa5`a\\x80\\x05;\\xd4;As\\xca\\x87\\x9bQ\\x94\\x8f\\xa7_\\xcb\\x1b\\xac\\xc9/\'9i\\xfeM\\x9a.Z?q[\\xc5\\x00\\x04\\xc4\\x12 )\\xae\\xf6\\xb3\\xb8\\xd8\\x9dsYvNnL]a$\\xc6P:\\xda\\xde{\\x95\\xf9\\x87\\xd1\\x15\\xab\\x8f\\x97\\xa6\\xe7\\xd2\\xd2\\xf7\\x96\\xc6\\xbd\\xc8;\\xe3vZiy\\xab\\x95?\\xc18k\\x83L\\xd6A\\x16\\xd5|\\x8c\\x14\\x1f\\x99\\xe2\\xd9\\xec\\xb2N\\x9d\\xf9U\\xad\\xb4\\xbb\\xc9*\\xedx2Nv|\\xd7\\x9d\\xd9a\\x15\\xd7F~\\x8duV\\x97\\x9a[\\x985\\x01\\x15\\xf5\\xef[R\\xb3!\\xca\\xccB\\xf7\\xd2\\xe6\\xe8\\xa7 \\x18 \\xa7\\x00`\\xc1\\x7f\\x0e\\xed\\xe71\\x7f\\t\\x00o\\x01\\xb6\\x94\\x0c\\\\\\xfa\\xd4E\\xc4\\xad\\xa5\\xb7\\x04\\x9b\\xfc\\x8b\\x02\\xde7A\\x8f\\xb8\\x90\\xa17E\\xef\\x8ce=6\\x8c\\xd0\\x1d[\\xec&lt;\\xa2\\xb8\\xdc\\x10w|\\x84\\x02\\xf0\\xb6\\xe0\\xd2S4F\\xeaUp8\\xd1\\xe8\\x8ar\\x98\\xa0\\xea\\xad\\xa6&lt;\\xb9(\\x90\\x9d_J\\x08\\xdf\\x150\\x9e/\\xacI\\x15J\\x97\\xba4\\x0f\\xfdjI c&gt;\\xfb\\xe6\\x9b\\xfd/\\x0e\\x870\\x8a\\x08*2$\\x10\\x9c\\xf91\\xc3*&gt;$t\\xbf\\x86\\xeaL,2\\xae\\xc6M\\xa3{O\\x07H\\xfa\\x90\\x94\\xef\\xa0/]_\\xb1\\xf2\\x8b\\xa0\\x80\\xa4\\xff\\xfc\\xb4\\xfe\\x00\\xd4\\xc7\\xa1 \"\np0\n."</t>
<t tx="ekr.20060513122450.21">Pause_e = "S\'x\\xda\\x95\\xceKn\\x830\\x18\\x04\\xe0=\\x97i\\xf3t\\xba\\xc8\\xe2\\xb7\\t\\xc6N\\xb0e\\x08\\x02\\x96\\x85\\x02\\x86:\\x84\\x14Wn9}Q{\\x82\\x8e\\xf4I\\xb3\\x19i\\xe2gC\\xa5o\\xf4\\t@A\\xa4\\x00\\x04\\xaa7\\x16e+[f\\xbb\\xc5f1\\xdbR.]\\xce\\x13Z\\xe4\\xc1\\xcb!\\x0f\\xd0&gt;3\\x03OR\\xc3\\x92\\x93\\t-\\xeaC1{\\x9a\\x8a\\xfeim?\\xea\\xb5\\xedM\\xc0\\x93\\xda\\xc1\\xffC\\xfeF\\xde\\xef#\\x00V(\\x10\\x04\\x7f\\xb1\\xe9\\xec\\xe3\\xd6U\\xb9\\x0c}\\xd82B\\xb4\\xdaJ\\xca\\xaf\\xeeN\\x19&amp;8m8\\xef\\x8aT\\xf9\\xb4\\xd3\\xd3%}\\xcc\\xf7(\\x13\\xac\\xed\\xa2\\xc6\\x80\\xday\\xef\\xcc\\x07\\x03\\xac\\xba\\xc9\\x98\\x1d\\x1e\\x82\\xde\\xba\\xd1\\x0e\\xda\\xb1\\xf4\\xbb\\x91\\xe6Z]\\xe2\\xcf\\xbe(h\\x89\\xc1\\x9d\\x13\\xdc\\xb7N\\x91\\x81\\x8c\\x8e\\xbf\\xd11~\\x8d\\x08\\x80t\\xc7\\xa3\\xf7\\x03\\xce\\xc7^\\x95\'\np0\n."</t>
<t tx="ekr.20060513122450.22">Stop_e = "S\'x\\xda-\\x8c\\xc1\\x8e\\x820\\x14E\\xf7\\xfc\\x8c\\xa2\\x18\\xdc\\xb8x\\x14h\\x0b%\\x0e4LSv`\\xb4O@t\\xa4\\x19\\x18\\xbe~&amp;d\\xee\\xe2\\x9c\\xe4,n\\xb1\\xed\\xe99\\xec1\\x02\\xc8Ad\\x00\\xe7\\xe6\\xb1\\xb7\\xfe\\xd5\\xb5\\xbeZl\\xa3\\x96\\xaf\\x9d}\\xd5\\xaal\\xd9_\\xdc\\xdb\\xb7&gt;\\x1eR~\\xf9$\\xb4q\\t\\xbdx3\\x88\\xed\\x0b\\xfe\\xe7\\xac$\\xd3\\xaa\\xf5\\x10\\x80\\xab\\x1c\\x18\\tf&gt;\\xa6a`&amp;\\x9d\\xb0\\xb8\\xe5\\x1d\\xa5\\x811Z\\x8b\\x04y\\xa78\\x18\\x8c\\xde\\xb5\\x91P\\xd6\\t\\xbd\\xe3\\xc4\\xaa\\xef\\xc9s\\xb2Z\\x02\\xc8l\\xb8\\xde\\x97\\xaa\\x93\\x85\\xe8\\xe4\\xb8A\\x94\\xba|T\\xa2_2\\x16\\xc5$\\x7f\\xa6\\xb7\\x8f\\xc1\\xe0\\x0f13X\\x8a\\x05F&amp;\\x1eZ\\xe9Y\\x1a\\x00\\x84\\xe3\\xc9\\xf9\\x05\\x1a\\x01HO\'\np0\n."</t>
<t tx="ekr.20060513122450.23">WatchData = "S\"x\\xda\\x95\\x90\\xdbr\\x820\\x10@\\xdf\\xf9\\x1a\\xc1Z\\xea\\xe3&amp;\\x86\\x8b\\x96\\x8bf\\x18\\x8coBk \\xa4B!\\x8a\\xc9\\xd77\\xfa\\x07\\xdd\\x99\\xb3g\\xf7ewg\\x0f\\x0b\\x19f\\x1b\\xd9\\x10\\x80=\\xa4\\x05@Z\\x95\\xae\\xaaJ\\xa3\\xaa\\xec\\xc9\\xa3\\xf633\\xf9\\xd6\\xc7\\xcc\\x9d\\xfc\\xc0:p\\xa7c`,\\xf7\\xca\\xd6\\xa3\\xb7\\xbeW\\xdeZ\\x9d\\xbd\\xb5\\xb3\\xfc-\\xd7\\x16w5h\\x0bu\\xfdwO\\x8d\'\\xad\\xcco)\\x07F\\xe5\\xaa\\xd7\\xd2\\xf4T.\\x07Z\\x8fL\\xd7\\x8a\\xd1\\xfa~\\xd2\\x85\\xdc\\xd2\\xe2j\\x11\\xb1NDL\\x9f\\x10\\xe7\\x99\\x9a\\xe8Fd\\x94\\x91\\xe1x#\\xc2\\xfaj\\xfb&amp;R~\\x13\\xa5\\xbe\\xb0X\\x9b\\xefejjO\\x99&amp;T\\xe3\\xd9\\x1d\\x04\\xf3\\xd2\\xb3]g\\xb1\\x13\\xbbaG9\\x80\\x03\\xff\\t&lt;\\xbf\\xf4z\\t@\\xdc\\x00D\\x18=\\x18\\xdbm\\x10\\x9f\\x07\\xe2\\xf4\\xb8El\\xda\\xda\\xe6\\xab,\\x82\\x16b\\x12F\\x98\\x7f\\x04|\\x143#\\x04\\x03\\x97\\x19N\\xda&gt;\\xee&gt;\\xa3\\x96s\\x9d$-\\xdbw1A\\xb3j\\xcfR\\xac\\x12\\xa0!\\xc6\\xec\\x92#~p\\xdeB\\x84\\x10]L\\xb7X\\xf3\\xbe\\xc8s\\x01\\x8f\\xe2\\x07o\\x0eo\\xfdq#`\\x9f\\x07!\\x1cz\\x8d\\n&gt;\\xbb\\xdd\\xe5\\xb3y\\xef\\x92,Ar\\xde\\xdez\\xd4\\xa4\\xa5)\\xc7\\x92\\x04\\xdfWx\\xd4\\x1d:9\\xdcey\\x84\\x16{{\\xba\\xef\\xfc\\x01\\xdb\\xb2\\x9a\\xfc\"\np0\n."</t>
<t tx="ekr.20060513122450.24">ConfigData = "S\'x\\xdaU\\xce\\xc1r\\x820\\x14\\x85\\xe1=O\\x03\\xd6\\x11\\xbb\\xbc\\t\\x84\\x06\\x0c\\x99@-\\xda\\x1d\\xa4N\\x10(j\\xc9\\x10\\xe0\\xe9k\\xd8yg\\xbe\\xb9\\x9b\\x7fq2\\xb7\\x8bx\\xd0\\xd5!\\x80\\x00&amp;\\x00R\\xff\\xe2i\\xbf\\xf0tU,\\xba\\xe2\\xd6$}\\x8b\\x8c\\xf2D\\xa6\\xa7Q\\x16\\xefc\\xb5\\xb1l\\xe6\\xfd\\x95\\x1bm9\\xf7\\xb2\\xe8\\xfa\\xa4\\x90}&lt;\\xaf::\\xb3\\x86\\xcea\\xfd\\xa1\\xfd\\xcb[\\xba\\xc8\\xb5K\\x9b\\xb3g\\xcb8?\\xb6\\xf7$W\\xf0z\\xd8\\xac\\xcfY\\x17\\x01\\xd0\\n \\xc68S7\\x16\\x802\\x8a\\xd0\\x01\\x1b\\x8a\\tF\\x8aR\\xce@\\x18N\\x00+\\x97\\x8a\\x14\\xc0$1\\xa0\\xba\\x1d\\xcaC-\\xdc\\x9c#\\x04\\xfbG\\x19\\xd57\\xe7\\xf8\\x0b(@\\xed\\x105\\x0b=3\\x1ev\\x8a\\xf5\\x15\\xc1\\xd0\\xee\\xd1!\\x80t\\xc74R\\xe2Hq\\x8f\\x94\\xfb\\xc5\\xae`\"\\x81\\x82O\\xd3d\\xd1\\xf5[\\xe5\\x12=\\xa6\\xed\\xcf)\\x84m\\xbb\\x1b\\x03\\xe7\\xb9\\xd8w\\xfe\\x01*\\x83e%\'\np0\n."</t>
<t tx="ekr.20060513122450.25">Prompt_e = "S\'x\\xda\\xad\\x90\\xcdn\\xab0\\x14\\x84\\xf7\\xbcJ\\x16\\xb9I\\xdbp\\xbb\\xe8\\xe2p\\xb0\\x8d\\xe1\\xf2\\xe3:\\xb4%;\\x12r\\r\\x86\\x14Zh\\x0cy\\xfa\\x92\\xf6\\t*\\xf5\\x93F\\xa3\\x91F\\xb3\\x98\\xc7?\\r\\x8b\\xdd\\xa6d\\x02\\x04D)@\\xb2\\x9c\\xf9\\x7fs\\xbfX\\x9e\\xed\\xc5\\xfet7\\xd8\\xc7\\x9ba\\xff\\xbc\\x9au\\xe9\\xed\\xf8\\xd2\\xbf\\xd0\\xf1\\x1a\\xf3\\xe7\\xa6\\xdbM\\x87W\\x7f:4|\\n5\\x97\\xc4*\\xbdk;\\xba\\x1c\\xd6\\xc3{&gt;+[\\x0f:[G:[us\\xdd\\x97i\\xdd\\x05\\xb2\\xf6Q\\xe8v\\x13W\\xd7@J.\\x00\\x96c\\xbdc\\x8f \\x08(\\x8e\\xf0\\x8d\\x05\\xbf\\xc8\\xcf\\xc6\\xd0|\\xd9\\xd7%\\x00\\xfcm&gt;\\x86\\xc5\\x0e\\xf4\\x81\\xeb(\\xa3\\xa8\\x85\\xf5\\x96\\xf7\\x01E\\x18y%\\xbb\\x91\\xf7G\\xdfE\\tSq\\xaeD\\x9f\\\'\\x9e\\x1e\\xf9G\\xd1\\x18q\\x9b\\\'\\xbe\\xae\\xc8S\\xd6Om\\x9b\\xba\\x1e:w\\xf1\\xae6\\x1da\\xa1\\x87\\x08\\xe2%\\xacn-\\x11\"\\xbaXli\\x0b\\xdc\\xb4\\x1c\\xdc1\\x13E\"D{@\\x07+\\x88\\\\L\\x03\\xf5\\x11zP\\xf6\\x9b\\xfd+(Ch\\xdaH\\xf8k\\xc3vl\\x81q45\\x8bC\\xbd\\x19d\\xce-TNU\\x94\\xda@J\\xa8\\xae)U\\\'\\xf8\\x97)BOR\\xaf\\xa0\\xdb\\xf9\\xf5\\xe2]\\x9d\\x19$|\\xb4\\x03\\xc5\\x02R\\x95\\xfc\\xb8]\\x0b\\x15I\\x80\\xd8&lt;&lt;X\\x9fJ\\x0f\\xa2\\xed\'\np0\n."</t>
<t tx="ekr.20060513122450.26">ErrorColor = "#%02x%02x%02x" % (255,200,200)
BreakColor = "#%02x%02x%02x" % (200,200,255)
LineNumColor = "#%02x%02x%02x" % (200,200,255)
RegExpFgColor = "#%02x%02x%02x" % (0,0,255)
VarSupBgColor = "#%02x%02x%02x" % (255,230,230)</t>
<t tx="ekr.20060513122450.28">def winPause(pid):
    
	import ctypes

	hp = ctypes.windll.Kernel32.OpenProcess(0x1F0FFF,0,int(pid))
	if hp == 0:
		return Error("xcc: ","can't open process: "+str(long(ctypes.windll.Kernel32.GetLastError())))
	
	if ctypes.windll.Kernel32.DebugBreakProcess(hp) == 0:
		return Warning("xcc: ","Unable to break into the target!")</t>
<t tx="ekr.20060513122450.29">def linPause(pid):	# theorical way to do it, untested!

	import signal
	os.kill(pid,signal.SIGINT)</t>
<t tx="ekr.20060513122450.31">def GoToNode(self,node,index=None,tagcolor=None):
    
    if not node: return
    cc = self ; c = cc.c ; w = cc.LeoBodyText
    
    c.beginUpdate()
    if not node.isVisible():
        for p in node.parents_iter():
            p.expand()
    c.selectPosition(node)
    c.endUpdate()

    if index is None: return
    w.mark_set("insert",index)
    w.see(index)

    if tagcolor is None: return 
    l,c = w.index("insert").split(".")
    w.tag_add("xcc_error",l+".0",l+".end")
    w.tag_config("xcc_error",background=tagcolor)
    w.tag_raise("xcc_error")</t>
<t tx="ekr.20060513122450.32">def GetNodePath(node,_as="-&gt;"):

	path = []
	for p in node.parents_iter():
		path.insert(0,p.headString()+_as)

	path.append(node.headString())
	return ''.join(path)</t>
<t tx="ekr.20060513122450.33">def AddText(text,node):

	node.setBodyString(node.bodyString()+text)
	l,c = LeoBody.index("end").split(".")
	LeoBody.see(l+".0")</t>
<t tx="ekr.20060513122450.34">def Error(module,error):
	g.es(module,newline = False,color = "blue")
	g.es(error,color = "red")
</t>
<t tx="ekr.20060513122450.35">def Warning(module,warning):

	g.es(module,newline = False,color = "blue")
	g.es(warning,color = "orange")</t>
<t tx="ekr.20060513122450.36">def Message(module,warning):

	g.es(module,newline = False,color = "blue")
	g.es(warning)
</t>
<t tx="ekr.20060513122450.38">def GetDictKey(dic,key,create=False,init=""):
        if key in dic:
            return dic[key]
        else:
            if create == True:
                dic[key] = init
                return dic[key]
            else:
                return None</t>
<t tx="ekr.20060513122450.39">def TraceBack():
        typ,val,tb = sys.exc_info()
        lines = traceback.format_exception(typ,val,tb)
        for line in lines:
            # g.es(line,color = "red")
            print line
            
TraceBack = g.es_exception</t>
<t tx="ekr.20060513122450.40">def DecompressIcon(data):
	try:
		#unpickle
		zdata = pickle.loads(data)	
		#unzip
		return zlib.decompress(zdata)	#return a base64
	except Exception:
		Traceback()
</t>
<t tx="ekr.20060513122450.41">@
# Encode to base64, zip the data in a string and finally pickle it to be free from illegal char
#the inflated file is a literal(without the quote)
#to be embeded in code and passed to DecompressIcon func before use.

#to use:
	# remove "@" at the top
	# ctrl+e (execute script)
	# choose the file to translate, press save
	# open choosedfile.lit in notepade, select all(ctrl+a), copy(ctrl+c), close notepade
	# paste(ctrl+v) where you needed your literal (dont forget to add the quote)

from leoGlobals import *
import tkFileDialog
from pickle import *
from base64 import *
from zlib import *
import os


try:
	ft = ('All Files', '.*'),
	s = tkFileDialog.askopenfilename(filetypes=ft,title="Select file to convert...")
	if s:
		f = file(s,"rb")
		data = f.read()
		f.close()
		b64data = encodestring(data)
		zdata = compress(b64data,9)
		pdata = dumps(zdata)
		pdata = pdata.replace("\\","\\\\")
		pdata = pdata.replace("\'","\\\'")
		pdata = pdata.replace("\"","\\\"")
		pdata = pdata.replace("\n","\\n")
		name,ext = os.path.splitext(s)
		f = file(name+".lit","wb")
		f.write(pdata)
		f.close()
except Exception,e:
	g.es(str(e))</t>
<t tx="ekr.20060513122450.42"></t>
<t tx="ekr.20060513122450.43">class ProcessClass:
    List=[]
    if os.name == "dos" or os.name == "nt":
        Encoding = "mbcs"
    else:
        Encoding = "utf-8"
    @others</t>
<t tx="ekr.20060513122450.44">class ReadingThreadClass(threading.Thread):

    @others</t>
<t tx="ekr.20060513122450.45">def __init__(self):

    threading.Thread.__init__(self)
    self.File = None
    self.Lock = thread.allocate_lock()
    self.Buffer = ""</t>
<t tx="ekr.20060513122450.46">def run(self):
    try:
        s=self.File.read(1)
        while s:
            self.Lock.acquire()
            self.Buffer = self.Buffer + s
            self.Lock.release()
            s=self.File.read(1)            
            
    except IOError, ioerr:
        self.Buffer = self.Buffer +"\n"+ "[@run] ioerror :"+str(ioerr)</t>
<t tx="ekr.20060513122450.47">def Update(self,func):

    ret = True
    if self.Lock.acquire(0) == 1:
        if self.Buffer and func:
            func(unicode(self.Buffer, ProcessClass.Encoding))
            self.Buffer=""
        else:
            ret = self.isAlive()	
        self.Lock.release()
    else:
        	ret = self.isAlive()
    return ret


</t>
<t tx="ekr.20060513122450.48">def __init__(self,cc,node,filename,args,start=None,out=None,err=None,end=None,spawn=False):

    self.cc = cc
    self.Node = node	
    self.Spawn = spawn	
    self.FileName = filename.replace("\\",path_sym)
    self.Arguments = args
    
    self.In = None
    self.OutThread = None
    self.ErrThread = None	
    
    self.OnStart = start
    self.Output = out
    self.Error = err
    self.OnEnd = end
    
    self.Kill = False
</t>
<t tx="ekr.20060513122450.49">def Open(self):
    
    cc = self.cc
    if self.Spawn:
        os.spawnl(os.P_NOWAIT,self.FileName,self.Arguments)
        ProcessClass.List.remove(self)
        return True

    path,fname = os.path.split(self.FileName)
    
    if fname == "" or os.access(self.FileName,os.F_OK) != 1:		
        Warning("xcc: ","PROCESS: "+self.FileName+" is not a valid file!")
        #return #removed to allow std commands

    # Create the threads and open the pipe, saving and restoring the working directory.
    oldwdir= os.getcwd().replace("\\",path_sym)
    if path != "" and os.access(path,os.F_OK):        
        os.chdir(path)
    
    # added 14/11/07 : linux seem to have a different behaviour
    if os.name != "dos" and os.name != "nt":
        fname =  self.FileName
    
    self.OutThread = self.ReadingThreadClass()
    self.ErrThread = self.ReadingThreadClass()
    self.In,self.OutThread.File,self.ErrThread.File	= os.popen3(fname+" "+self.Arguments)
    os.chdir(oldwdir)
    
    if not self.In or not self.OutThread.File or not self.ErrThread.File:
        return Error("xcc: ","PROCESS: Can't open file!")
                            
    # Start the threads.
    self.OutThread.start()
    self.ErrThread.start()	

    self.Node.setMarked()	
    cc.LeoTop.redraw()
    return True</t>
<t tx="ekr.20060513122450.50">def Close(self):
    
    cc = self.cc
    
    self.In and self.In.close()
    
    self.OutThread.File and self.OutThread.File.close()

    exitcode = self.ErrThread.File and self.ErrThread.File.close()
    
    self.Node.clearMarked()
    self.Node = None	
        
    self.OnEnd and self.OnEnd(exitcode)	

    cc.LeoTop.redraw()
    
    return exitcode</t>
<t tx="ekr.20060513122450.51">def Update(self):

    if not self.OutThread or not self.ErrThread:
        return False
        
    # writing intro to console
    if self.OnStart:
        self.OnStart()
        self.OnStart = None
    
    return self.OutThread.Update(self.Output) or self.ErrThread.Update(self.Error)</t>
<t tx="ekr.20060513122450.52"></t>
<t tx="ekr.20060513122450.53">class ConfigClass:
    @others</t>
<t tx="ekr.20060513122450.54">class PageClass(Tk.Canvas):
    @others
</t>
<t tx="ekr.20060513122450.55">class CHECK:
    @others
</t>
<t tx="ekr.20060513122450.56">def __init__(self,master,n,x=0,y=0,dpd=[]):
    self.dpd = dpd
    self.Check = Tk.StringVar()
    self.Name = n
    c = self.c = Tk.Checkbutton(master,text=n,onvalue="True",offvalue="False",variable=self.Check,command=self.UpdDpd)
    master.create_window(x,y,anchor='nw',window=c)</t>
<t tx="ekr.20060513122450.57">def Get(self):
    return self.Check.get()
</t>
<t tx="ekr.20060513122450.58">def Set(self,value):
    self.Check.set(value)
    self.UpdDpd()
</t>
<t tx="ekr.20060513122450.59">class ENTRY:
    @others
</t>
<t tx="ekr.20060513122450.60">def __init__(self,c,n,w=175,h=22,e=1,a='nw',x=0,y=0,re=False,vs=False):
    self.Name = n
    
    if re != False: fg = RegExpFgColor
    else: fg = "black"
        
    if vs != False: bg = VarSupBgColor
    else: bg = "white"
    
    self.MasterFrame = mf = Tk.Frame(c,relief='groove',height=h,width=w)
    self.ID = c.create_window(x,y,anchor=a,window=mf,height=h,width=w)	
    
    self.Entry = Tk.Entry(mf,width=1,bg=bg)
    self.Entry.pack(side="right",fill="x",expand=e)
    l = Tk.Label(mf,text=n+":",fg=fg).pack(side="right")
</t>
<t tx="ekr.20060513122450.61">def Get(self):
    return self.Entry.get()
</t>
<t tx="ekr.20060513122450.62">def Set(self,text):
    self.Entry.delete(0,'end')
    self.Entry.insert('end',text)
</t>
<t tx="ekr.20060513122450.63">class TEXT:
    @others
</t>
<t tx="ekr.20060513122450.64">def __init__(self,c,n,w=350,h=80,a='nw',x=0,y=0,re=False,vs=False):#text are 3 column wide
    
    self.Name = n
    
    if re != False: fg = RegExpFgColor
    else: fg = "black"
        
    if vs != False: bg = VarSupBgColor
    else: bg = "white"
    
    self.MasterFrame = mf = Tk.Frame(c,relief='groove')
    self.ID = c.create_window(x,y+1,anchor=a,window=mf,width=w,height=h)
    
    lf = Tk.Frame(mf,relief='flat')
    lf.pack(side="top",fill="x",expand=1)			
    Tk.Label(lf,text=n+":",fg=fg).pack(side="left")
    
    self.Text = Tk.Text(mf,bg=bg)
    self.Text.pack(side="top",fill="x",expand=1)
</t>
<t tx="ekr.20060513122450.65">def Get(self):
    s = self.Text.get(1.0,'end')
    lines = s.splitlines()
    res = ""
    for l in lines:
        if l != "":
            res += l+"\n"
    return res
</t>
<t tx="ekr.20060513122450.66">def Set(self,text):
    self.Text.delete(1.0,'end')
    self.Text.insert('end',text)
</t>
<t tx="ekr.20060513122450.67">class LABEL:
    @others
</t>
<t tx="ekr.20060513122450.68">def __init__(self,c,text,w=175,h=22,e=1,a='nw',x=0,y=0,color="#%02x%02x%02x" % (150,150,150)):
    
    self.MasterFrame = mf = Tk.Frame(c,relief='groove',height=h,width=w)
    self.ID = c.create_window(x,y,anchor=a,window=mf,height=h,width=w)	
    
    self.Label = Tk.Label(c,text=text,justify='left',fg=color)
    self.ID = c.create_window(x,y,anchor=a,window=self.Label)
    </t>
<t tx="ekr.20060513122450.69">class HELP(Tk.Button):
    @others</t>
<t tx="ekr.20060513122450.70">def __init__(self,c,buttontext="Help",boxtitle="Help",msg="!",x=5,y=0):
    
    self.Title = boxtitle
    self.Message = msg
    Tk.Button.__init__(self,c,text=buttontext,command=self.Help)
    self.ID = c.create_window(x,y,anchor='nw',window=self)</t>
<t tx="ekr.20060513122450.71">def Help(self):
    tkMessageBox.showinfo(self.Title,self.Message)</t>
<t tx="ekr.20060513122450.72">def __init__(self,cc,name):
    
    self.cc = cc
    self.name = name
    self.Objects = []
    Tk.Canvas.__init__(self,cc.LeoBodyParent)
    self.X=self.Y=self.W=self.H = 0
    self.CreateObjects(self)</t>
<t tx="ekr.20060513122450.73">def AddObject(self,o):

    if o != None:
        self.Objects.append(o)
        self.X,self.Y,self.W,self.H = self.bbox('all')
</t>
<t tx="ekr.20060513122450.74">def BBox(self):
    self.X,self.Y,self.W,self.H = self.bbox('all')
</t>
<t tx="ekr.20060513122450.75">def AddSep(self,length=380,color="black"):

    if length != None:
        l = length
    else:
        l = self.W
    self.create_line(5,self.H+4,l+5,self.H+4,fill=color)
    self.H += 10
</t>
<t tx="ekr.20060513122450.76">def CreateObjects(self,master):#must overide
    pass
</t>
<t tx="ekr.20060513122450.77">def SaveObjects(self,pd=None):
    
    cc = self.cc

    if pd == None:
        pd = cc.sGet(self.name,init={})
    
    for o in self.Objects:
        pd[o.Name] = o.Get()
</t>
<t tx="ekr.20060513122450.78">def LoadObjects(self,pd=None):	

    cc = self.cc
    if pd == None:
        pd = cc.sGet(self.name,{})
        
    #g.trace(self.name,pd)
    
    for o in self.Objects:
        if o.Name not in pd:				
            pd[o.Name] = o.Get()
        else:
            o.Set(pd[o.Name])</t>
<t tx="ekr.20060513122450.79">def ClearObjects(self,value=""):
    for o in self.Objects:
        if o.Name == "Build sequence":
            o.Set("COMPILE")
        else:
            o.Set(value)</t>
<t tx="ekr.20060513122450.80">def Hide(self):
    
    cc = self.cc
    self.pack_forget()
    
    b = cc.Config.GetButton(self.name)
    b.config(relief='groove',fg="black")
    
    cc.LeoYBodyBar.config(command=cc.LeoBodyText.yview)
    cc.LeoBodyText.config(yscrollcommand=cc.LeoYBodyBar.set)</t>
<t tx="ekr.20060513122450.81">def Show(self):
    
    cc = self.cc
    
    if cc.Config.ActivePage:
        cc.Config.ActivePage.Hide()
        
    cc.Config.ActivePage = self
    b = cc.Config.GetButton(self.name)
    b.config(relief='sunken',fg="blue")	
    
    self.config(scrollregion=self.bbox('all'))
    self.config(yscrollcommand=cc.LeoYBodyBar.set)
    
    cc.LeoYBodyBar.config(command=self.yview)
    cc.LeoYBodyBar.pack(side="right",fill="y")
    self.pack(expand=1,fill="both")</t>
<t tx="ekr.20060513122450.82">def __init__(self,cc):
    
    self.cc = cc
    self.Pages = []
    self.Buttons = []
    self.ActivePage = None

    #switch frame
    self.SwitchFrame = Tk.Frame(
        cc.LeoBodyParent,relief='groove',bd=2,height=40,width=100)
    
    #title
    self.Title = Tk.Entry(self.SwitchFrame,justify='center')
    self.Title.pack(side="top",fill="x",expand=1)	
    
    self.AddPages()	
    #add pages switches
    for page in self.Pages:
        if page:
            b = Tk.Button(self.SwitchFrame,text=page.name,width=10,command=page.Show,relief='groove')
            self.Buttons.append(b)
            b.pack(side="left")
            if not self.ActivePage:
                self.ActivePage = page
        
    if 0: #Cancel button
        # Not needed.
        b = Tk.Button(self.SwitchFrame,text="Cancel",command=lambda: self.Hide(False))
        b.pack(side="right")

   
    
    self.BreakTags = {}
    self.visible = False</t>
<t tx="ekr.20060513122450.83">def GetPage(self,name):
    
    for p in self.Pages:
        if p and p.name == name:
            return p</t>
<t tx="ekr.20060513122450.84">def GetButton(self,name):

    for b in self.Buttons:
        if b and b["text"] == name:
            return b</t>
<t tx="ekr.20060513122450.85">def Hide(self,save=True):
    try:
        cc = self.cc
    
        if self.visible == True:
            self.ActivePage.Hide()	
            self.SwitchFrame.pack_forget()
            cc.LeoYBodyBar.config(command=cc.LeoBodyText.yview)
            cc.LeoBodyText.config(yscrollcommand=cc.LeoYBodyBar.set)
            cc.LeoXBodyBar.pack(side = "bottom",fill="x")
            if cc.CHILD_NODE:
                cc.BreakBar.Show()
            cc.LeoBodyText.pack(expand=1, fill="both")
        
            if save == True:
                self.SaveToNode()
            cc.ToolBar.ConfigButton.config(command=self.Show,relief='raised')
            cc.ToolBar.DisplayFrame.pack(side="top",fill="x",expand=1)
            self.visible = False
    except Exception:
        g.es_exception</t>
<t tx="ekr.20060513122450.86">def Show(self):
    try:
        cc = self.cc
        cc.HideWidgets()
        if cc.BreakBar.visible:
            cc.BreakBar.Hide()
        
        cc.ToolBar.DisplayFrame.pack_forget()
        cc.LeoBodyText.pack_forget()
        cc.LeoXBodyBar.pack_forget()
        cc.LeoYBodyBar.pack_forget()
    
        self.SwitchFrame.pack(side="top", fill="x")
        
        self.LoadFromNode()
        self.ActivePage.Show()
        cc.ToolBar.ConfigButton.config(command=self.Hide,relief='sunken')
        self.visible = True
        #cc.c.redraw()
    except Exception:
        TraceBack()

</t>
<t tx="ekr.20060513122450.87">def ClearConfig(self):
    self.Title.delete(0,'end')
    self.Title.insert('end',"BLANK_CONFIG")
    for p in self.Pages:
        if p.name == "Options":
            p.ClearObjects("False")
        else:
            p.ClearObjects()
</t>
<t tx="ekr.20060513122450.88">def LoadFromNode(self):

    cc = self.cc
    self.Title.delete(0,'end')
    self.Title.insert('end',cc.sGet("Title"))
        
    for p in self.Pages:
        if p:
            p.LoadObjects()</t>
<t tx="ekr.20060513122450.89">def SaveToNode(self):
    
    cc = self.cc
    
    cc.sSet("Title",self.Title.get())
    
    for p in self.Pages:
        p and p.SaveObjects()</t>
<t tx="ekr.20060513122450.90">def LoadFromFile(self):
    try:
        ft = ('XCC Config files', '.xcc'),
        s = tkFileDialog.askopenfilename(filetypes=ft,title="Open xcc connfiguration file...")
    
        if s == "":
            Error("xcc: ","Load action canceled by user!")
            return
        
        #read file and compose code
        f = file(s,"r")
        td = None
        code = "td ="+f.readline()
        f.close()
        
        # load in temp dict
        try:
            exec code
        except Exception:
            TraceBack()
            Error("xcc: ","File content is invalid!")
            return
        
        #	load each pages
        for p in self.Pages:
            if p.name in td:
                p.LoadObjects(td[p.name])
                
        #set title to file name
        name,ext = os.path.splitext(s)
        path,name = os.path.split(name)		
        self.Title.delete(0,'end')
        self.Title.insert('end',name)		
        
        #save to node to ensure integrity
        self.SaveToNode()
        
    except Exception:
        TraceBack()




</t>
<t tx="ekr.20060513122450.91">def SaveToFile(self):
    try:
        
    
        ft = ('XCC Config files', '.xcc'),
        s = tkFileDialog.asksaveasfilename(
        filetypes=ft,
        title="Save xcc connfiguration file...",
        initialfile = self.Title.get()
        )
        
        if s == "":
            Error("xcc: ","Save action canceled by user!")
            return		
        
        name,ext = os.path.splitext(s)
                
        td = {}
        
        # save each pages
        for p in self.Pages:
            td[p.name] = {}
            p.SaveObjects(td[p.name])	
        
        #write the dict to file
        f = file(name+".xcc","w+")
        Message("xcc: ","Writing config in "+name+".xcc")
        f.write(str(td))
        f.close()
        
        # reset title to file name
        path,name = os.path.split(name)		
        self.Title.delete(0,'end')
        self.Title.insert('end',name)
        
        # save to node
        self.SaveToNode()
    except Exception:
        TraceBack()







</t>
<t tx="ekr.20060513122450.92">def Apply(self):
    self.SaveToNode()
    self.Hide()
</t>
<t tx="ekr.20060513122450.93">def AddPages(self):
    
    cc = self.cc
    
    self.Pages.append(self.OptPageClass(cc,self))
    self.Pages.append(self.CplPageClass(cc))
    self.Pages.append(self.LkrPageClass(cc))
    self.Pages.append(self.DbgPageClass(cc))
    self.Pages.append(self.ExePageClass(cc))
    self.Pages.append(self.LangPageClass(cc))
    #self.Pages.append(self.CodePageClass(cc))</t>
<t tx="ekr.20060513122450.94">class OptPageClass(PageClass):

    @others
</t>
<t tx="ekr.20060513122450.95">def __init__(self,cc,cfgc):
    
    self.cc = cc
    self.cfgc = cfgc
    ConfigClass.PageClass.__init__(self,cc,"Options")
</t>
<t tx="ekr.20060513122450.96">def CreateObjects(self,master): # must overide

    @others

    self.AddSep(length=self.W)</t>
<t tx="ekr.20060513122450.97">s1 = self.CHECK(master,"Create files",x=5,y=self.H)
self.AddObject(s1)

s2 = self.CHECK(master,"Source files",x=5,y=self.H)
s3 = self.CHECK(master,"Auto include header",x=100,y=self.H)
self.AddObject(s2)
self.AddObject(s3)

s4 = self.CHECK(master,"Doc files",x=5,y=self.H)
self.AddObject(s4)

s1.dpd = [s2.c,s3.c,s4.c]</t>
<t tx="ekr.20060513122450.98"></t>
<t tx="ekr.20060513122450.99">class CplPageClass(PageClass):
    @others
</t>
<t tx="ekr.20060513122450.100">def __init__(self,cc):
    
    self.cc = cc
    ConfigClass.PageClass.__init__(self,cc,"Compiler")</t>
<t tx="ekr.20060513122450.101">def Browse(self):
    try:
        for o in self.Objects:
            if o and o.Name == "Compiler":
                break
        else: return

        ft = ('Executables', '.exe;.bin'),
        s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Compiler...")
        if s == None:
            return Error("xcc: ","Action canceled by user!")
        elif s == "":
            return Error("xcc: ","Empty path returned!")

        o.Set(os.path.normpath(s))
    except Exception:
        g.es_exception</t>
<t tx="ekr.20060513122450.102">def AddPath(self,name):
    try:
        d = tkFileDialog.askdirectory()
        if d != "":
            d = d.replace("\\",path_sym)
            for o in self.Objects:
                if o.Name == name:
                    opaths = o.Get().splitlines()
                    npaths = []
                
                    for p in opaths:
                        p = p.strip()
                        if p != "":
                            npaths.append(p)
                        
                    npaths.append(d)
                
                    o.Set(string.join(npaths,"\n"))
    except Exception:
        g.es_exception</t>
<t tx="ekr.20060513122450.103">def CreateObjects(self,master): #must overide

    @others



</t>
<t tx="ekr.20060513122450.104">x=10
y=10
text_w = 350
text_h = 80

# compiler entry -
self.AddObject(self.ENTRY(master,"Compiler",x=5,y=5,w=350,h=20))
b = Tk.Button(master,text=" ...",command=self.Browse)
master.create_window(360,self.Y-2,anchor='nw',window=b)</t>
<t tx="ekr.20060513122450.105">self.AddSep()
#-------------------------------------------------

t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
self.HELP(master,boxtitle="Arguments info",msg=CplArgumentsHelp,x=360,y=self.H+20)
self.AddObject(t1)

#------------------------------------------
t1 = self.TEXT(master,"Debug arguments",x=5,y=self.H,vs=True)
self.HELP(master,boxtitle="Debug arguments info",msg=CplDebugArgumentsHelp,x=360,y=self.H+20)
self.AddObject(t1)</t>
<t tx="ekr.20060513122450.106">self.AddSep()
#-------------------------------------------------------------
b = Tk.Button(master,text="Browse",command=lambda:self.AddPath("Include search paths"))
master.create_window(360,self.H+58,anchor='nw',window=b)
t1 = self.TEXT(master,"Include search paths",x=5,y=self.H)
self.HELP(master,boxtitle="Include search paths info",msg=IncludeSearchPathsHelp,x=360,y=self.H+20)
self.AddObject(t1)</t>
<t tx="ekr.20060513122450.107">ww =19
self.AddSep()
#------------------------------------------------------
lf = Tk.Frame(master,relief='flat',bd=2)
master.create_window(self.X,self.H+2,width=text_w,height=20,anchor='nw',window=lf)
Tk.Label(lf,text="Compiler symbols:").pack(side="left")
self.H += 22

self.HELP(master,boxtitle="Include path and Library path info",msg=IncludePathAndLibraryPathHelp,x=360,y=self.H)
#Include path
e1 = self.ENTRY(master,"Include path",x=5,y=self.H)
#Check syntaxe
e2 = self.ENTRY(master,"Check syntaxe",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)</t>
<t tx="ekr.20060513122450.108"># ------------------
self.AddSep()
e = self.ENTRY(master,"Error detection",x=5,y=self.H,w=350,re=True)
self.HELP(master,boxtitle="Error detection info",msg=CplArgumentsHelp,x=360,y=self.H)
self.AddObject(e)</t>
<t tx="ekr.20060513122450.109">class DbgPageClass(PageClass):
    @others
</t>
<t tx="ekr.20060513122450.110">def __init__(self,cc):
    
    self.cc = cc
    ConfigClass.PageClass.__init__(self,cc,"Debugger")
</t>
<t tx="ekr.20060513122450.111">def Browse(self):
    try:
        for o in self.Objects:
            if o != None and o.Name == "Debugger":
                break
        else: return

        ft = ('Executables', '.exe;.bin'),
        s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Debugger...")
    
        if s == None:
            return Error("xcc: ","Action canceled by user!")
        elif s == "":
            return Error("xcc: ","Empty path returned!")

        o.Set(os.path.normpath(s))
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.112">def CreateObjects(self,master):#must overide
    @others
</t>
<t tx="ekr.20060513122450.113">x=10
y=10
text_w = 350
text_h = 80
    
# compiler entry
self.AddObject(self.ENTRY(master,"Debugger",x=5,y=5,w=350,h=20))
b = Tk.Button(master,text=" ...",command=self.Browse)
master.create_window(360,self.Y-2,anchor='nw',window=b)	
</t>
<t tx="ekr.20060513122450.114">self.AddSep()
t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
self.HELP(master,boxtitle="Arguments info",msg=DbgArgumentsHelp,x=360,y=self.H+20)
self.AddObject(t1)</t>
<t tx="ekr.20060513122450.115">self.AddSep()
e1 = self.ENTRY(master,"Prompt pattern",x=5,y=self.H,re=True) 
e2 = self.ENTRY(master,"Pipe eol",x=180,y=self.H)

self.HELP(master,boxtitle="Prompt pattern and Pipe eol info",msg=DbgPipingHelp,x=360,y=self.H)
self.AddObject(e1)
self.AddObject(e2)</t>
<t tx="ekr.20060513122450.116">ww =19
    
self.AddSep()
    
lf = Tk.Frame(master,relief='flat',bd=2)
master.create_window(5,self.H+2,width=text_w,height=20,anchor='nw',window=lf)
Tk.Label(lf,text="Debugger commands symbols:").pack(side="left")
self.H += 22
    
# ------------------
e1 = self.ENTRY(master,"Go",x=5,y=self.H)
e2 = self.ENTRY(master,"Step in",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)

# ------------------
e1 = self.ENTRY(master,"Continue",x=5,y=self.H)
e2 = self.ENTRY(master,"Step over",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)
    
# ------------------
e1 = self.ENTRY(master,"Stop",x=5,y=self.H)
e2 = self.ENTRY(master,"Step out",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)
    
# ------------------
e1 = self.ENTRY(master,"Evaluate",x=5,y=self.H)
e2 = self.ENTRY(master,"X cmd",x=180,y=self.H)
self.AddObject(e1)
self.AddObject(e2)</t>
<t tx="ekr.20060513122450.117">#------------------------------------------------------
self.AddSep()
t1 = self.TEXT(master,"Startup task",x=5,y=self.H,vs=True)

self.HELP(master,boxtitle="Startup task info",msg=DbgStartupTaskHelp,x=360,y=self.H+20)

self.AddObject(t1)</t>
<t tx="ekr.20060513122450.118"># ------------------
self.AddSep()
e = self.ENTRY(master,"Target pid task",x=5,y=self.H,w=350,vs=True)

self.HELP(master,boxtitle="Target pid task and Find pid info",msg=DbgTargetPidHelp,x=360,y=self.H)
self.AddObject(e)

e = self.ENTRY(master,"Find pid",x=5,y=self.H,w=350,re=True,vs=True)
self.AddObject(e)</t>
<t tx="ekr.20060513122450.119">#------------------------------------------------------
self.AddSep()
self.HELP(master,boxtitle="Break detection info",msg=DbgBreakDetectionHelp,x=360,y=self.H+20)
self.AddObject(self.TEXT(master,"Break detection",x=5,y=self.H,w=text_w,h=text_h,re=True))

self.AddSep()
e1 = self.ENTRY(master,"Set break",x=5,y=self.H,vs=True)
e2 = self.ENTRY(master,"Clear break",x=180,y=self.H,vs=True)
self.HELP(master,boxtitle="Set break and Clear break info",msg=DbgSetClearBreakHelp,x=360,y=self.H)
self.AddObject(e1)
self.AddObject(e2)

self.AddSep()
self.HELP(master,boxtitle="List breaks and Identify break info",msg=DbgBreakIdHelp,x=360,y=self.H)
self.AddObject(self.ENTRY(master,"List breaks",x=5,y=self.H,w=350))
e = self.ENTRY(master,"Identify break",x=5,y=self.H,w=350,re=True)
self.AddObject(e)

# ------------------
self.AddSep()
self.HELP(master,boxtitle="Query location and Find location info",msg=DbgLocationHelp,x=360,y=self.H)
self.AddObject(self.ENTRY(master,"Query location",x=5,y=self.H,w=350))
e = self.ENTRY(master,"Find location",x=5,y=self.H,w=350,re=True,vs=True)
self.AddObject(e)</t>
<t tx="ekr.20060513122450.120">#-------------------------------------------------------------
self.AddSep()
t1 = self.TEXT(master,"Regular expression",x=4,y=self.H,w=173,re=True,vs=True)
t2 = self.TEXT(master,"Task",x=180,y=self.H,w=173,vs=True)
self.HELP(master,boxtitle="Regular expression and Task info",msg=DbgMiscExpHelp,x=360,y=self.H+20)
self.AddObject(t1)
self.AddObject(t2)</t>
<t tx="ekr.20060513122450.121">class ExePageClass(PageClass):
    @others
</t>
<t tx="ekr.20060513122450.122">def __init__(self,cc):
    
    self.cc = cc
    ConfigClass.PageClass.__init__(self,cc,"Executable")
</t>
<t tx="ekr.20060513122450.123">def CreateObjects(self,master):#must overide
    bd=self["background"]
    x=10
    y=10
    text_w = 350
    text_h = 80
    @others
    self.create_line(0,self.H+5,self.W+1,self.H+5)</t>
<t tx="ekr.20060513122450.124">self.AddObject(self.TEXT(master,"Execution arguments",x=5,y=5))

</t>
<t tx="ekr.20060513122450.125">#self.AddSep()
#e1 = self.ENTRY(master,"Dll caller",x=5,y=self.H,w=280,h=20)
#b = Tk.Button(master,text="Browse...",width=10,default='disabled')
#master.create_window(self.X+285,self.H,width=60,height=20,anchor='nw',window=b)
#self.AddObject(e1)</t>
<t tx="ekr.20060513122450.126"></t>
<t tx="ekr.20060513122450.127"></t>
<t tx="ekr.20060513122450.128"></t>
<t tx="ekr.20060513122450.129"></t>
<t tx="ekr.20060513122450.130"></t>
<t tx="ekr.20060513122450.131">DbgArgumentsHelp = """
Command line passed to to the debugger.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_"""</t>
<t tx="ekr.20060513122450.132">DbgPipingHelp = """
Prompt pattern:
    Regular expression used to detect the debugger prompt.
    
Pipe eol:
    End of line character used when sending command to the debugger."""</t>
<t tx="ekr.20060513122450.133">DbgStartupTaskHelp = """
Commands sent to the debugger at startup.
These commands must leave the debugger breaked
in the entry point of the target.

The following variables are supported:
    
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_"""</t>
<t tx="ekr.20060513122450.134">DbgTargetPidHelp = """
Target pid task:
    Command used to retreive the target process identifier.
    The target pid is used to break into the debugger.

    The following variables are supported:
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
    
Find pid:
    Regular expression used to retreive the target pid when
    the "Target pid task" is sent to the debugger.

    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
    The following groups must be returned by the regular expression:
        
        PID"""</t>
<t tx="ekr.20060513122450.135">DbgBreakDetectionHelp = """
Regular expression used to detect a break in target code execution.

When an output line match one of the expressions, an attempt is 
made to find the current location in the target code using the
"Query location" and "Find location" fields.

Each line is a different regular expression."""</t>
<t tx="ekr.20060513122450.136">DbgSetClearBreakHelp = """
Set break:
    Command used to set a breakpoint.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_

Clear break:
    Command used to clear/delete a breakpoint.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_
        _ID_*
        
    *If _ID_ is used, attempt to find it using the
    "List breaks" and "Identify break" fields."""
</t>
<t tx="ekr.20060513122450.137">DbgBreakIdHelp = """
List breaks:
    Command used to list the debugger's break table.
    
    This field is ignored if the "Clear break" field
    make no use of the _ID_ variable.
    
Identify break:
    Regular expresion used to find the id of a breakpoint
    when the "List breaks" command is sent to the debugger.
    
    This field is ignored if the "Clear break" field
    make no use of the _ID_ variable.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_
        
    The following groups must be returned by the regular expression:
        
        ID"""
</t>
<t tx="ekr.20060513122450.138">DbgLocationHelp = """
Query location:
    Command used to retreive the file and line where
    the debugger is currently breaked.
    
Find location:
    Regular expression used to retreiv the current 
    file and line when the "Query location" command
    is sent to the debugger.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
    The following groups must be returned by the regular expression:
        
        EXT
        LINE

"""
</t>
<t tx="ekr.20060513122450.139">DbgMiscExpHelp = """
Regular expression:
    Each line is a separate regular expression.
    
    If an output line is matched by one of the expression,
    the corresponding "Task" line is sent to the debugger.
        
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
Task:
    Each line is a separate task trigered by the corresponding
    "Regular expression" line.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_"""</t>
<t tx="ekr.20060513122450.140"></t>
<t tx="ekr.20060513122450.141">CplArgumentsHelp = """
Command line passed to to the compiler.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""</t>
<t tx="ekr.20060513122450.142">CplDebugArgumentsHelp = """
Command line passed to to the compiler 
when debugging is requested.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""</t>
<t tx="ekr.20060513122450.143">IncludeSearchPathsHelp = """
Each lines is a path to be searched for include files.

These paths are assembled unsing the "Include path"
symbol to create the _INCPATHS_ variable."""</t>
<t tx="ekr.20060513122450.144">LibrarySearchPathsHelp = """
Each lines is a path to be searched for library files.

These paths are assembled unsing the "Library path"
symbol to create the _LIBPATHS_ variable."""</t>
<t tx="ekr.20060513122450.145">UsedLibrariesHelp = """
Each whitespace delimited word is a libary to be 
used while building the project.

These libraries are assembled unsing the "Use library"
symbol to create the _LIBRARIES_ variable."""</t>
<t tx="ekr.20060513122450.146">IncludePathAndLibraryPathHelp = """
Include path:	
    Symbol used with "Include search path" field
    to create the _INCPATHS_ variable.
    
Library path:	
    Symbol used with "Library search path" field
    to create the _LIBPATHS_ variable."""
</t>
<t tx="ekr.20060513122450.147">UseLibraryAndCheckSyntaxeHelp = """
Use library:	
    Symbol used with "Used libraries" field
    to create the _LIBRARIES_ variable.
    
Check syntaxe:	
    Symbol used when the project is a single
    header (.h extension). Header alone cant be 
    built but some compiler offer a syntaxe check."""</t>
<t tx="ekr.20060513122450.148">BuildExeAndBuildDllHelp = """
One of these symbols will be used to replace
the _BUILD_ variable in the "Arguments" and 
"Debug arguments" fields.

The correct one is choosed according to the
project extension.

These generally determine if the output is 
single or multi-threaded.

Build exe:	
    Symbol used to build an executable.
    
Build dll:	
    Symbol used to build a dll."""</t>
<t tx="ekr.20060513122450.149">CompilePchAndUsePchHelp = """
TODO: Support precompiled header auto creation/inclusion."""</t>
<t tx="ekr.20060513122450.150">ErrorDetectionHelp = """
Regular expression used to detect error 
from the compiler output.

The following groups must be defined by
the regular expression:
    
    FILE
    LINE
    ID *
    DEF *
    
    * = Facultative groups"""
</t>
<t tx="ekr.20060513122450.151">class ToolbarClass(Tk.Frame):
    
    @others

</t>
<t tx="ekr.20060513122450.152">def __init__(self,cc):    
    self.cc = cc
    
    Tk.Frame.__init__(self,cc.LeoBodyParent)
    
    f = Tk.Frame(self)
    f.pack(side="top",fill="x",expand=1)
    
    self.Go_e=Tk.PhotoImage(data=DecompressIcon(Go_e))
    self.GoButton = Tk.Button(f,command=self.Go,image=self.Go_e)
    self.GoButton.pack(side="left")
    
    self.Pause_e=Tk.PhotoImage(data=DecompressIcon(Pause_e))
    self.PauseButton = Tk.Button(f,image=self.Pause_e,command=cc.aPause,state='disabled')
    self.PauseButton.pack(side="left")
    
    self.Stop_e=Tk.PhotoImage(data=DecompressIcon(Stop_e))
    self.StopButton = Tk.Button(f,image=self.Stop_e,command=cc.aStop,state='disabled')
    self.StopButton.pack(side="left")
    
    self.StepIn_e=Tk.PhotoImage(data=DecompressIcon(StepIn_e))
    self.StepButton = Tk.Button(f,image=self.StepIn_e,state='disabled',command=cc.aStepIn)
    self.StepButton.pack(side="left")
    
    self.StepOver_e=Tk.PhotoImage(data=DecompressIcon(StepOver_e))
    self.StepInButton = Tk.Button(f,image=self.StepOver_e,state='disabled',command=cc.aStepOver)
    self.StepInButton.pack(side="left")
    
    self.StepOut_e=Tk.PhotoImage(data=DecompressIcon(StepOut_e))
    self.StepOutButton = Tk.Button(f,image=self.StepOut_e,state='disabled',command=cc.aStepOut)
    self.StepOutButton.pack(side="left")	
    
    self.Prompt_e=Tk.PhotoImage(data=DecompressIcon(Prompt_e))
    self.PromptButton = Tk.Button(f,image=self.Prompt_e,command=self.Refresh)
    
    s="&lt;&lt;"
    e="&gt;&gt;"
    # command entry
    self.DbgEntry = Tk.Entry(f)
    self.DbgEntry.bind("&lt;Key&gt;",self.OnKey)
    
    
    
    #---------------------------------------------------
    self.ConfigGif=Tk.PhotoImage(data=DecompressIcon(ConfigData))
    self.ConfigButton = Tk.Button(f,image=self.ConfigGif,command=cc.Config.Show)
    self.ConfigButton.pack(side="right")
    
    self.Xcmd_gif = Tk.PhotoImage(data=DecompressIcon(Xcmd_icon))
    
    self.DasmButton = Tk.Button(f,image=self.Xcmd_gif,command=cc.Dasm.Show)
    self.DasmButton.pack(side="right")    
    
    self.WatchGif = Tk.PhotoImage(data=DecompressIcon(WatchData))
    
    self.WatchButton = Tk.Button(f,image=self.WatchGif,command=cc.Watcher.Show)
    self.WatchButton.pack(side="right")
    
    self.DocGif=Tk.PhotoImage(data=DecompressIcon(DocData))
    self.DocButton = Tk.Button(f,image=self.DocGif,command=cc.DocEdit.Show)
    self.DocButton.pack(side="right")
    
    self.DisplayFrame = Tk.Frame(self)
    self.DisplayFrame.pack(side="top",fill="x",expand=1)
    
    fgcolor = "#808080"#BreakBar.fgcolor
    self.Spacer = Tk.Text(
        self.DisplayFrame,height=1,fg=fgcolor,relief='flat',
        font=cc.LeoFont,width=4,state='disabled')
    self.Spacer.pack(side="left")
    
    self.Display = Tk.Text(
        self.DisplayFrame,height=1,relief='flat',fg=fgcolor,bg=cc.BreakBar["bg"],
        font=cc.LeoFont,state='disabled')
    self.Display.pack(side="left",fill="x",expand=1)
</t>
<t tx="ekr.20060513122450.153">def Go(self):    
    try:
        cc = self.cc
        
        
        if not cc.ACTIVE_NODE:
            if len(ProcessClass.List) &gt; 0:
                return Error("xcc: ","already running!")
            cc.sGo()
        elif cc.ACTIVE_NODE == cc.SELECTED_NODE:
            cc.aGo()
        else:
            Error("xcc: ",str(cc.ACTIVE_NODE)+" is already active!")            
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.154">def Hide(self):

    cc = self.cc
    self.pack_forget()
    cc.LeoBodyText.config(wrap=cc.LeoWrap)
    if cc.Watcher.visible:
        cc.Watcher.Hide()</t>
<t tx="ekr.20060513122450.155">def Show(self):

    cc = self.cc    
    self.pack(side="top",fill="x")
    cc.LeoBodyText.config(wrap='none')

    if cc.Watcher.visible:
        cc.Watcher.Show()</t>
<t tx="ekr.20060513122450.156">def OnKey(self,event=None):
    
    cc = self.cc
    
    if cc.ACTIVE_NODE:
        if len(event.char)==1 and ord(event.char) == 13:
            cc.aWrite(self.DbgEntry.get().replace("\n",""))
            self.DbgEntry.delete(0,'end')</t>
<t tx="ekr.20060513122450.157">def EnableStep(self):

    self.StepButton["state"] = 'normal'
    self.StepInButton["state"] = 'normal'
    self.StepOutButton["state"] = 'normal'</t>
<t tx="ekr.20060513122450.158">def DisableStep(self):

    self.StepButton["state"] = 'disabled'
    #self.StepButton["image"] = self.Step_d
    
    self.StepInButton["state"] = 'disabled'
    #self.StepInButton["image"] = self.StepIn_d
    
    self.StepOutButton["state"] = 'disabled'
    #self.StepOutButton["image"] = self.StepOut_d</t>
<t tx="ekr.20060513122450.159">def SyncDisplayToChild(self,loc):
    
    cc = self.cc
    self.Display["cursor"] = ""
    self.Display.unbind("&lt;Button-1&gt;")
    self.Spacer["state"] = 'normal'
    self.Spacer.pack(side="left")
    if cc.BreakBar.visible:
        self.Spacer["width"] = int(cc.BreakBar["width"])+1
    else:
        self.Spacer["width"] = 4
    
    self.Spacer.delete(1.0,'end')
    self.Spacer.insert('insert',"."+loc.FOUND_FILE_EXT)
    self.Spacer["state"] = 'disabled'
    
    disp = ":: " ; _as = ""
    for c in loc.CLASS_LIST:
        _as += c+" :: "
    disp += _as	
    off = 0
    if loc.CURRENT_RULE and loc.CURRENT_RULE != "class" and loc.CURRENT_RULE != "doc":
        off = len(disp)
        disp += cc.CHILD_NODE.headString()	
    
    self.Display["state"] = 'normal'
    self.Display.delete(1.0,'end')
    self.Display.tag_delete("marking")
    self.Display.insert("insert",disp)
    
    if loc.CURRENT_RULE == "func":
        spec,ret,name,params,pure,dest,ctors = loc.CURRENT_MO
        
        v,s,e = spec
        if v != "":
            self.Display.tag_add("marking","1."+str(s+off),"1."+str(e+off))
        
        v,s,e = ret
        if s != -1 and e != -1:
            self.Display.tag_add("marking","1."+str(s+off),"1."+str(e+off))		
        
        params,s,e = params
        if params != "()":
            s += 1
            params = params.split(",")
            for p in params:
                pmo = re.search("[( ]*(?P&lt;TYPE&gt;.+) +(?P&lt;NAME&gt;[^) ]+)[ )]*",p)
                if pmo != None:
                    s2,e2 = pmo.span("TYPE")
                    self.Display.tag_add("marking","1."+str(s+off+s2-1),"1."+str(s+off+(e2-s2)))
                    off += len(p)+1
                    
    
    if loc.CURRENT_RULE == "doc":
        self.Display.insert("insert",loc.DocName())
        
    self.Display.tag_config("marking",foreground="#7575e5")
    self.Display["state"] = 'disabled'
</t>
<t tx="ekr.20060513122450.160">def SyncDisplayToError(self):
    cc = self.cc
    
    self.Spacer["state"] = 'normal'
        
    if cc.BreakBar.visible == True:
        self.Spacer["width"] = int(cc.BreakBar["width"])+1
    else:
        self.Spacer["width"] = 4
    
    self.Spacer.delete(1.0,'end')
    self.Spacer.insert("insert","ERR")
    self.Spacer["state"] = 'disabled'
    
    self.Display["state"] = 'normal'
    self.Display.delete(1.0,'end')
    self.Display.tag_delete("marking")
    
    self.Display.insert("insert",cc.PARSE_ERROR)
    self.Display.tag_add("marking","1.0",'end')
    self.Display.tag_config("marking",foreground="red")
    self.Display["state"] = 'disabled'
    
    self.Display["cursor"] = "hand2"
    self.Display.bind("&lt;Button-1&gt;",self.OnErrorLeftClick)

</t>
<t tx="ekr.20060513122450.161">def SetError(self,err,node=None):
    
    self.cc.PARSE_ERROR = err
    self.cc.PARSE_ERROR_NODE = node</t>
<t tx="ekr.20060513122450.162">def OnErrorLeftClick(self,event):
    
    self.cc.GoToNode(self.cc.PARSE_ERROR_NODE)</t>
<t tx="ekr.20060513122450.163">def HideInput(self):
    self.PromptButton.pack_forget()
    self.DbgEntry.pack_forget()
</t>
<t tx="ekr.20060513122450.164">def ShowInput(self):
    
    #self.ConfigButton.pack_forget()
    #self.WatchButton.pack_forget()
    
    self.PromptButton.pack(side="left")
    self.DbgEntry.pack(side="left",fill="x",expand=1)

    #self.ConfigButton.pack(side="right")
    #self.WatchButton.pack(side="right")</t>
<t tx="ekr.20060513122450.165">def Refresh(self):
    try:
        cc = self.cc

        if (
            cc.ACTIVE_NODE and cc.DBG_PROMPT and
            cc.ACTIVE_NODE != cc.SELECTED_NODE
        ):
            cc.GoToNode(ACTIVE_NODE)
            QueryGoTaskClass(cc)
            cc.DbgOut("")
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.166">class WatcherClass(Tk.Frame):

    @others
</t>
<t tx="ekr.20060513122450.167">def __init__(self,cc):
   
    self.cc = cc
    self.Watching = False
    self.visible = False
    
    Tk.Frame.__init__(self,cc.LeoBodyParent,relief='groove')
    
    self.EditFrame = Tk.Frame(self,relief='groove')
    self.VarEntry = Tk.Entry(self.EditFrame)
    self.VarEntry.bind("&lt;Key&gt;",self.OnEditKey)
    self.VarEntry.pack(side="left",fill="x",expand=1)
    self.EditFrame.pack(side="top",fill="x")
    
    self.BoxFrame = Tk.Frame(self,relief='groove')
    
    self.InFrame = Tk.Frame(self.BoxFrame,relief='groove')
    self.OutFrame = Tk.Frame(self.BoxFrame,relief='groove')
    self.BoxBar = Tk.Scrollbar(self.BoxFrame,command=self.yview)
    
    self.InFrame.pack(side="left",fill="both",expand=1)   
    self.BoxBar.pack(side="left",fill="y")
    self.OutFrame.pack(side="left",fill="both",expand=1)
    
    
    self.InXBar = Tk.Scrollbar(self.InFrame,orient="horizontal")
    self.InXBar.pack(side="bottom",fill="x")
    self.InBox = Tk.Text(
            self.InFrame,
            yscrollcommand=self.BoxBar.set,
            xscrollcommand=self.InXBar.set,font=cc.LeoFont,
            state='disabled',width=20,wrap='none',height=10,
            selectbackground="white",selectforeground="black")
    self.InXBar.config(command=self.InBox.xview)
    self.InBox.pack(side="bottom",fill="both",expand=1)
    
    self.OutXBar = Tk.Scrollbar(self.OutFrame,orient="horizontal")
    self.OutXBar.pack(side="bottom",fill="x")
    self.OutBox = Tk.Text(
        self.OutFrame,
        yscrollcommand=self.BoxBar.set,
        xscrollcommand=self.OutXBar.set,
        font=cc.LeoFont,state='disabled',width=20,wrap='none',height=10,
        selectbackground="white",selectforeground="black")
    self.OutXBar.config(command=self.OutBox.xview)   
    self.OutBox.pack(side="bottom",fill="both",expand=1)

    self.BoxFrame.pack(fill="both",expand=1)
    self.InBox.bind("&lt;Delete&gt;",self.OnDelete)
    self.OutBox.bind("&lt;Delete&gt;",self.OnDelete)
    self.InBox.bind("&lt;Button-1&gt;",self.OnLeftClick)
    self.OutBox.bind("&lt;Button-1&gt;",self.OnLeftClick)</t>
<t tx="ekr.20060513122450.168">def OnEditKey(self,event):
    
    cc = self.cc

    if not self.Watching and len(event.char)==1 and ord(event.char) == 13:
        self.InBox.config(state='normal')
        self.OutBox.config(state='normal')
        
        var = self.VarEntry.get()
        cc.sGet("Watch",[]).append(var)
        
        self.InBox.mark_set("insert",'end')			
        self.InBox.insert("insert",var+"\n")
        
        self.OutBox.mark_set("insert",'end')
        self.OutBox.insert("insert","- ?? -\n")
        
        self.InBox.config(state='disabled')
        self.OutBox.config(state='disabled')
        self.VarEntry.delete(0, 'end')
        
        if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
            WatchTaskClass(cc)
            cc.DbgOut("")</t>
<t tx="ekr.20060513122450.169">def OnLeftClick(self,event):
   
    if self.InBox.get(1.0,'end').replace("\n",""):
        w = event.widget
        w.mark_set("insert","@0,"+str(event.y))
        l,c = w.index("insert").split(".")
    
        self.InBox.tag_delete("current")
        self.InBox.tag_add("current",l+".0",l+".end")
        self.InBox.tag_config("current",background=BreakColor)
    
        self.OutBox.tag_delete("current")
        self.OutBox.tag_add("current",l+".0",l+".end")
        self.OutBox.tag_config("current",background=BreakColor)</t>
<t tx="ekr.20060513122450.170">def OnDelete(self,event):
    if "current" in self.InBox.tag_names():
        ib = self.InBox ; ob = self.OutBox
        ib.config(state='normal')
        ob.config(state='normal')
        try:        
            s,e = ib.tag_nextrange("current","1.0")
            var = ib.get(s,e)	
            watchs = self.cc.sGet("Watch",[])
            if var in watchs:
                watchs.remove(var)		
            ib.delete(s,e+"+1c")
            ib.tag_delete("current")
            
            s,e = ob.tag_nextrange("current","1.0")
            ob.delete(s,e+"+1c")
            ob.tag_delete("current")
            
        except Exception:
            pass
            
        ib.config(state='disabled')
        ob.config(state='disabled')</t>
<t tx="ekr.20060513122450.171">def yview(self, *args):
    apply(self.InBox.yview,args)
    apply(self.OutBox.yview,args)</t>
<t tx="ekr.20060513122450.172">def Hide(self):
    try:
        cc = self.cc
        self.pack_forget()
        self.visible = False
        cc.ToolBar.WatchButton.config(command=self.Show,relief='raised')
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.173">def Show(self):
    try:
        cc = self.cc
        cc.HideWidgets()
        
        cc.LeoBodyText.pack_forget()
        cc.LeoXBodyBar.pack_forget()
        cc.LeoYBodyBar.pack_forget()
        
        self.pack(side = "bottom",fill="x")
        
        cc.LeoXBodyBar.pack(side = "bottom",fill="x")
        cc.LeoYBodyBar.pack(side="right",fill="y")
        if cc.BreakBar.visible:
            cc.BreakBar.Hide()
            cc.BreakBar.Show()
        cc.LeoBodyText.pack(fill="both",expand=1)
        
        cc.ToolBar.WatchButton.config(command=self.Hide,relief='sunken')
        self.visible = True
        self.Sync()
        
        if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
            WatchTaskClass(cc)
            cc.DbgOut("")
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.174">def Sync(self):
    
    cc = self.cc

    if self.visible == True:
        self.InBox.config(state='normal')
        self.OutBox.config(state='normal')
        
        self.InBox.delete(1.0,'end')
        self.OutBox.delete(1.0,'end')
        
        w = cc.sGet("Watch",[])
        for v in w:
            if v.strip() != "":
                self.InBox.mark_set("insert",'end')
                self.InBox.insert("insert",v+"\n")
            
                self.OutBox.mark_set("insert",'end')
                self.OutBox.insert("insert","- ?? -\n")
            else:
                w.remove(v)
    
        self.InBox.config(state='disabled')
        self.OutBox.config(state='disabled')</t>
<t tx="ekr.20060513122450.175">class BreakbarClass(Tk.Text):

    @others
</t>
<t tx="ekr.20060513122450.176">def __init__(self,cc):
    
    self.cc = cc
    self.bodychanged = False	
    self.visible = False
    coffset = 10
    c = cc.LeoBodyText.winfo_rgb(cc.LeoBodyText["bg"])	
    red, green, blue = c[0]/256, c[1]/256, c[2]/256
    red -= coffset ; green -= coffset ; blue -= coffset	
    self.bgcolor = "#%02x%02x%02x" % (red,green,blue)
    red -= coffset*6 ; green -= coffset*6 ; blue -= coffset*6
    self.fgcolor = "#%02x%02x%02x" % (red,green,blue)
    
    Tk.Text.__init__(self,
        cc.LeoBodyParent,
        name='sidebar',
        width=2,
        bd=cc.LeoBodyText["bd"],
        bg = self.bgcolor,
        relief='flat',
        setgrid=0,
        selectbackground = self.bgcolor,
        selectforeground = self.fgcolor,
        foreground = self.fgcolor,
        font=cc.LeoFont,
        pady=cc.LeoBodyText["pady"],
        cursor="hand2",
        wrap='none'
    )
    
    self.leowrap = cc.LeoBodyText["wrap"]
    self.bind("&lt;Button-1&gt;",self.OnLeftClick)
    self.bind("&lt;Button-3&gt;",self.OnRightClick)
    self["state"]='disabled'
    cc.LeoBodyText.pack_forget()
    cc.LeoXBodyBar.pack(side="bottom", fill="x")
    cc.LeoBodyText.pack(expand=1, fill="both")</t>
<t tx="ekr.20060513122450.177"></t>
<t tx="ekr.20060513122450.178">def yview(self,cmd=None,arg1=None,arg2=None):
    cc = self.cc ; w = cc.LeoBodyText
    #g.es("yview")
    if cmd:
        if arg1 != None:
            if arg2 != None:
                w.yview(cmd,arg1,arg2)
                Tk.Text.yview(self,cmd,arg1,arg2)
            else:
                w.yview(cmd,arg1)
                Tk.Text.yview(self,cmd,arg1)
    else:
        return w.yview()
</t>
<t tx="ekr.20060513122450.179">def setForBody(self,lo, hi):
    cc = self.cc
    #g.es("setforbody")
    Tk.Text.yview(self,'moveto',lo)	
    cc.LeoYBodyBar.set(lo,hi)	</t>
<t tx="ekr.20060513122450.180">def setForBar(self,lo, hi):
    cc = self.cc
    #g.es("setforbar")
    #cc.LeoBodyText.yview('moveto',lo)	
    cc.LeoYBodyBar.set(lo,hi)</t>
<t tx="ekr.20060513122450.181">def Plug(self):
    
    cc = self.cc
    
    cc.LeoYBodyBar.config(command=self.yview)
    cc.LeoBodyText["yscrollcommand"] = self.setForBody
    self["yscrollcommand"] = self.setForBar</t>
<t tx="ekr.20060513122450.182">def UnPlug(self):
    
    cc = self.cc
    
    cc.LeoYBodyBar.config(command=cc.LeoBodyText.yview)
    cc.LeoBodyText["yscrollcommand"] = cc.LeoYBodyBar.set
    self["yscrollcommand"] = None</t>
<t tx="ekr.20060513122450.183"></t>
<t tx="ekr.20060513122450.186">def OnRightClick(self,event):
    try:
        m = Tk.Menu(self)
        m.add_command(label="Delete Node Breaks", command=self.DeleteNodeBreaks)
        m.add_command(label="Delete Project Breaks", command=self.DeleteProjectBreaks)
        m.add_separator()
        m.add_command(label="Cancel",command=lambda :self.Cancel(m))
        
        m.post(event.x_root,event.y_root)
    except Exception:
        g.es_exception()
    self.cc.LeoYBodyBar.focus_set()</t>
<t tx="ekr.20060513122450.187">def OnLeftClick(self,event):

    cc = self.cc
    self["state"] = 'normal'	
    self.mark_set("insert","@0,"+str(event.y))
    self["state"] = 'disabled'
    l,c = self.index("insert").split(".")
    breaks = cc.cGet("BreakPoints")
    
    loc = LocatorClass(cc,cc.CHILD_NODE,l)
    if loc.FOUND_FILE_LINE == None:
        return
    
    filext = loc.FOUND_FILE_EXT.replace(".","")
    
    if l in breaks:
        self.DeleteBreak(filext,loc.FOUND_FILE_LINE,l)
    else:
        t = cc.LeoBodyText.get(str(l)+".0",str(l)+".end")
        if t != "\n" and t != "" and t.strip() != "@others":
            self.AddBreak(filext,loc.FOUND_FILE_LINE,l)
    
    self.tag_delete(Tk.SEL)
    self.cc.LeoYBodyBar.focus_set()</t>
<t tx="ekr.20060513122450.188"></t>
<t tx="ekr.20060513122450.189">def AddNodeBreak(self,l,s="Enabled"):
    self.cc.cGet("BreakPoints")[l] = s
</t>
<t tx="ekr.20060513122450.190">def DeleteNodeBreak(self,l):
    breaks = self.cc.cGet("BreakPoints")
    if l in breaks:
        del breaks[l]
</t>
<t tx="ekr.20060513122450.191">def ClearNodeBreaks(self):
    self.cc.cSet("BreakPoints",{})
</t>
<t tx="ekr.20060513122450.192">def BreaksFromNode(self):
    
    cc = self.cc
    self.ClearBreakTags()
    self.Sync()
    
    breaks = cc.cGet("BreakPoints",{})
    for l,s in breaks.iteritems():
        self.AddBarBreak(l,s)
        self.AddBreakTag(l)
</t>
<t tx="ekr.20060513122450.193"></t>
<t tx="ekr.20060513122450.194">def AddBarBreak(self,l,s="Enabled"):
    self["state"] = 'normal'
    #----------------------------------------
        
    fl = self.get(l+".0",l+".end")
    self.insert(l+".end",(int(self["width"])-len(str(fl))-1)*" "+"&gt;")
    self.tag_add(l,l+".0",l+".end")
    
    if s == "Enabled":
        self.tag_config(l,foreground="blue")
    else:
        self.tag_config(l,foreground="gray")
    #-----------------------------------------
    self["state"] = 'disabled'

</t>
<t tx="ekr.20060513122450.195">def DeleteBarBreak(self,l):
    self["state"] = 'normal'
    #----------------------------------------
    #self.insert(l+".end -2c","  ")
    self.delete(l+".end -1c",l+".end")
    self.tag_delete(l)	
    
    
    #-----------------------------------------
    self["state"] = 'disabled'
    self.update_idletasks()


</t>
<t tx="ekr.20060513122450.196">def ClearBarBreaks(self):
    
    cc = self.cc
    self["state"] = 'normal'
    self.delete(1.0,'end')	
    #----------------------------------------
    w =4
    if cc.CHILD_LINE and cc.CHILD_LINE != -1:
        yv = Tk.Text.yview(self)
        
        fl = cc.CHILD_LINE
        lines = cc.CHILD_NODE.bodyString().splitlines(True)
        l = ""
        while len(lines) &gt; 0:
            l = lines.pop(0)
            if l.strip() != "@others":
                self.insert("end",str(fl)+"\n")
                fl += 1
            else:
                break
            if len(lines)==0 and l[-1] == "\n":
                self.insert("end",str(fl)+"\n")
    
        if l.strip() == "@others":
            self.insert("end","\n")
            
            loc = LocatorClass(cc,cc.CHILD_NODE,fl-cc.CHILD_LINE+2)
            fl = loc.FOUND_FILE_LINE
            
            if fl != None:
                while len(lines) &gt; 0:
                    l = lines.pop(0)
                    self.insert("end",str(fl)+"\n")
                    fl += 1
                    if len(lines)==0 and l[-1] == "\n":
                        self.insert("end",str(fl)+"\n")
        if len(str(fl))+1 &lt; w:
            pass
        else:
            w = len(str(fl))+1
                    
        self.yview(yv)
        self.config(width = w)
    #-----------------------------------------
    self["state"] = 'disabled'

</t>
<t tx="ekr.20060513122450.197"></t>
<t tx="ekr.20060513122450.198">def AddBreakTag(self,l):
    
    w = self.cc.LeoBodyText
    
    w.tag_add("xcc_break",l+".0",l+".end")</t>
<t tx="ekr.20060513122450.199">def DeleteBreakTag(self,s,e=None):
    
    w = self.cc.LeoBodyText
    
    if e == None:
        w.tag_remove("xcc_break",s+".0",s+".end")
    else:
        w.tag_remove("xcc_break",s,e)</t>
<t tx="ekr.20060513122450.200">def ClearBreakTags(self):
    
    w = self.cc.LeoBodyText
    w.tag_delete("xcc_break")
    w.tag_config("xcc_break",background=self.bgcolor)</t>
<t tx="ekr.20060513122450.201">def BreaksFromTags(self):
    
    cc = self.cc
    w = self.cc.LeoBodyText
    self.ClearNodeBreaks()
    self.ClearBarBreaks()
    range = w.tag_nextrange("xcc_break","1.0")
    while len(range) &gt; 0:
        s,e = range
        el,ec = e.split(".")
        self.DeleteBreakTag(s,e)
        self.AddBreak(cc.CHILD_EXT,cc.CHILD_LINE,el)
        range = w.tag_nextrange("xcc_break",el+".end")</t>
<t tx="ekr.20060513122450.202">def AddBreak(self,filext,fileline,bodyline,state="Enabled"):
    
    cc = self.cc
    breaks = cc.sGet("BreakPoints",{})
    
    breaks[filext+":"+str(fileline)] = state
    
    bl = str(bodyline)
    self.AddNodeBreak(bl,state)
    self.AddBarBreak(bl,state)
    self.AddBreakTag(bl)
    
    if cc.ACTIVE_PROCESS:
        bpat = cc.DBG.get("Set break")
        bpat = bpat.replace("_FILE_",cc.NAME+"."+filext).replace("_LINE_",str(fileline))
        DbgTaskClass(cc,bpat)
        if cc.DBG_PROMPT:
            cc.DbgOut("")

</t>
<t tx="ekr.20060513122450.203">def DeleteBreak(self,filext,fileline,bodyline):
    
    cc = self.cc
        
    bl = str(bodyline)
    self.DeleteNodeBreak(bl)
    self.DeleteBarBreak(bl)
    self.DeleteBreakTag(bl)
    
    if cc.SELECTED_NODE == cc.ACTIVE_NODE:
        if cc.DBG.get("Clear break",'').find("_ID_") != -1:
            BreakIdTaskClass(cc,[filext,str(fileline)])
        else:
            DbgTaskClass(cc,cc.ReplaceVars(cc.DBG["Clear break"]).replace("_FILE_",cc.NAME+"."+filext).replace("_LINE_",str(fileline)))
        
        if cc.DBG_PROMPT:
            cc.DbgOut("")
</t>
<t tx="ekr.20060513122450.204">def DeleteNodeBreaks(self):
    try:
        cc = self.cc
  
        breaks = cc.cGet("BreakPoints",{})
        
        if cc.CHILD_LINE and cc.CHILD_EXT:
            for bp in breaks.keys():
                self.DeleteBreak(cc.CHILD_EXT,cc.CHILD_LINE+int(bp),int(bp))
    
        cc.cSelect(cc.CHILD_NODE)
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.205">def DeleteProjectBreaks(self):
    
    cc = self.cc
   
    if cc.SELECTED_NODE:
        for c in cc.SELECTED_NODE.subtree_iter():
            ua = cc.GetUnknownAttributes(c.v)
            if ua and "xcc_child_cfg" in ua.keys():
                if "BreakPoints" in ua["xcc_child_cfg"].keys():
                    ua["xcc_child_cfg"]["BreakPoints"] = {}
    
        cc.cSelect(cc.CHILD_NODE)</t>
<t tx="ekr.20060513122450.206">def Hide(self,erase = False):
    
    w = self.cc.LeoBodyText
    self.UnPlug()
    self.pack_forget()
    w.pack(expand=1, fill="both")
    w.tag_delete("xcc_break")
    self.visible = False</t>
<t tx="ekr.20060513122450.207">def Show (self):

    cc = self.cc
    self.Plug()
    
    cc.LeoBodyText.pack_forget()
    if self.leowrap != 'none':
        cc.LeoXBodyBar.pack(side="bottom",fill="x")
    border = cc.LeoBodyText ["bd"]
    self.config(pady=cc.LeoBodyText["pady"],bd=border)
    self.pack(side='left',fill="y")
    
    cc.LeoBodyText.pack(expand=1,fill="both")
    self.BreaksFromNode()
    self.visible = True</t>
<t tx="ekr.20060513122450.208">def Sync(self):
    
    cc = self.cc
    self["state"] = 'normal'
    self.delete(1.0,'end')	
    #----------------------------------------
    w=4    
    if cc.CHILD_LINE and cc.CHILD_LINE != -1:
        fl = cc.CHILD_LINE
        bs = cc.CHILD_NODE.bodyString()
        lines = bs.splitlines(True)
        
        while len(lines) &gt; 0:
            l = lines.pop(0)
            if l.strip() != "@others":
                self.insert("end",str(fl)+"\n")
                fl += 1
            else:
                break
    
        if len(lines) &gt; 0 and l.strip() == "@others":
            self.insert("end","\n")
            
            loc = LocatorClass(cc,cc.CHILD_NODE,fl-cc.CHILD_LINE+2)
            fl = loc.FOUND_FILE_LINE
            
            if fl != None:
                while len(lines) &gt; 0:
                    l = lines.pop(0)
                    self.insert("end",str(fl)+"\n")
                    fl += 1
                            
        if len(str(fl))+1 &lt; w:
            pass
        else:
            w = len(str(fl))+1
    self.config(width = w)
    cc.ToolBar.Spacer.config(width=w+1)
    #-----------------------------------------
    self["state"] = 'disabled'</t>
<t tx="ekr.20060513122450.209">def IdleUpdate(self):
    if self.bodychanged == True:
        t,b = Tk.Text.yview(self)
        self.BreaksFromTags()
        Tk.Text.yview(self,Tk.MOVETO,t)
        self.bodychanged = False</t>
<t tx="ekr.20060513122450.210">def Cancel(self,menu):
    menu.unpost()
    
</t>
<t tx="ekr.20060513122450.211"></t>
<t tx="ekr.20060513122450.212">class ParserClass:
    
    @others

</t>
<t tx="ekr.20060513122450.213"></t>
<t tx="ekr.20060513122450.214">def LoadCppRules(self):
    
    parser = self

    self.OUTFUNC_RULES = [
        self.ATRULE(),
        self.COMMENTRULE(parser),	#placed fisrt to allow functions and class to be commented out
        self.FUNCRULE(parser),
        self.CLASSRULE(parser),	#must be after CppFuncRule or it will catch template funcs
        self.DEFAULTRULE(parser)	#must be the last rule cos it always proceed
    ]
    
    self.RULES = self.OUTFUNC_RULES
    
    self.INFUNC_RULES = [
        self.ATRULE(),
        self.FUNCCOMMENTRULE(parser),	#placed fisrt to allow functions and class to be commented out
        self.FUNCASMRULE(parser),
        self.FUNCDEFAULTRULE(parser)	#must be the last rule cos it always proceed
    ]</t>
<t tx="ekr.20060513122450.218">class COMMENTRULE:
    @others</t>
<t tx="ekr.20060513122450.219">def Match(self,head):
    if head.startswith(self.Parser.cc.CMT):
        if head.endswith(";"):
            return True
        return False
    return None</t>
<t tx="ekr.20060513122450.220">def OnMatch(self,mo,node):
    
    p = self.Parser
    cc = p.cc    
    
    p.CURRENT_RULE = "comment"
    
    if mo:#put in source
        w = p.Define
        #cc.cSet("DESTINATION","SRC",node)
        head = node.headString()[2:-1]
    else:        
        if p.CLASS_WRITER:
            w = p.CLASS_WRITER
        else:
            w = p.Declare
        cc.cSet("DESTINATION","HDR",node)
        head = node.headString()[2:]
    
    #---------------------------------    
    p.StartDoc(head,node)#------------------------doc
    
    p.CURRENT_LOCATION = 0  #head
    
    p.Tab(p.cc.CMT)
    w(p.TAB_STRING+head+"\n")    
    
    if p.WriteOthers(node,w) == False:#---------------
        return False
    
    p.CURRENT_LOCATION = 2  #tail
    p.UnTab(p.cc.CMT)
    w("\n")

    p.EndDoc(node)#-------------------------------doc
    #----------------------------------
    
    return True


</t>
<t tx="ekr.20060513122450.221">class FUNCRULE:
    @others</t>
<t tx="ekr.20060513122450.222">def Match(self,head):	
   return SplitFunc(head)
    
</t>
<t tx="ekr.20060513122450.223">def OnMatch(self,mo,node):
    
    p = self.Parser
    p.CURRENT_RULE = "func"
    
    p.OnFunc(mo)
    
    spec,ret,name,params,pure,dest,ctors = self.Groups = p.CURRENT_FUNC_MO = mo
    
    if pure[0] == "":#define the func, possibly splitted
        if ";" in dest[0]:#put in source
            if "!" not in dest[0]:
                if self.DeclareFunc(p.Declare) == False:
                    return False
                return self.DefineFunc(p.Define,node)
            else:#no declaration in header
                return self.DefineFunc(p.Define,node,full=True)     
        
        else:
            if p.CLASS_WRITER:
                if p.CLASS_WRITER == p.Declare:#func is split
                    if ";" in dest[0]:#put in source
                        if self.DeclareFunc(p.CLASS_WRITER) == False:
                            return False
                        return self.DefineFunc(p.Define,node,push=True)
                    else:
                        return self.DefineFunc(p.Declare,node,full=True)            
                                        
                else:#func is not splitted, written with the class
                    return self.DefineFunc(p.CLASS_WRITER,node)
        
            else:
                return self.DefineFunc(p.Declare,node,full=True)
    
    else:#only declare the func, real destination depend upon DEST group and EXT
        if p.CLASS_WRITER:
            p.CURRENT_FUNC_DST = "HDR"
            p.cc.cSet("DESTINATION","HDR",node)
            return self.DeclareFunc(p.CLASS_WRITER)
            
        else:
            Error("xcc :","Pure virtual function outside a class is illegal!")
            #cc.GoToNode(node)
            return False</t>
<t tx="ekr.20060513122450.224">def DeclareFunc(self,wf):
    
    p = self.Parser
    spec,ret,name,params,pure,dest,ctors = self.Groups
    
    if name[0] == "":
        return False
    
    specs = spec[0].split()
    if "__asm" in specs:
        specs.remove("__asm")
        spec = (string.join(specs),spec[1],spec[2])
    
    
    p.CURRENT_FUNC = proto = spec[0] +" "+ ret[0] +" "+ name[0] + params[0] + pure[0] +";"
            
    p.CURRENT_LOCATION = 0  #head
    
    wf(p.TAB_STRING+proto.strip()+"\n")	
        
    return True</t>
<t tx="ekr.20060513122450.226">class CLASSRULE:
    @others</t>
<t tx="ekr.20060513122450.227">#spec class name base inst dest
def Match(self,head):
    #return self.Matcher.search(head)
    class_s = head.find("class ")
    if class_s &gt; -1:
        head = head.split()
        head = string.join(head)
        class_s = head.rfind("class ")
        
        spec = (head[:class_s],0,class_s)
        name_s = class_s+6		
        dest_s = head.find(";",name_s)
        inst_s = head.find("!",name_s)
        base_s = head.find(":",name_s)
        
        #dest -----------------------
        if dest_s &gt; -1:
            name_e = dest_s
            dest = (head[dest_s:dest_s+1],dest_s,dest_s+1)
            inst_e = dest_s
            base_e = dest_s
        else:
            dest = ("",-1,-1)
            name_e = inst_e = base_e = len(head)
        
        #inst --------------------------
        if inst_s &gt; -1:
            name_e = inst_s
            base_e = inst_s
            inst = (head[inst_s:inst_e],inst_s,inst_e)
        else:
            inst = ("",-1,-1)
        
        #base ---------------------------------		
        if base_s &gt; -1:
            name_e = base_s
            base = (head[base_s:base_e],base_s,base_e)
        else:
            base = ("",-1,-1)
        
        name = (head[name_s:name_e],name_s,name_e)
                
        return (spec,name,base,inst,dest)
            
    return None</t>
<t tx="ekr.20060513122450.228">def OnMatch(self,mo,node):
    # global LOCATE_CHILD
    
    p = self.Parser
    cc = p.cc
    
    p.CURRENT_RULE = "class"
    
    spec,name,base,inst,dest = mo
    
    #determine where to write
    if len(p.CLASS_LIST) == 0:#redirect only for the root class
        if dest[0] != "":#directed toward source
            p.CLASS_WRITER = p.Define
            push = True
        else:
            p.CLASS_WRITER = p.Declare
            push = False
    else:
        if p.CLASS_WRITER == p.Declare:
            push = False
        else:
            push = True
    
    cw = p.CLASS_WRITER
    
    cdec = ""
    
    if spec[0] != "":
        cdec += spec[0]+" "
    
    if name[0] == "":
        p.cc.ToolBar.SetError("No name in class definition :"+GetNodePath(p.CURRENT_NODE),p.CURRENT_NODE)
        return False
    
    cdec += "class "+name[0]
    
    if base[0] != "":
        cdec += base[0]
        
    if push == True:
        p.PushTab()
    
    #---------------------------------
    p.StartDoc(name[0],node)#-------------------------------

    p.CLASS_LIST.append(name[0])#-------------------------
    p.CURRENT_LOCATION = 0  #head
    
    cw(p.TAB_STRING+cc.CLASS_HDR)
    
    cw(p.TAB_STRING+cdec+cc.CLASS_OPN+"\n")
    p.Tab()
    
    if p.WriteOthers(node,cw) == False:#------------------
        return False
    
    p.UnTab()
    
    inst = inst[0][1:]
    ce = cc.CLASS_END.replace("_INST_",inst)
        
    cw(p.TAB_STRING+ce+"\n")
    p.CURRENT_LOCATION = 2  #tail
    p.CLASS_LIST.pop()#-----------------------------------

    p.EndDoc(node)#--------------------------------------
    #---------------------------------
    
    push and p.PopTab()

    if len(p.CLASS_LIST) == 0:
        p.CLASS_WRITER = None		
    
    return True
</t>
<t tx="ekr.20060513122450.229">class DEFAULTRULE:
    @others</t>
<t tx="ekr.20060513122450.230">def __init__(self,Parser):
    
    self.Parser = Parser
    self.Matcher = re.compile("(?P&lt;HEAD&gt;[^;]*)(?P&lt;DEST&gt;;$)*")</t>
<t tx="ekr.20060513122450.231">def Match(self,head):
    return head.endswith(";")</t>
<t tx="ekr.20060513122450.232">def OnMatch(self,mo,node):
        
    p = self.Parser
    cc = p.cc
    
    if mo:#put in source
        w = p.Define
        head = node.headString()[:-1]        
    else:        
        if p.CLASS_WRITER:
            w = p.CLASS_WRITER
        else:
            w = p.Declare
        head = node.headString()          
        
    p.CURRENT_RULE = "default"        
    
    #---------------------------    
    p.StartDoc(head,node)#----------------------------------
    
    p.CURRENT_LOCATION = 0  #head
    w(p.TAB_STRING+cc.CMT+head+"\n")
    
    #p.Tab() - for python compatibility
    if p.WriteOthers(node,w) == False:#-----------------------
        return False    
    #p.UnTab()- for python compatibility
    
    p.CURRENT_LOCATION = 2  #tail	
    w("\n")
    
    p.EndDoc(node)#---------------------------------------------
    #----------------------------
    return True</t>
<t tx="ekr.20060513122450.233">class FUNCCOMMENTRULE:
    @others</t>
<t tx="ekr.20060513122450.234">def __init__(self,Parser):
    
    self.Parser = Parser	
    self.Matcher = re.compile("^//(?P&lt;HEAD&gt;.*)")
    </t>
<t tx="ekr.20060513122450.235">def Match(self,head):
    return self.Matcher.search(head)
</t>
<t tx="ekr.20060513122450.236">def OnMatch(self,mo,node):
    
    p = self.Parser
    p.CURRENT_RULE = "funccomment"
    
    w = p.FUNC_WRITER
    groups = mo.groupdict()
    
    head = groups["HEAD"]
    if head == None:
        head = ""
        
    p.CURRENT_LOCATION = 0  #head
    p.Tab(p.cc.CMT)
    w(p.TAB_STRING+head+"\n")
    
    if p.WriteOthers(node,w) == False:
        return False
    
    p.CURRENT_LOCATION = 2  #tail
    p.UnTab(p.cc.CMT)
    w("\n")

    return True
</t>
<t tx="ekr.20060513122450.237">class FUNCDEFAULTRULE:
    @others</t>
<t tx="ekr.20060513122450.238">def __init__(self,Parser):
    
    self.Parser = Parser
    self.Matcher = re.compile("(?P&lt;HEAD&gt;.*)")</t>
<t tx="ekr.20060513122450.239">def Match(self,head):

    return self.Matcher.search(head)
</t>
<t tx="ekr.20060513122450.240">def OnMatch(self,mo,node):
    
    p = self.Parser
    p.CURRENT_RULE = "funcdefault"
    
    w = p.FUNC_WRITER
    groups = mo.groupdict()

    head = groups["HEAD"]
    if head == None:
        head = ""
    
    #---------------------------    
    p.StartDoc(head,node)#----------------------------------
    
    p.CURRENT_LOCATION = 0  #head
    w(p.TAB_STRING+p.cc.CMT+head+"\n")
    p.Tab()
    
    if p.WriteOthers(node,w) == False:
        return False
    
    p.UnTab()	
    p.CURRENT_LOCATION = 2  #tail
    w("\n")    
    p.EndDoc(node)#---------------------------------------------
    #----------------------------
    return True
</t>
<t tx="ekr.20060513122450.241">def __init__(self,cc):
    self.cc = cc
    
    self.__name__ = "ParserClass"
    self.DO_PARSE = True	
    self.NOW_PARSING = False
    
    self.RULES = []	
    self.OnStart = None
    self.OnEnd = None    
    
    self.DEC_PROC_LIST = []
    self.DEF_PROC_LIST = []
    self.DOC_PROC_LIST = []
    self.OPN_PROC_LIST = []
    
    self.BODY_LINE_STACK = []
    
    self.CURRENT_SRC_LINE = 0
    self.CURRENT_HDR_LINE = 0
    self.CURRENT_DOC_LINE = 0
    
    self.CURRENT_BODY_LINE = 0
    self.CURRENT_VNODE = None
    self.CURRENT_NODE = None
    self.CURRENT_LOCATION = 0   # 0 = head, 1 = body, 2 = tail
    self.PYWNODE = None
    
    self.CURRENT_RULE = ""
    self.CURRENT_MO = None
    self.CURRENT_FUNC = ""
    self.CURRENT_FUNC_DST = ""
    
    self.DECLARE_IN_HDR = True
    self.DEFINE_IN_SRC = True	
    
    self.CLASS_LIST = []
    self.CLASS_WRITER = None
    self.FUNC_WRITER = None
    
    self.TAB_STRING = ""
    self.TAB_LIST = []
    
    self.PARSE_TIME = 0.0
    
    self.DOC_NAMES = []</t>
<t tx="ekr.20060513122450.242">def Declare(self,text):
    lines = text.splitlines()
    #lc = len(lines)
    
    for l in lines:
        if self.CURRENT_LOCATION == 1:  #body
            self.CURRENT_BODY_LINE += 1		
        else:
            self.CURRENT_BODY_LINE = 0

        if self.DECLARE_IN_HDR == True:
            self.CURRENT_HDR_LINE += 1      
        else:
            self.CURRENT_SRC_LINE += 1       
        
        for d in self.DEC_PROC_LIST:
            d(l+"\n")
</t>
<t tx="ekr.20060513122450.243">def Define(self,text):
    lines = text.splitlines()      
    
    #if len(lines)==1 and lines[0]=="":
    #    return
    
    for l in lines:
        if self.CURRENT_LOCATION == 1:  #body
            self.CURRENT_BODY_LINE += 1		
        else:
            self.CURRENT_BODY_LINE = 0
    
        if self.DEFINE_IN_SRC == True:
            self.CURRENT_SRC_LINE += 1      
        else:
            self.CURRENT_HDR_LINE += 1       
        
        for d in self.DEF_PROC_LIST:
            d(l+"\n")
</t>
<t tx="ekr.20060513122450.244">def Docum(self,text):
    if self.CURRENT_LOCATION == 1:  #body
        self.CURRENT_BODY_LINE += 1		
    else:
        self.CURRENT_BODY_LINE = 0

    self.CURRENT_DOC_LINE += 1
        
    for d in self.DOC_PROC_LIST:
        d(text)</t>
<t tx="ekr.20060513122450.245">def PushBodyLine(self):
    self.BODY_LINE_STACK.insert(0,self.CURRENT_BODY_LINE)
</t>
<t tx="ekr.20060513122450.246">def PopBodyLine(self):
    self.CURRENT_BODY_LINE = self.BODY_LINE_STACK.pop(0)
    
    
</t>
<t tx="ekr.20060513122450.248"></t>
<t tx="ekr.20060513122450.249">def Tab(self,sym="\t"):
    self.TAB_STRING += sym</t>
<t tx="ekr.20060513122450.250">def UnTab(self,sym="\t"):
    self.TAB_STRING = self.TAB_STRING[:-len(sym)] 
</t>
<t tx="ekr.20060513122450.251">def PushTab(self):
    self.TAB_LIST.append(self.TAB_STRING)
    self.TAB_STRING = ""</t>
<t tx="ekr.20060513122450.252">def PopTab(self):
    self.TAB_STRING = self.TAB_LIST.pop(-1)</t>
<t tx="ekr.20060513122450.253">def TabWrite(self,text,outfunc):
    lines = text.splitlines(True)
    #if len(lines)==1 and lines[0]=="\n":
    #    return
    for l in lines:
        outfunc(self.TAB_STRING+l)
</t>
<t tx="ekr.20060513122450.254">def WriteOthers(self,node,w):
    
    cc = self.cc
    if cc.CREATE_DOC == "True":
        doc = cc.cGet("DOC","",node)
        self.Docum(doc)
        
    b = node.bodyString().strip("\n")
    o = b.find("@others")
    
    self.CURRENT_LOCATION = 1   #body
    
    if o != -1:
        lb = b[:o]
        pnl = lb.rfind("\n")
        if pnl &gt; -1:
            lb = lb[:pnl]
        
        tb = b[o+7:]
        pnl = tb.find("\n")		
        if pnl &gt; -1:
            tb = tb[pnl+1:]        
        
        if lb != "":
            self.TabWrite(lb+"\n",w)
        self.PushBodyLine()
        if self.ParseNode(node) == False:
            return False
        self.PopBodyLine()
        self.CURRENT_LOCATION = 1   #body
        self.TabWrite(b[o+7:]+"\n",w)
        #self.TabWrite(b[o+7:],w)
    else:        
        #self.TabWrite(b+"\n",w)
        self.TabWrite(b,w)
        if self.ParseNode(node) == False:
            return False
    
    return True
</t>
<t tx="ekr.20060513122450.255">def Parse(self):
    
    cc = self.cc
    #----------------------------------------------
    self.LoadCppRules()
        
    if cc.EXT == cc.SRC_EXT:
        self.DECLARE_IN_HDR = False
    
    if cc.EXT == cc.HDR_EXT:
        self.DEFINE_IN_SRC = False
    #-----------------------------------------------------
    self.CURRENT_VNODE = cc.SELECTED_NODE.v
    self.CURRENT_NODE = cc.SELECTED_NODE
    
    #-----------------------------------------------------
    if self.NOW_PARSING == True:
        Error("xcc: ","Already parsing!")
        return False
    
    self.NOW_PARSING = True    
    #------------------------------------------------------
    
    
    if not (self.OnStart and self.OnStart()):
        return False
        
    
            
    self.PushDoc(cc.NAME)
    
    time.clock()
    start = time.clock()
    
    if self.DEFINE_IN_SRC and self.DECLARE_IN_HDR:
        if cc.OPTS.get("Auto include header") == "True":
            self.Define("#include \""+cc.NAME+".h\"\n")
    
    self.Docum(cc.sGet("DOC",""))
    #------------------------------------------------------		
    res = self.ParseNode(cc.SELECTED_NODE,reset=True)	
    #------------------------------------------------------
    if res:
        self.PopDoc()
    
    self.PARSE_TIME = time.clock()-start
    self.OnEnd and self.OnEnd()	
    #g.es(self.PARSE_TIME)
    
    return res

</t>
<t tx="ekr.20060513122450.256">def OnParseNode(self,node,back=False):
    self.CURRENT_VNODE = node.v
    self.CURRENT_NODE = node.copy()
    for opn in self.OPN_PROC_LIST:
        opn(node,back)
</t>
<t tx="ekr.20060513122450.257">def ParseNode(self,node,reset=False):
    cc = self.cc
    
    if self.DO_PARSE == False:
        return False
        
    for cn in node.children_iter():        
        
        self.OnParseNode(cn)		
        ch = cn.headString()		
        
        tcr = self.CURRENT_RULE
        tcmo = self.CURRENT_MO
        
        for r in self.RULES:
            result = r.Match(ch)
            if result != None:
                self.CURRENT_MO = result
                if r.OnMatch(result,cn) == False or self.DO_PARSE == False:
                    return False
                else:
                    cc.cSet("RULE",self.CURRENT_RULE,cn)
                break
        
        self.CURRENT_RULE = tcr
        self.CURRENT_MO = tcmo
    
    if node != cc.SELECTED_NODE:
        self.OnParseNode(node,True)
    
    return True</t>
<t tx="ekr.20060513122450.259">class WriterClass(ParserClass):

    @others
</t>
<t tx="ekr.20060513122450.260">def __init__(self,cc):
    
    self.Result = False
    
    self.BeginHtml = "&lt;!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\"&gt;\n&lt;html&gt;\n&lt;head&gt;\n&lt;title&gt;TITLE&lt;/title&gt;\n&lt;meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\"&gt;\n&lt;/head&gt;\n&lt;body&gt;"
    
    self.EndHtml = "&lt;/body&gt;\n&lt;/html&gt;"
    self.DocTab = -5
    
    self.DOC_FILES = [] #must be initialized before cppparse is called
    self.DOC_MENU = None #
    self.DOC_NAMES = [] #
    self.DOC_FOLDER = cc.NAME+"_doc"
    
    ParserClass.__init__(self,cc)
    self.__name__ = "WriterClass"
    self.OnStart = self.OnWriteStart
    self.OnEnd = self.OnWriteEnd
    
    self.Result = self.Parse()
    #g.trace('WriteClass.Result',self.Result)
</t>
<t tx="ekr.20060513122450.261">def OnWriteStart(self):    
    
    cc = self.cc
        
    self.HDR_FILE = None
    self.SRC_FILE = None
    
    if cc.ABS_PATH != "":
        name = cc.ABS_PATH+"/"+cc.NAME
    else:
        name = cc.NAME
    
    cc.OUTEXT = cc.BIN_EXT
    if cc.OPTS.get("Source files") == "True":
        #create exe using .h and .cpp files
        if cc.EXT == cc.BIN_EXT or cc.EXT == "dll" or cc.EXT == "so":
            cc.sAddText("\" writing "+name+"."+cc.HDR_EXT+" and "+name+"."+cc.SRC_EXT+"...\n")
            self.HDR_FILE = file(name+"."+cc.HDR_EXT,"w+")
            self.SRC_FILE = file(name+"."+cc.SRC_EXT,"w+")
            if cc.EXT == "dll" or cc.EXT == "so":
                cc.OUTEXT = cc.EXT
        #create a header and verify syntaxe	
        if cc.EXT == cc.HDR_EXT:
            cc.sAddText("\" writing "+name+"."+cc.HDR_EXT+"...\n")
            self.HDR_FILE = file(name+"."+cc.HDR_EXT,"w+")
        
        #create exe using .cpp or .c file
        if cc.EXT == cc.SRC_EXT:
            cc.sAddText("\" writing "+name+"."+cc.EXT+"...\n")
            self.SRC_FILE = file(name+"."+cc.EXT,"w+")
            
                
        if self.HDR_FILE == None and self.SRC_FILE == None:
            Error("xcc: ","Unable to open output file(s)!")
            return False	
    
        #------------------------------------------
        if self.DECLARE_IN_HDR:
            self.DEC_PROC_LIST.append(self.HDR_FILE.write)
        else:
            self.DEC_PROC_LIST.append(self.SRC_FILE.write)
        
        if self.DEFINE_IN_SRC:
            self.DEF_PROC_LIST.append(self.SRC_FILE.write)
        else:
            self.DEF_PROC_LIST.append(self.HDR_FILE.write)
    
    if cc.CREATE_DOC == "True":
        self.CreateBaseDoc() 
        self.DOC_PROC_LIST.append(self.WriteDoc)

    return True</t>
<t tx="ekr.20060513122450.262">def OnWriteEnd(self):
    
    if self.HDR_FILE:
        self.HDR_FILE.write("\n")
        self.HDR_FILE.close()
        self.HDR_FILE = None
        
    if self.SRC_FILE:
        self.SRC_FILE.write("\n")
        self.SRC_FILE.close()
        self.SRC_FILE = None
        
    for df in self.DOC_FILES:
        if df:
            df.write(self.EndHtml)
            df.close()
            
    if self.DOC_MENU != None:
        self.DOC_MENU.close()</t>
<t tx="ekr.20060513122450.263">class BreakFinderClass(ParserClass):
    @others</t>
<t tx="ekr.20060513122450.264">def __init__(self,cc):
    
    self.Result = False
    ParserClass.__init__(self,cc)
    self.OnStart = self.OnFindStart
    self.Result = self.Parse()
</t>
<t tx="ekr.20060513122450.265">def OnFindStart(self):
    # loading event funcs
    if self.DECLARE_IN_HDR:
        self.DEC_PROC_LIST.append(self.BreakDec)		
    else:
        self.DEC_PROC_LIST.append(self.BreakDef)
        
    if self.DEFINE_IN_SRC:
        self.DEF_PROC_LIST.append(self.BreakDef)
    else:
        self.DEF_PROC_LIST.append(self.BreakDec)		
        
    self.OPN_PROC_LIST.append(self.BreakOPN)
    
    self.BREAKS = {}
    
    self.CURRENT_BREAKS = None

    return True</t>
<t tx="ekr.20060513122450.267">def BreakDec(self,text):
    
    cbl = self.CURRENT_BODY_LINE
    cb = self.CURRENT_BREAKS	
    
    if cb and str(cbl) in cb:
        self.BREAKS["h:"+str(self.CURRENT_HDR_LINE)] = cb[str(cbl)]</t>
<t tx="ekr.20060513122450.268">def BreakDef(self,text):
    
    cbl = self.CURRENT_BODY_LINE
    cb = self.CURRENT_BREAKS
    
    if cb and str(cbl) in cb:
        self.BREAKS[self.cc.SRC_EXT+":"+str(self.CURRENT_SRC_LINE)] = cb[str(cbl)]
</t>
<t tx="ekr.20060513122450.269">def BreakOPN(self,node,back=False):
    
    cc = self.cc
    
    txcd = cc.cGetDict(node)
   
    self.CURRENT_BREAKS = txcd.get("BreakPoints")</t>
<t tx="ekr.20060513122450.270">class SeekErrorClass(ParserClass):
    @others</t>
<t tx="ekr.20060513122450.271">def __init__(self,cc,line,ext,col="0",color="red"):

    ParserClass.__init__(self,cc)		
    self.SEEK_LINE = line
    self.SEEK_COL = col
    self.SEEK_EXT = ext
    self.FOUND_NODE = None
    self.FOUND_INDEX = "1."+col
    self.OnStart = self.OnStartSeek
    
    if self.Parse() == False and self.FOUND_NODE:
        cc.GoToNode(self.FOUND_NODE,self.FOUND_INDEX,tagcolor=color)
    else:
        Error("xcc: ","Unable to find line: "+str(line))</t>
<t tx="ekr.20060513122450.272">def OnStartSeek(self):
    
    if self.DECLARE_IN_HDR:
        self.DEC_PROC_LIST.append(self.SeekDec)
    else:
        self.DEC_PROC_LIST.append(self.SeekDef)    
    
    if self.DEFINE_IN_SRC:
        self.DEF_PROC_LIST.append(self.SeekDef)
    else:
        self.DEF_PROC_LIST.append(self.SeekDec)
    
    return True</t>
<t tx="ekr.20060513122450.273">def SeekDec(self,text):
    if self.DO_PARSE:
        if self.CURRENT_HDR_LINE == self.SEEK_LINE and self.SEEK_EXT == self.cc.HDR_EXT:
            index = None
            if self.CURRENT_LOCATION == 0:  #head
                index = "1."+self.SEEK_COL
            if self.CURRENT_LOCATION == 1:  #body
                index = str(self.CURRENT_BODY_LINE)+"."+self.SEEK_COL
            if self.CURRENT_LOCATION == 2:  #tail
                index = "1000."+self.SEEK_COL
            
            self.DO_PARSE = False
            self.FOUND_NODE = self.CURRENT_NODE.copy()
            self.FOUND_INDEX = index</t>
<t tx="ekr.20060513122450.274">def SeekDef(self,text):
    if self.DO_PARSE:
        if self.CURRENT_SRC_LINE == self.SEEK_LINE and self.SEEK_EXT == self.cc.SRC_EXT:
            index = None
            if self.CURRENT_LOCATION == 0:  #head
                index = "1."+self.SEEK_COL
            if self.CURRENT_LOCATION == 1:  #body
                index = str(self.CURRENT_BODY_LINE)+"."+self.SEEK_COL
            if self.CURRENT_LOCATION == 2:  #tail
                index = "1000."+self.SEEK_COL
            
            self.DO_PARSE = False
            self.FOUND_NODE = self.CURRENT_NODE.copy()
            self.FOUND_INDEX = index</t>
<t tx="ekr.20060513122450.275">class LocatorClass(ParserClass):
    @others
</t>
<t tx="ekr.20060513122450.276">def __init__(self,cc,node,line):
    
    ParserClass.__init__(self,cc)		
        
    self.LOCATE_NODE = node
    self.LOCATE_BODY_LINE = int(line)
    self.FOUND_FILE_LINE = None
    self.FOUND_FILE_EXT = None

    self.OnStart = self.OnStartLocate
    
    self.Parse()</t>
<t tx="ekr.20060513122450.277">def OnStartLocate(self):
    if self.DECLARE_IN_HDR:
        self.DEC_PROC_LIST.append(self.LocateDec)
    else:
        self.DEC_PROC_LIST.append(self.LocateDef)
    
    
    if self.DEFINE_IN_SRC:
        self.DEF_PROC_LIST.append(self.LocateDef)
    else:
        self.DEF_PROC_LIST.append(self.LocateDec)
    
    self.DOC_PROC_LIST.append(self.LocateDoc)
    
    return True
</t>
<t tx="ekr.20060513122450.278">def LocateDec(self,text):
    if self.DO_PARSE == True:
        if self.CURRENT_NODE == self.LOCATE_NODE:
            if self.CURRENT_RULE == "func" and self.CURRENT_MO[4][0]!= "":
                self.FOUND_FILE_LINE = -1                
                self.FOUND_FILE_LINE = self.CURRENT_HDR_LINE
                self.FOUND_FILE_EXT = self.cc.HDR_EXT                
                self.DO_PARSE = False
                
                return
            
            if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                if self.DECLARE_IN_HDR == True:
                    self.FOUND_FILE_LINE = self.CURRENT_HDR_LINE
                    self.FOUND_FILE_EXT = self.cc.HDR_EXT                    
                else:
                    self.FOUND_FILE_LINE = self.CURRENT_SRC_LINE
                    self.FOUND_FILE_EXT = self.cc.SRC_EXT
                    
                    
                self.DO_PARSE = False
                
                </t>
<t tx="ekr.20060513122450.279">def LocateDoc(self,text):
    if self.DO_PARSE:
        if self.CURRENT_NODE == self.LOCATE_NODE:
            if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                self.FOUND_FILE_LINE = self.CURRENT_DOC_LINE
                self.FOUND_FILE_EXT = "html"
                self.DO_PARSE = False</t>
<t tx="ekr.20060513122450.281"></t>
<t tx="ekr.20060513122450.282">def aSet(self,name,value):
    
    cc = self
    
    cc.ACTIVE_DICT[name] = value
</t>
<t tx="ekr.20060513122450.283">def aGet(self,name,init=""):
    
    cc = self
    
    if name not in cc.ACTIVE_DICT:
        cc.aSet(name,init)

    return cc.ACTIVE_DICT[name]
</t>
<t tx="ekr.20060513122450.284">def aGetDict(self):
    
    '''Get xcc parent dict alias "xcc_cfg" in uA.'''
    
    cc = self

    if not cc.ACTIVE_NODE:
        return None
    
    v = cc.ACTIVE_NODE.v	
    if not hasattr(v,"unknownAttributes"):
        v.unknownAttributes = {}
    
    if "xcc_cfg" not in v.unknownAttributes:
        v.unknownAttributes["xcc_cfg"] = {}
    
    return v.unknownAttributes.get("xcc_cfg")</t>
<t tx="ekr.20060513122450.285">def aGo(self):
    
    #g.trace()
    
    cc = self
    
    if cc.ACTIVE_NODE:
        s = cc.DBG.get("Continue")
        if s:
            cc.aWrite(s)
            cc.LeoBodyText.tag_delete("xcc_error")
            cc.ToolBar.DisableStep()</t>
<t tx="ekr.20060513122450.286">def aStop(self):
    try:
        cc = self
   
        if not cc.ACTIVE_NODE or not cc.ACTIVE_PROCESS:
            return Error("xcc: ","Current xcc node is not active!")

        if cc.ACTIVE_NODE == cc.SELECTED_NODE and cc.TARGET_PID:
            stop = cc.DBG.get("Stop")
            if cc.DBG_PROMPT:
                if stop: cc.aWrite(stop)
            else:
                pause(cc.TARGET_PID)
                if stop: cc.DBG_TASK.append(DbgTaskClass(cc,stop))					
            
            cc.LeoBodyText.tag_delete("xcc_error")
            if cc.WATCH_TASK: cc.WATCH_TASK.Cancel()
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.287">def aStepIn(self):
    try:
        cc = self
   
        if (
            cc.ACTIVE_NODE and cc.ACTIVE_PROCESS and
            cc.ACTIVE_NODE == cc.SELECTED_NODE and
            cc.DBG["Step in"] != "" and cc.DBG_PROMPT
        ):
            cc.DBG_STEPPING = True
            cc.aWrite(cc.DBG["Step in"])
            cc.ToolBar.DisableStep()
            cc.LeoBodyText.tag_delete("xcc_error")
            cc.DBG_TASK.append(QueryGoTaskClass(cc))
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.288">def aStepOver(self):
    try:
        cc = self
    
        if (
            cc.ACTIVE_NODE and cc.ACTIVE_PROCESS and
            cc.ACTIVE_NODE == cc.SELECTED_NODE and
            cc.DBG.get("Step in") and cc.DBG_PROMPT
        ):
            cc.DBG_STEPPING = True			
            cc.aWrite(cc.DBG["Step over"])
            cc.ToolBar.DisableStep()
            cc.LeoBodyText.tag_delete("xcc_error")
            cc.DBG_TASK.append(QueryGoTaskClass(cc))
    except Exception:
        g.es_exception()
</t>
<t tx="ekr.20060513122450.289">def aStepOut(self):
    try:
        cc = self

        if (
            cc.ACTIVE_NODE and cc.ACTIVE_PROCESS and
            cc.ACTIVE_NODE == cc.SELECTED_NODE and
            cc.DBG.get("Step in") and cc.DBG_PROMPT
        ):
            cc.DBG_STEPPING = True
            cc.aWrite(cc.DBG["Step out"])
            cc.ToolBar.DisableStep()
            cc.LeoBodyText.tag_delete("xcc_error")
            cc.DBG_TASK.append(QueryGoTaskClass(cc))
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.290">def aPause(self):
    try:
        cc = self
    
        if not cc.ACTIVE_NODE or not cc.ACTIVE_PROCESS:
            Error("xcc: ","Current xcc node is not active!")

        elif cc.ACTIVE_NODE == cc.SELECTED_NODE and cc.TARGET_PID:
            pause(cc.TARGET_PID)
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.291">def aWrite(self,text):
    
    cc = self

    if not cc.FILTER_OUTPUT:
        cc.aAddText(text+"\n")
    
    eol = ""   
    code = "eol = \""+cc.EOL+"\""    
    try:
        exec code
    except:
        TraceBack()
    
    if eol == "":
        eol = "\n"
    
    cc.ACTIVE_PROCESS.In.write(text+eol)
    cc.ACTIVE_PROCESS.In.flush()
    cc.DBG_PROMPT = False
    cc.ToolBar.PauseButton["state"] = 'normal'
    
    if cc.DEBUG and cc.EXECUTE:
        cc.ToolBar.HideInput()</t>
<t tx="ekr.20060513122450.292">def aSelect(self,node=None):
    
    cc = self

    cc.ACTIVE_NODE = node
    cc.ACTIVE_DICT = cc.aGetDict()</t>
<t tx="ekr.20060513122450.293">def aSetText(self,text=""):
    
    cc = self
    
    if cc.ACTIVE_NODE:
        cc.c.setBodyString(ACTIVE_NODE,text)</t>
<t tx="ekr.20060513122450.294">def aAddText(self,text):
    
    cc = self
    
    if cc.ACTIVE_NODE:
        cc.c.setBodyString(cc.ACTIVE_NODE,cc.ACTIVE_NODE.bodyString()+text)
    
        if cc.SELECTED_NODE == cc.ACTIVE_NODE and cc.CHILD_NODE==None:
            l,c = cc.LeoBodyText.index("end").split(".")
            cc.LeoBodyText.see(l+".0")</t>
<t tx="ekr.20060513122450.295"></t>
<t tx="ekr.20060513122450.296"></t>
<t tx="ekr.20060513122450.297"></t>
<t tx="ekr.20060513122450.298"></t>
<t tx="ekr.20060513122450.299"></t>
<t tx="ekr.20060513122450.300"></t>
<t tx="ekr.20060513122450.301"></t>
<t tx="ekr.20060513122450.302"></t>
<t tx="ekr.20060513122450.303">def sExtractHeadInfo (self):
    
    cc = self

    w = cc.SELECTED_NODE.headString() [5:]
    if w:
        path, name = os.path.split(w)
        name, ext = os.path.splitext(name)
        ext = ext.lower().replace(".","") or 'exe'
    else:
        path, name, ext = '', '', ''

    cc.sSet("REL_PATH",path)
    cc.sSet("NAME",name)
    cc.sSet("EXT",ext)
    theDir = g.choose(path,cc.CWD+"/"+path,cc.CWD)
    cc.sSet("ABS_PATH",theDir)</t>
<t tx="ekr.20060513122450.304">def sGetBrowseInfo (self):
    cc = self
    
    
    w = cc.SELECTED_NODE.headString() [5:]
    if w:
        cc.REL_PATH, cc.NAME = os.path.split(w)
        cc.NAME, EXT = os.path.splitext(cc.NAME)
        cc.EXT = EXT.lower().replace(".","")
    else:
        cc.REL_PATH, cc.NAME, cc.EXT = '', '', ''    

    cc.CWD = cc.ABS_PATH = cc.c.openDirectory#os.getcwd().replace("\\","/")
    
    if cc.REL_PATH and cc.REL_PATH[1] != ":": cc.ABS_PATH = cc.ABS_PATH + "/" + cc.REL_PATH
    
    cc.ABS_PATH = cc.ABS_PATH.replace("\\",path_sym)
    cc.REL_PATH = cc.REL_PATH.replace("\\",path_sym)
    
    cc.OPTS = cc.sGet("Options",{})
    cc.LANG = cc.sGet("Language",{})
    cc.HDR_EXT = GetDictKey(cc.LANG,"Header ext",create=True,init="h")
    cc.SRC_EXT = GetDictKey(cc.LANG,"Source ext",create=True,init="c")
    cc.BIN_EXT = GetDictKey(cc.LANG,"Binary ext",create=True,init="exe")
    
    
    co = GetDictKey(cc.LANG,"Class opening",create=True,init="")
    ce = GetDictKey(cc.LANG,"Class closing",create=True,init="")
    fo = GetDictKey(cc.LANG,"Fonction opening",create=True,init="")
    fe = GetDictKey(cc.LANG,"Fonction closing",create=True,init="")
    
    code = "self.CLASS_OPN = \""+co+"\"\n"
    code += "self.CLASS_END = \""+ce+"\"\n"
    code += "self.FUNC_OPN = \""+fo+"\"\n"
    code += "self.FUNC_END = \""+fe+"\""
    
    try:
        exec code
    
    except Exception as e:
        Error("xcc :sGetBrowseInfo()",e)
    
    
    
    
    if cc.EXT == "":
        cc.EXT = cc.BIN_EXT</t>
<t tx="ekr.20060513122450.305">def sGetWriteInfo(self):
    
    cc = self
    
    if cc.NAME == "":
        return Error("xcc: ","Node have no name!")
        
    cc.CMT = GetDictKey(cc.LANG,"Comment symbol",create=True,init="//")
    if cc.CMT == "":
        cc.CMT = cc.LANG["Comment symbol"] = "//"
    
    
    if cc.REL_PATH != "" and os.access(cc.ABS_PATH,os.F_OK) != 1:
        os.makedirs(cc.ABS_PATH)
    
    if cc.OPTS.get("Create files") == "True":
        cc.CREATE_DOC = cc.OPTS.get("Doc files")
        cc.PYWRAP = cc.OPTS.get("Python wrapper")
    else:
        cc.CREATE_DOC = "False"
        cc.PYWRAP = "False"
    
    
        
    co = GetDictKey(cc.LANG,"Class opening",create=True,init="")
    ce = GetDictKey(cc.LANG,"Class closing",create=True,init="")
    fo = GetDictKey(cc.LANG,"Fonction opening",create=True,init="")
    fe = GetDictKey(cc.LANG,"Fonction closing",create=True,init="")
    
    code = "self.CLASS_OPN = \""+co+"\"\n"
    code += "self.CLASS_END = \""+ce+"\"\n"
    code += "self.FUNC_OPN = \""+fo+"\"\n"
    code += "self.FUNC_END = \""+fe+"\""
    
    try:
        exec code
    
    except Exception as e:
        Error("xcc :sGetWriteInfo()",e)
    
    self.CLASS_HDR = self.CMT+5*"------------------"+"\n"
    self.FUNC_HDR = self.CMT+5*"------------------"+"\n"
    
    return True</t>
<t tx="ekr.20060513122450.306">def sGetCompileInfo(self):
    
    cc = self
    cc.CPL = cc.sGet("Compiler")
    cc.LKR = cc.sGet("Linker")

    if not cc.CPL.get("Compiler"):
        return Error("xcc: ","No compiler defined!")
        
    cc.VERBOSE = StrToBool(cc.OPTS.get("Xcc verbose"))
    cc.DEBUG = StrToBool(cc.OPTS.get("Debug"))
    cc.EXECUTE = StrToBool(cc.OPTS.get("Execute"))
    cc.SEEK_FIRST_ERROR = StrToBool(cc.OPTS.get("Seek first error"))
    
    #compiling compiler &amp; linker error detection regexp
    cc.CPL_ERR_REGEXP = re.compile(cc.CPL.get("Error detection"),re.IGNORECASE) 
    cc.LKR_ERR_REGEXP = re.compile(cc.LKR.get("Error detection"),re.IGNORECASE)
    
    return True


</t>
<t tx="ekr.20060513122450.307">def sGetDebugInfo(self):
    
    cc = self
   
    cc.DBG = cc.sGet("Debugger")
    if cc.DBG["Debugger"]:
        self.DBG_PROMPT_REGEXP = re.compile(cc.DBG.get("Prompt pattern"))
        return True
    else:
        return Error("xcc: ","No debugger defined!")</t>
<t tx="ekr.20060513122450.308">def sGetExecInfo(self):
    
    cc = self

    cc.EXE = cc.sGet("Executable")		
    return True</t>
<t tx="ekr.20060513122450.309">def sGoToError(self,e=None):#if e==None, retreive current body line
    
    cc = self
    
    mask = [" ",":","(",")"]
    if e == None:
        row,col = cc.LeoBodyText.index("insert").split(".")
        row = int(row)
        col = int(col)
        lines = cc.SELECTED_NODE.bodyString().splitlines()
        e = lines[row-1]
        #e=e.replace("/","\\")
    
    if cc.CPL_ERR_REGEXP:
        m = cc.CPL_ERR_REGEXP.search(e)
        if m != None:
            op = ""
            try:            
                id = m.group("ID")
                op += id
            except Exception:
                pass
            try:
                file = m.group("FILE")
                op += " in "+file
            except Exception:
                pass    
            try:
                line = m.group("LINE")
                op += " line "+line                
            except Exception:
                pass            
            try:    
                edef = m.group("DEF")
                op += " : "+edef
            except Exception:
                pass    
            
            path,name = os.path.split(cc.CPL["Compiler"])
            Error(name+" : ","Error: "+op)
        
            name,ext = os.path.splitext(file)
            if name == cc.NAME:
                SeekErrorClass(cc,int(line),ext.replace(".",""),color=ErrorColor)</t>
<t tx="ekr.20060513122450.310">def sGo(self):	#this is where the selected node also become the active node

    cc = self
    
    cc.sGetBrowseInfo()
    
    if not cc.NAME:
        return Error("xcc: ","Node has no name!")

    if cc.LANG["Language"] == "":
        cc.LANG["Language"] == "c++"
        
        
    cc.sSetText("@language "+cc.LANG["Language"]+"\n")
    
    if not cc.sGetWriteInfo():
        return False
    if cc.OPTS.get("Create files") == "True":
        if cc.OPTS.get("Source files") == "True" or cc.OPTS.get("Doc files"):
            if not cc.CreateFiles():
                return False
    
    cc.sGetExecInfo()
    if cc.OPTS.get("Build") == "True":        
        if not cc.sGetCompileInfo():
            return False
        
        
        bs = cc.OPTS.get("Build sequence").splitlines() 
        for s in bs:
            if s != "":
                s = s.strip()
                if s == "COMPILE":
                    cc.COMPILE = True           
                    if cc.Compile() == "False":
                        return False
                    else:
                        continue
                if s == "LINK":
                    cc.LINK = True           
                    if cc.Link() == "False":
                        return False
                    else:
                        continue                
                if cc.RunTool(cc,s) == "False":
                        return False
            
    if cc.EXECUTE and cc.EXT != cc.HDR_EXT:
        if cc.DEBUG:
            if not cc.Debug():
                return False
        else:
            if not cc.Execute():
                return False        
    
    return True


</t>
<t tx="ekr.20060513122450.311">def sSet (self,name,value):
    
    cc = self

    cc.SELECTED_DICT [name] = value
</t>
<t tx="ekr.20060513122450.312">def sGet(self,name,init=""):
    
    cc = self
    
    if name not in cc.SELECTED_DICT:
        cc.sSet(name,init)

    return cc.SELECTED_DICT[name]</t>
<t tx="ekr.20060513122450.313">def sIsDict(self):
    
    cc = self

    if not cc.SELECTED_NODE:
        return False
    
    v = cc.SELECTED_NODE.v	
    
    return hasattr(v,"unknownAttributes") and "xcc_cfg" in v.unknownAttributes</t>
<t tx="ekr.20060513122450.314">def sGetDict(self): # Get xcc parent dict alias "xcc_cfg" in ua

    cc = self

    if not cc.SELECTED_NODE:
        return None
    
    v = cc.SELECTED_NODE.v

    if not hasattr(v,"unknownAttributes"):
        v.unknownAttributes = {}
    
    if "xcc_cfg" in v.unknownAttributes:
        return v.unknownAttributes["xcc_cfg"]
    else:
        v.unknownAttributes["xcc_cfg"] = d = {}
        return d</t>
<t tx="ekr.20060513122450.315">def sInitDict(self):
    
    cc = self
    
    Warning("xcc: ","Writing blank configuration!")
    cc.sSetText("@language c++")
    cc.Config.ClearConfig()
    cc.Config.SaveToNode()
    cc.sSet("INITED","True")



</t>
<t tx="ekr.20060513122450.316">def sSelect(self,node=None):
    
    cc = self ; c = cc.c

    if node:
        if cc.SELECTED_NODE:
            cc.Config.Hide()
        
        cc.SELECTED_NODE = node        
        cc.SELECTED_DICT = cc.sGetDict()
        
        if cc.SELECTED_NODE != cc.ACTIVE_NODE and cc.SELECTED_NODE.isMarked():
            cc.SELECTED_NODE.clearMarked()
            c.redraw()
        
        cc.sGetBrowseInfo()
        cc.sShow()
    elif cc.SELECTED_NODE:
        cc.Config.Hide()        
        cc.sHide()
        cc.SELECTED_NODE = None
        cc.SELECTED_DICT = None</t>
<t tx="ekr.20060513122450.317">def sSync(self):
    
    cc = self
    
    cc.SELECTED_DICT = cc.sGetDict()
    if cc.SELECTED_DICT:
        cc.sExtractHeadInfo()
    
    cc.CHILD_DICT = cc.cGetDict()</t>
<t tx="ekr.20060513122450.318">def sShow(self):
    
    cc = self
    
    if cc.Config.visible:
        cc.Config.Hide()        
    if cc.BreakBar.visible:
        cc.BreakBar.Hide()        
    
    
    cc.LeoBodyText.pack_forget()
    cc.LeoYBodyBar.pack_forget()
    cc.LeoXBodyBar.pack_forget()
    
    #show the toolbar
    cc.ToolBar.pack(side="top",fill="x")
    
    if cc.DocEdit.visible:
        cc.DocEdit.LoadFromNode()
        
    #show the watch pane
    if cc.Watcher.visible:
        cc.Watcher.pack(side = "bottom",fill="x")        
        cc.ToolBar.WatchButton.config(command=cc.Watcher.Hide,relief='sunken')
        #sync data to selected node
        cc.Watcher.Sync()
        
        #update watch data if running
        if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
            WatchTaskClass(cc)
            cc.DbgOut("")
        
    cc.LeoXBodyBar.pack(side="bottom",fill="x")
    cc.LeoYBodyBar.pack(side="right",fill="y")
    cc.LeoBodyText.pack(fill="both",expand=1)
    cc.LeoBodyText.config(wrap='none')
    
    cc.ToolBar.Spacer["state"] = 'normal'
    cc.ToolBar.Spacer.delete('1.0','end')
    cc.ToolBar.Spacer.insert("insert","."+cc.EXT)
    cc.ToolBar.Spacer["state"] = 'disabled'
    
    cc.ToolBar.Display["state"] = 'normal'
    cc.ToolBar.Display.delete('1.0','end')
    cc.ToolBar.Display["state"] = 'disabled'</t>
<t tx="ekr.20060513122450.319">def sHide(self):
    
    cc = self

    cc.LeoXBodyBar.pack_forget()
    cc.ToolBar.pack_forget()
    
    #set back the wrapping mode
    cc.LeoBodyText.config(wrap=cc.LeoWrap)
    
    if cc.Watcher.visible:
        cc.Watcher.Hide()
        
    if cc.DocEdit.visible:
        cc.DocEdit.Hide()</t>
<t tx="ekr.20060513122450.320">def sSetText(self,text=""):
    
    cc = self
    cc.c.setBodyString(cc.SELECTED_NODE,text)
</t>
<t tx="ekr.20060513122450.321">def sAddText(self,text):
    
    cc = self
    
    cc.c.setBodyString(cc.SELECTED_NODE,cc.SELECTED_NODE.bodyString()+text)

    if cc.CHILD_NODE == None:
        l,c = cc.LeoBodyText.index("end").split(".")
        cc.LeoBodyText.see(l+".0")</t>
<t tx="ekr.20060513122450.322"></t>
<t tx="ekr.20060513122450.323">def cIs(self,node):

    for p in node.parents_iter():
        if p.headString()[0:5] == "@xcc ":
            return True	
    return False</t>
<t tx="ekr.20060513122450.324">def cSet(self,name,value,node=None):    
    cc = self
    if node == None:
        if cc.CHILD_DICT != None:
            cc.CHILD_DICT[name] = value
    else:
        v = node.v    
        
        if not hasattr(v,"unknownAttributes"):
            v.unknownAttributes = ua = {}
        else:
            ua	=	v.unknownAttributes
    
        if "xcc_child_cfg" not in ua:
            ua["xcc_child_cfg"] = cfg = {}
        else:
            cfg = ua["xcc_child_cfg"]
            
        cfg[name] = value
        
</t>
<t tx="ekr.20060513122450.325">def cGet(self,name,init="",node=None):
    
    cc = self
    if node == None:
        cfg = cc.CHILD_DICT
    else:
        v = node.v
    
        if not hasattr(v,"unknownAttributes"):
            v.unknownAttributes = ua = {}
        else:
            ua	=	v.unknownAttributes
    
        if "xcc_child_cfg" not in ua:
            ua["xcc_child_cfg"] = cfg = {}
        else:
            cfg = ua["xcc_child_cfg"]

    if name not in cfg:
        cfg[name] = init
            
    return cfg[name]</t>
<t tx="ekr.20060513122450.326">def cSelect(self,node=None):
    
    cc = self

    if node:
        cc.Config.Hide()
        cc.CHILD_NODE = node
        cc.CHILD_DICT = cc.cGetDict()
        
        if cc.DocEdit.visible:
            cc.DocEdit.LoadFromNode()
        
        if cc.LOCATE_CHILD:
            loc = LocatorClass(cc,cc.CHILD_NODE,1)
            cc.CHILD_EXT = loc.FOUND_FILE_EXT
            cc.CHILD_LINE = loc.FOUND_FILE_LINE								
            cc.BreakBar.Show()            
            if loc.FOUND_FILE_EXT:
                cc.ToolBar.SyncDisplayToChild(loc)
            else:
                cc.ToolBar.SyncDisplayToError()
    
    elif cc.CHILD_NODE:
        cc.BreakBar.Hide()
        cc.CHILD_NODE = None
        cc.CHILD_DICT = None
        cc.CHILD_LINE = None
        cc.CHILD_EXT = None</t>
<t tx="ekr.20060513122450.327">def cGetDict(self,node=None,create=True):#Get xcc child dict alias "xcc_child_cfg" in ua	
    #the func must return the CHILD_NODE dict if node == None
    cc = self

    if node == None:
        node =	cc.CHILD_NODE
    
    v = node.v
    
    if not hasattr(v,"unknownAttributes"):
        if create != True:
            return None
        v.unknownAttributes = {}		
    
    if "xcc_child_cfg" not in v.unknownAttributes:
        if create != True:
            return None
        v.unknownAttributes["xcc_child_cfg"] = {}    
            
    return v.unknownAttributes.get("xcc_child_cfg")
</t>
<t tx="ekr.20060513122450.328"></t>
<t tx="ekr.20060513122450.329">def CreateFiles(self):

    cc = self
    #g.trace(cc.OPTS)
    
    if cc.OPTS.get("Create files") == "True":
        return WriterClass(cc).Result
    else:
        return None</t>
<t tx="ekr.20060513122450.330">def Compile(self):
    cc = self
    
    try:
        process = ProcessClass(cc,
            cc.SELECTED_NODE,
            cc.CPL.get("Compiler"),
            cc.CplCmd(),
            start=cc.CplStart,
            out=cc.CplOut,
            err=cc.CplErr,
            end=cc.CplEnd)
        
        return ProcessClass.QueueProcess(process)        
        
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.331">def CplCmd(self):
    
    cc = self
    cwd = os.getcwd()

    if cc.DEBUG:
        cmd = cc.CPL["Debug arguments"]
    else:
        cmd = cc.CPL["Arguments"]
    
    cmd = cc.ReplaceVars(cmd.replace("\n"," ").strip())
    
    @others
    
    return cmd


</t>
<t tx="ekr.20060513122450.332">s = cc.CPL.get("Include path")
if s:
    sym = s
    paths = cc.CPL.get("Include search paths",'').splitlines()
    cc.INCPATHS = ""
    for p in paths:
        if p != "":
            cc.INCPATHS += " "+sym+"\""+p+"\""
    cmd = cmd.replace("_INCPATHS_",cc.INCPATHS.strip())</t>
<t tx="ekr.20060513122450.333">s = cc.LKR.get("Library path")
if s:
    sym = s
    paths = cc.LKR.get("Library search paths",'').splitlines()
    cc.LIBPATHS = ""
    for p in paths:
        if p != "":
            cc.LIBPATHS += " "+sym+"\""+p+"\""
    cmd = cmd.replace("_LIBPATHS_",cc.LIBPATHS.strip())</t>
<t tx="ekr.20060513122450.334">s = cc.LKR.get("Use library")
if s:
    sym = s
    libs = cc.LKR.get("Used libraries",'').split()
    cc.LIBRARIES = ""
    for l in libs:
        if l != "":
            cc.LIBRARIES += " "+sym+"\""+l+"\""
    cmd = cmd.replace("_LIBRARIES_",cc.LIBRARIES.strip())</t>
<t tx="ekr.20060513122450.335">if cc.OUTEXT == "dll":
    s = cc.LKR.get("Build dll")
else:
    s = cc.LKR.get("Build exe")
    
if s: cmd = cmd.replace("_BUILD_",s)</t>
<t tx="ekr.20060513122450.336">def Debug(self):
    
    cc = self
    if cc.sGetDebugInfo() and cc.OUTEXT == cc.BIN_EXT:
        process = ProcessClass(cc,
            cc.SELECTED_NODE,
            cc.DBG.get("Debugger"),
            cc.DbgCmd(),
            start=cc.DbgStart,
            out=cc.DbgOut,
            err=cc.DbgErr,
            end=cc.DbgEnd)
            
        return ProcessClass.QueueProcess(process)
    return False</t>
<t tx="ekr.20060513122450.337">def DbgCmd(self):
    
    cc = self
    
    cmd = cc.DBG.get("Arguments").replace("\n"," ").strip()
    cmd = cc.ReplaceVars(cmd)
    
    #g.trace(repr(cmd))
    return cmd</t>
<t tx="ekr.20060513122450.338">def Execute(self):    
    #g.trace()
    
    cc = self
    
    cmd = cc.ABS_PATH+"/"+cc.NAME+"."+cc.OUTEXT
    args = cc.EXE.get("Execution arguments")
        
    if cc.OPTS.get("Connect to pipe") == "True":
        g.es("piping")
        process = ProcessClass(cc,
            cc.SELECTED_NODE,
            cmd,
            args,
            start=cc.ProgStart,
            out=cc.ProgOut,
            err=cc.ProgErr,
            end=cc.ProgEnd)
    else:
        process = ProcessClass(cc,cc.SELECTED_NODE,cmd,args,spawn=True)

    return ProcessClass.QueueProcess(process)
</t>
<t tx="ekr.20060513122450.339"></t>
<t tx="ekr.20060513122450.340">def CplStart(self):
    cc = self
    cc.OutBuff = ""
    cc.ErrBuff = ""
    cc.FIRST_ERROR = False
    cc.aSelect(cc.SELECTED_NODE)
    process = ProcessClass.List[0]    
    
    text = ""	
    if cc.VERBOSE:
        if cc.LINK == True:
            pn = "Compiling"
        else:
            pn = "Building"       
        
        text += "\" "+pn+"...  Starting "+process.FileName+"...\n"
        text += "\" using arguments: "+process.Arguments+"\n"		
    text += "\""+("="*60)+"\n"
    
    cc.aAddText(text)
</t>
<t tx="ekr.20060513122450.341">def CplOut(self,text):
    cc = self
    cc.OutBuff += text
    lines = cc.OutBuff.splitlines(True)
    
    last_char = lines[-1][-1]
    if last_char != "\n" and last_char != "\r":
        cc.OutBuff = lines.pop()
    else:
        cc.OutBuff = ""
    
    text = ""	
    for l in lines:
        if l != "":
            if cc.CPL_ERR_REGEXP:
                m = cc.CPL_ERR_REGEXP.search(l,re.IGNORECASE)
                if m != None:
                    text += cc.CMT+" "+l
                    if cc.SEEK_FIRST_ERROR and not cc.FIRST_ERROR:
                        cc.FIRST_ERROR = True
                        cc.sGoToError(l)
                else:
                    if cc.FILTER_OUTPUT != "True":
                        text += "\" "+l
            else:
                text += l
            
    cc.aAddText(text)

</t>
<t tx="ekr.20060513122450.342">def CplErr(self,text):
    cc = self    
    cc.ErrBuff += text
    lines = cc.ErrBuff.splitlines(True)
    
    if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
        cc.ErrBuff = lines.pop()
    else:
        cc.ErrBuff = ""    
    
    text = ""	
    for l in lines:
        if l != "":
            text += cc.CMT+"err: "+l
            if cc.CPL_ERR_REGEXP:
                m = cc.CPL_ERR_REGEXP.search(l,re.IGNORECASE)
                if m != None:
                    if cc.SEEK_FIRST_ERROR and not cc.FIRST_ERROR:
                        cc.FIRST_ERROR = True
                        cc.sGoToError(l)
            
    cc.aAddText(text)</t>
<t tx="ekr.20060513122450.343">def CplEnd(self,exitcode):
    
    cc = self
    text = "\""+("="*60)+"\n"
    
    if cc.LINK == True:
        pn = "Compilation"
    else:
        pn = "Build"
    
    
    if exitcode == None:
        text += "\" "+pn+" process successful!\n"
        Message("xcc : ",pn+" process successful!\n")
    else:
        text += "\" "+pn+" process aborted!\n"
        Error("xcc : ",pn+" process failed!")
    text += "\""+("-"*60)+"\n"

    cc.aAddText(text)
    cc.aSelect()</t>
<t tx="ekr.20060513122450.344"></t>
<t tx="ekr.20060513122450.345"></t>
<t tx="ekr.20060513122450.346">class DbgTaskClass:
    @others</t>
<t tx="ekr.20060513122450.347">def __init__(self,cc,cmd,index=None):
    
    self.cc = cc
    self.Command = cmd
    
    if index:
        cc.DBG_SD.insert(index,self.Send)
    else:
        cc.DBG_SD.append(self.Send)</t>
<t tx="ekr.20060513122450.348">def Send(self):
    
    cc = self.cc

    if self.Command:
        cc.aWrite(self.Command)
    cc.DBG_SD.remove(self.Send)</t>
<t tx="ekr.20060513122450.349">class OutputTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="ekr.20060513122450.350">def __init__(self,cc):

    self.cc = cc
    cc.DBG_RD.append(self.Receive)</t>
<t tx="ekr.20060513122450.351">def Send(self):
    pass	#we just receive
</t>
<t tx="ekr.20060513122450.352">def Receive(self,line):
    
    cc = self.cc
    
    if cc.DBG_PROMPT == False and line != "":
        lower = line.lower()
        if lower.find("error") &gt; -1 or lower.find("warning") &gt; -1:
            cc.aAddText(cc.CMT+line)
        else:
            if cc.OPTS["Filter output"] == "False":
                cc.aAddText("\" "+line)</t>
<t tx="ekr.20060513122450.353">class TargetPidTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="ekr.20060513122450.354">def __init__(self,cc):
    
    self.cc = cc
    cc.DBG_SD.append(self.Send)
    
    self.PidTask = cc.ReplaceVars(cc.DBG.get("Target pid task"))
    self.FindPid = cc.ReplaceVars(cc.DBG.get("Find pid"))</t>
<t tx="ekr.20060513122450.355">def Send(self):
    cc = self.cc
    if self.PidTask != "":		
        cc.aWrite(cc.ReplaceVars(self.PidTask))
        cc.DBG_SD.remove(self.Send)
        cc.DBG_RD.append(self.Receive)
    else:
        cc.DBG_SD.remove(self.Send)
        Warning("xcc: ","Target pid task is undefined!")


</t>
<t tx="ekr.20060513122450.356">def Receive(self,line):
   
    cc = self.cc
    if self.FindPid:
        if not cc.DBG_PROMPT:
            if line != "":
                m = re.search(self.FindPid,line)
                if m != None:
                    cc.TARGET_PID = int(m.group("PID"))		
                    if cc.VERBOSE:					
                        cc.aAddText("\" Target pid is: "+str(cc.TARGET_PID)+" \n")
                    cc.DBG_RD.remove(self.Receive)
                
    else:
        cc.DBG_RD.remove(self.Receive)</t>
<t tx="ekr.20060513122450.357">class BreakTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="ekr.20060513122450.358">def __init__(self,cc):
    
    self.cc = cc
    #gathering breaks
    self.Breaks = BreakFinderClass(cc).BREAKS
    if len(self.Breaks) != 0:
        self.bpsym = cc.DBG["Set break"]
        if self.bpsym == "":
            Waning("xcc: ","Set break symbol is undefined!")
        else:
            self.bpsym = cc.ReplaceVars(self.bpsym)
            cc.DBG_SD.append(self.Send)
    
    regexp = cc.DBG["Break detection"]
    if regexp != "":		
        regexp = regexp.splitlines()
        self.RegExp = []
        for e in regexp:
            self.RegExp.append(re.compile(e))		
    else:
        Warning("xcc: ","No break detection expression defined!")</t>
<t tx="ekr.20060513122450.359">def Send(self):
    cc = self.cc
    if len(self.Breaks) &gt; 0:
        extl,s = self.Breaks.popitem()
        ext,l = extl.split(":")
        bpat = self.bpsym
        bpat = bpat.replace("_FILE_",cc.NAME+"."+ext).replace("_LINE_",l)
        cc.aWrite(bpat)
    else:
        cc.DBG_SD.remove(self.Send)
        cc.DBG_RD.append(self.Receive)

</t>
<t tx="ekr.20060513122450.360">def Receive(self,line):
    
    cc = self.cc

    for r in self.RegExp:
        if r.search(line) != None:
            if cc.OPTS.get("Seek breakpoints"):
                QueryGoTaskClass(cc,0)
            if cc.VERBOSE:
                cc.aAddText("\" Break detected!\n")
            
            if cc.ACTIVE_PROCESS and cc.SELECTED_NODE == cc.ACTIVE_NODE:
                if cc.Watcher.visible:
                    WatchTaskClass(cc)               
                    if cc.DBG_PROMPT:
                        cc.DbgOut("")
                        
                if cc.Dasm.visible:
                    DasmTaskClass(cc)               
                    if cc.DBG_PROMPT:
                        cc.DbgOut("")
                         
            cc.ToolBar.EnableStep()						
            return</t>
<t tx="ekr.20060513122450.361">class RegExpTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="ekr.20060513122450.362">def __init__(self,cc):
    
    self.cc = cc
    cc.DBG_RD.append(self.Receive)
    
    self.Exps = cc.ReplaceVars(cc.DBG.get("Regular expression",'')).splitlines()
    self.Task = cc.ReplaceVars(cc.DBG.get("Task",'')).splitlines()
    self.on = False	</t>
<t tx="ekr.20060513122450.363">def Send(self):
    pass	#receive only



</t>
<t tx="ekr.20060513122450.364">def Receive(self,line):
    
    cc = self.cc

    if not self.on:
        self.on = True ; return
    i=1
    for e in self.Exps:
        if e != "" and re.search(e,line) != None:
            if len(self.Task) &gt;= i:
                t = self.Task[i-1]
            else:
                t = ""
            DbgTaskClass(cc,t,0)
            self.on = False
        i += 1</t>
<t tx="ekr.20060513122450.365">class WatchTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="ekr.20060513122450.366">def __init__(self,cc,index=0):
    
    self.cc = cc
    self.Index = index
    cc.WATCH_TASK = self
    self.Buffer = ""
    self.Count = 0
    
    cc.Watcher.OutBox.tag_delete("changed")
    self.Lines = cc.Watcher.InBox.get(1.0,'end').strip().splitlines()	
    
    if len(self.Lines) != 0:
        d=cc.DBG_SD.append(self.Send)
    
    for l in self.Lines:
        if l == "":
            del l
    
    self.nl = ""
    self.Inited = False
</t>
<t tx="ekr.20060513122450.367">def Cancel(self):
    cc = self.cc
    if self.Send in cc.DBG_SD:
        cc.DBG_SD.remove(self.Send)
    if self.Receive in cc.DBG_RD:
        cc.DBG_RD.remove(self.Receive)
    if self.OnPrompt in cc.PROMPT_RD:
        cc.PROMPT_RD.remove(self.OnPrompt)
        
    cc.Watcher.Watching = False
    cc.WATCH_TASK = None

</t>
<t tx="ekr.20060513122450.368">def Send(self):
    cc = self.cc
    if len(self.Lines) &gt; 0:
        cc.Watcher.Watching = True
        vari = self.Lines.pop(0)
        if vari.startswith("@"):
            vari = vari[1:]
        else:
            vari = vari = cc.DBG["Evaluate"]+vari
        cc.aWrite(vari)
        cc.DBG_SD.remove(self.Send)
        cc.DBG_RD.append(self.Receive)
        cc.PROMPT_RD.append(self.OnPrompt)
        self.Buffer = ""
        self.Count += 1</t>
<t tx="ekr.20060513122450.369">def Receive(self,line):
    cc = self.cc
    if cc.DBG_PROMPT == False:		
        self.Buffer += line</t>
<t tx="ekr.20060513122450.370">def OnPrompt(self):
    cc = self.cc
    
    cc.Watcher.OutBox["state"] = 'normal'
    s = str(self.Count)+".0"
    e = str(self.Count)+".end"
    
    self.Buffer = self.Buffer.replace("\n"," ")
    
    if self.Buffer != cc.Watcher.OutBox.get(s,e):
        changed = True
    else:
        changed = False
    
    cc.Watcher.OutBox.delete(s,e+"+1c")
    cc.Watcher.OutBox.insert(s,self.Buffer+"\n")	
    
    if changed == True:
        cc.Watcher.OutBox.tag_add("changed",s,e)
        cc.Watcher.OutBox.tag_config("changed",foreground ="red")
    
    cc.Watcher.OutBox["state"] = 'disabled'
        
    if len(self.Lines) != 0:
        cc.DBG_SD.append(self.Send)		
    else:
        cc.Watcher.Watching = False
        cc.WATCH_TASK = None
    
    cc.PROMPT_RD.remove(self.OnPrompt)	
    cc.DBG_RD.remove(self.Receive)

</t>
<t tx="ekr.20060513122450.371">class QueryGoTaskClass(DbgTaskClass):

    @others
    </t>
<t tx="ekr.20060513122450.372">def __init__(self,cc,index=None):
    
    self.cc = cc
    self.Query = cc.DBG.get("Query location")
    self.Find = cc.ReplaceVars(cc.DBG.get("Find location"))
    if not self.Query:
        cc.DBG_TASK.remove(self)
        Warning("xcc: ","Query location task is undefined!")
    elif index:
        cc.DBG_SD.insert(index,self.Send)
    else:
        cc.DBG_SD.append(self.Send)</t>
<t tx="ekr.20060513122450.373">def Send(self):
    
    cc = self.cc
    cc.aWrite(self.Query)
    cc.DBG_SD.remove(self.Send)
    cc.DBG_RD.append(self.Receive)</t>
<t tx="ekr.20060513122450.374">def Receive(self,line):

    cc = self.cc
    if cc.DBG_PROMPT == False:
        if line != "":
            m = re.search(self.Find,line,re.IGNORECASE)
            if m != None:
                bline = m.group("LINE")
                bext = m.group("EXT")
                    
                if bline and bext:
                    if cc.VERBOSE:					
                        cc.aAddText("\" Current location is: "+bline+" in "+bext+" file!\n")
                    bline = int(bline)	
                    SeekErrorClass(self.cc,bline,bext,color=BreakColor)
                
                cc.DBG_RD.remove(self.Receive)
                
                if cc.Watcher.visible and cc.ACTIVE_PROCESS:
                    if cc.SELECTED_NODE == cc.ACTIVE_NODE:
                        WatchTaskClass(cc)
                    if cc.DBG_PROMPT:
                        cc.DbgOut("")
    else:
        cc.DBG_RD.remove(self.Receive)
            
</t>
<t tx="ekr.20060513122450.375">class BreakIdTaskClass(DbgTaskClass):
    @others
    </t>
<t tx="ekr.20060513122450.376">def __init__(self,cc,b,index=0):
    
    self.cc = cc
    
    if len(b) &gt;0:
        self.Break = b
        self.ListBreaks = cc.DBG["List breaks"]
        self.IdentifyBreak = cc.ReplaceVars(cc.DBG["Identify break"])
        
        if self.ListBreaks and self.IdentifyBreak:
            if index:
                cc.DBG_SD.insert(index,self.Send)
            else:
                cc.DBG_SD.append(self.Send)
        else:
            Warning("xcc: ","Break Identification task is undefined!")</t>
<t tx="ekr.20060513122450.377">def Send(self):
    cc = self.cc
    cc.aWrite(self.ListBreaks)
    cc.DBG_SD.remove(self.Send)
    cc.DBG_RD.append(self.Receive)

</t>
<t tx="ekr.20060513122450.378">def Receive(self,line):
    
    cc = self.cc
    if not cc.DBG_PROMPT:
        if line:
            idb = cc.ReplaceVars(self.IdentifyBreak)
                        
            idb = idb.replace("_FILE_",self.Break[0]).replace("_LINE_",self.Break[1])
            m = re.search(idb,line,re.IGNORECASE)
            if m != None:
                bid = m.group("ID")					
                if bid != None:
                    if cc.VERBOSE:					
                        cc.aAddText("\" Break id at line "+self.Break[1]+" in "+self.Break[0]+" is "+bid+"\n")
                    DbgTaskClass(cc,cc.ReplaceVars(cc.DBG["Clear break"]).replace("_ID_",bid))
                    
    else:
        cc.DBG_RD.remove(self.Receive)
            </t>
<t tx="ekr.20060513122450.379">def DbgStart(self):

    #g.trace()
    cc = self
    cc.OutBuff = ""
    cc.ErrBuff = ""
    cc.ACTIVE_PROCESS = ProcessClass.List[0]
    cc.PROMPT_RD = []
    cc.DBG_STEPPING = False
    cc.DBG_PROMPT = False
    cc.TARGET_PID = ""
    cc.EOL = cc.DBG.get("Pipe eol")
    cc.aSelect(cc.SELECTED_NODE)
    # set buttons
    cc.ToolBar.PauseButton["state"] = 'normal'
    cc.ToolBar.StopButton["state"] = 'normal'
    # startup banner
    text = ""	
    if cc.VERBOSE:
        text += "\" Starting "+cc.ACTIVE_PROCESS.FileName+"...\n"
        text += "\" using arguments: "+cc.ACTIVE_PROCESS.Arguments+"\n"
    text += "\""+("="*60)+"\n"
    cc.aAddText(text)
    cc.DBG_TASK = []
    cc.DBG_SD = []
    cc.DBG_RD = []
    OutputTaskClass(cc)
    st = cc.ReplaceVars(cc.DBG["Startup task"]).splitlines()
    for t in st:
        DbgTaskClass(cc,t)
    TargetPidTaskClass(cc)
    RegExpTaskClass(cc)
    
    BreakTaskClass(cc)
    DbgTaskClass(cc,cc.DBG["Continue"])</t>
<t tx="ekr.20060513122450.380">def DbgOut(self,text):
    
    #g.trace(repr(text))
    
    cc = self
   
    #Extract output lines and prompt
    if text:
        cc.OutBuff += text
        lines = cc.OutBuff.splitlines(True)
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.OutBuff = lines.pop()
        else:
            cc.OutBuff = ""

        # sending output to SENT tasks
        for l in lines:
            for r in cc.DBG_RD:
                r(l)
            if cc.DBG_PROMPT_REGEXP and cc.DBG_PROMPT_REGEXP.search(l):
                cc.DBG_PROMPT = True            
            		
    
    if not cc.DBG_PROMPT:
        if cc.DBG_PROMPT_REGEXP and cc.DBG_PROMPT_REGEXP.search(cc.OutBuff):
            cc.DBG_PROMPT = True
    
    # detect the prompt
    if cc.DBG_PROMPT:
        cc.ToolBar.PauseButton["state"] = 'disabled'
        for prd in cc.PROMPT_RD:
            prd()
        if cc.DBG_STEPPING:
            cc.DBG_STEPPING = False
            cc.ToolBar.EnableStep()
        if not cc.FILTER_OUTPUT and cc.OutBuff != "":
            cc.aAddText("\" "+cc.OutBuff)
        cc.OutBuff = ""

    # send task to the debugger
    while cc.DBG_PROMPT and len(cc.DBG_SD) &gt; 0:
        cc.DBG_SD[0]()
    
    if cc.DBG_PROMPT:
        cc.ToolBar.ShowInput()</t>
<t tx="ekr.20060513122450.381">def DbgErr(self,text):
    
    #g.trace(repr(text))
    
    cc = self
    cc.ErrBuff += text
    lines = cc.ErrBuff.splitlines(True)
    if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
        cc.ErrBuff = lines.pop()
    else:
        cc.ErrBuff = ""
    
    text = ""	
    for l in lines:
        text += "//err: "+l
                    
    cc.aAddText(text)</t>
<t tx="ekr.20060513122450.382">def DbgEnd(self,exitcode):

    cc = self
    text = "\""+("="*60)+"\n"
    if exitcode == None:
        text += "\" Debug session ended successfully!\n"
    else:
        text += self.CMT+" Debug session aborted!\n"
    
    text += "\""+("-"*60)+"\n"

    cc.aAddText(text)
    cc.ToolBar.PauseButton["state"] = 'disabled'
    cc.ToolBar.StopButton["state"] = 'disabled'
    cc.ACTIVE_PROCESS = None
    cc.DBG_TASK = []
    cc.ToolBar.DisableStep()
    cc.LeoBodyText.tag_delete("xcc_error")	
    cc.TARGET_PID = ""
    cc.aSelect()
</t>
<t tx="ekr.20060513122450.383"></t>
<t tx="ekr.20060513122450.384">def ProgStart(self):
    
    #g.trace()

    cc = self
    cc.OutBuff = ""
    cc.ErrBuff = ""
    cc.aSelect(cc.SELECTED_NODE)
    cc.ACTIVE_PROCESS = ProcessClass.List[0]
    cc.EOL = cc.EXE.get("Pipe eol")

    text = ""	
    if cc.VERBOSE:
        text += "\" Starting "+cc.ACTIVE_PROCESS.FileName+"...\n"
        text += "\" using arguments: "+cc.ACTIVE_PROCESS.Arguments+"\n"		
    text += "\""+("="*60)+"\n"
    cc.aAddText(text)
    
    cc.ToolBar.ShowInput()</t>
<t tx="ekr.20060513122450.385">def ProgOut(self,text):
    
    #g.trace(repr(text))
    g.es(text)
    cc = self
    cc.OutBuff += text
    lines = cc.OutBuff.splitlines(True)
    if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
        cc.OutBuff = lines.pop()
    else:
        cc.OutBuff = ""
    
    text = ""	
    for l in lines:
        if l != "":
            text += "# "+l
    
    text += "# "+cc.OutBuff
    cc.OutBuff = ""
    cc.aAddText(text)</t>
<t tx="ekr.20060513122450.386">def ProgErr(self,text):
    
    #g.trace(repr(text))
    
    cc = self
    
    cc.ErrBuff += text
    lines = cc.ErrBuff.splitlines(True)
    if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
        cc.ErrBuff = lines.pop()
    else:
        cc.ErrBuff = ""
    
    text = ""	
    for l in lines:
        text += "// "+l+"\n"
    text += "# "+cc.ErrBuff
    cc.ErrBuff = ""
    cc.aAddText(text)</t>
<t tx="ekr.20060513122450.387">def ProgEnd(self,exitcode):
    
    cc = self
    cc.ToolBar.HideInput()
    text = "\n\""+("="*60)+"\n"
    if exitcode == None:
        text += "\" "+cc.ACTIVE_PROCESS.FileName+" exited normally!\n"
    else:
        text += "// "+cc.ACTIVE_PROCESS.FileName+" exited with code: "+str(exitcode)+"\n"		
    text += "\""+("-"*60)+"\n"

    cc.aAddText(text)
    cc.ACTIVE_PROCESS = None
    cc.aSelect()</t>
<t tx="ekr.20060513122450.389">def GetXccNode(node):

	for p in node.parents_iter():
		h = p.headString()
		if (h[0:5] == "@xcc "):
			return p
	
	return None
</t>
<t tx="ekr.20060513122450.390">def IsXcc(node):

	if node.headString()[0:5] == "@xcc ":
		return True
	else:
		return False
</t>
<t tx="ekr.20060513122450.392">def UpdateProcess(self):
    
    #g.trace(ProcessClass.List)
    
    cc = self
    if len(ProcessClass.List) &gt; 0:
        process = ProcessClass.List[0]
        if process.Update():
            #g.es("update")
            return
        if process.Close():
            ProcessClass.List = [] #reset
        else:
            ProcessClass.List.pop(0)
            if ProcessClass.List:
                if not ProcessClass.List[0].Open():
                    ProcessClass.List = [] #reset</t>
<t tx="ekr.20060513122450.394">def ImportFiles():

	Warning("TODO: ","Add import code in ImportFiles function!")</t>
<t tx="ekr.20060513122450.395"></t>
<t tx="ekr.20060513122450.396">if 0:
    def OnStart2(tag,keywords):
        try:
            if XCC_INITED == False:
                c = keywords.get("c")
                InitXcc(c)
                n = c.currentPosition()
                h = n.headString()	
                
        except Exception,e:
            TraceBack()</t>
<t tx="ekr.20060513122450.397">def OnCreate(tag,keywords):
    try:
        c = keywords.get("c")
        if c:
            controllers [c] = controllerClass(c)
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.398">def OnSelect2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onSelect()
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.399">def OnIdle(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onIdle()
    except Exception:
        g.disableIdleTimeHook()
        g.es_exception()</t>
<t tx="ekr.20060513122450.400">def OnCommand2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onCommand2(keywords)
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.401">def OnBodyDoubleClick(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onBodyDoubleClick()
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.402">def OnBodyKey2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onBodyKey2(keywords)
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122450.403">def OnHeadKey2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onHeadKey2(keywords)
    except Exception:
        TraceBack()</t>
<t tx="ekr.20060513122450.404">def OnQuit(tag,keywords):
    try:
        global controllers
        for key in controllers.keys():
            cc = controllers.get(key)
            cc.onQuit()
    except Exception:
        g.es_exception()</t>
<t tx="ekr.20060513122613"></t>
<t tx="ekr.20060513122613.1">@
opengl.h is just a test for long files
cltest\testprog is an xcc project to test functionality under win32 compile env, with it's gcc equivalent underneath.

no plugin conflicts detected with core plugins, read-only nodes, unl or linecol plugin.
should work with most plugins...
</t>
<t tx="ekr.20060513122613.2">@language c++

</t>
<t tx="ekr.20060513122613.3">#ifndef USE_OPENGL
	#define USE_OPENGL 1
#endif</t>
<t tx="ekr.20060513122613.4">#ifdef GL_DEFS
typedef unsigned int GLenum;
typedef unsigned char GLboolean;
typedef unsigned int GLbitfield;
typedef signed char GLbyte;
typedef short GLshort;
typedef int GLint;
typedef int GLsizei;
typedef unsigned char GLubyte;
typedef unsigned short GLushort;
typedef unsigned int GLuint;
typedef float GLfloat;
typedef float GLclampf;
typedef double GLdouble;
typedef double GLclampd;
typedef void GLvoid;
typedef unsigned int GLintptr;
typedef unsigned int GLsizeiptr;
#endif</t>
<t tx="ekr.20060513122613.5">#if USE_OPENGL &gt;= 1
	@others
#endif</t>
<t tx="ekr.20060513122613.6">#ifdef GL_DEFS
#define GL_VERSION_1_1                    1
#define GL_ACCUM                          0x0100
#define GL_LOAD                           0x0101
#define GL_RETURN                         0x0102
#define GL_MULT                           0x0103
#define GL_ADD                            0x0104
#define GL_NEVER                          0x0200
#define GL_LESS                           0x0201
#define GL_EQUAL                          0x0202
#define GL_LEQUAL                         0x0203
#define GL_GREATER                        0x0204
#define GL_NOTEQUAL                       0x0205
#define GL_GEQUAL                         0x0206
#define GL_ALWAYS                         0x0207
#define GL_CURRENT_BIT                    0x00000001
#define GL_POINT_BIT                      0x00000002
#define GL_LINE_BIT                       0x00000004
#define GL_POLYGON_BIT                    0x00000008
#define GL_POLYGON_STIPPLE_BIT            0x00000010
#define GL_PIXEL_MODE_BIT                 0x00000020
#define GL_LIGHTING_BIT                   0x00000040
#define GL_FOG_BIT                        0x00000080
#define GL_DEPTH_BUFFER_BIT               0x00000100
#define GL_ACCUM_BUFFER_BIT               0x00000200
#define GL_STENCIL_BUFFER_BIT             0x00000400
#define GL_VIEWPORT_BIT                   0x00000800
#define GL_TRANSFORM_BIT                  0x00001000
#define GL_ENABLE_BIT                     0x00002000
#define GL_COLOR_BUFFER_BIT               0x00004000
#define GL_HINT_BIT                       0x00008000
#define GL_EVAL_BIT                       0x00010000
#define GL_LIST_BIT                       0x00020000
#define GL_TEXTURE_BIT                    0x00040000
#define GL_SCISSOR_BIT                    0x00080000
#define GL_ALL_ATTRIB_BITS                0x000fffff
#define GL_POINTS                         0x0000
#define GL_LINES                          0x0001
#define GL_LINE_LOOP                      0x0002
#define GL_LINE_STRIP                     0x0003
#define GL_TRIANGLES                      0x0004
#define GL_TRIANGLE_STRIP                 0x0005
#define GL_TRIANGLE_FAN                   0x0006
#define GL_QUADS                          0x0007
#define GL_QUAD_STRIP                     0x0008
#define GL_POLYGON                        0x0009
#define GL_ZERO                           0
#define GL_ONE                            1
#define GL_SRC_COLOR                      0x0300
#define GL_ONE_MINUS_SRC_COLOR            0x0301
#define GL_SRC_ALPHA                      0x0302
#define GL_ONE_MINUS_SRC_ALPHA            0x0303
#define GL_DST_ALPHA                      0x0304
#define GL_ONE_MINUS_DST_ALPHA            0x0305
#define GL_DST_COLOR                      0x0306
#define GL_ONE_MINUS_DST_COLOR            0x0307
#define GL_SRC_ALPHA_SATURATE             0x0308
#define GL_TRUE                           1
#define GL_FALSE                          0
#define GL_CLIP_PLANE0                    0x3000
#define GL_CLIP_PLANE1                    0x3001
#define GL_CLIP_PLANE2                    0x3002
#define GL_CLIP_PLANE3                    0x3003
#define GL_CLIP_PLANE4                    0x3004
#define GL_CLIP_PLANE5                    0x3005
#define GL_BYTE                           0x1400
#define GL_UNSIGNED_BYTE                  0x1401
#define GL_SHORT                          0x1402
#define GL_UNSIGNED_SHORT                 0x1403
#define GL_INT                            0x1404
#define GL_UNSIGNED_INT                   0x1405
#define GL_FLOAT                          0x1406
#define GL_2_BYTES                        0x1407
#define GL_3_BYTES                        0x1408
#define GL_4_BYTES                        0x1409
#define GL_DOUBLE                         0x140A
#define GL_NONE                           0
#define GL_FRONT_LEFT                     0x0400
#define GL_FRONT_RIGHT                    0x0401
#define GL_BACK_LEFT                      0x0402
#define GL_BACK_RIGHT                     0x0403
#define GL_FRONT                          0x0404
#define GL_BACK                           0x0405
#define GL_LEFT                           0x0406
#define GL_RIGHT                          0x0407
#define GL_FRONT_AND_BACK                 0x0408
#define GL_AUX0                           0x0409
#define GL_AUX1                           0x040A
#define GL_AUX2                           0x040B
#define GL_AUX3                           0x040C
#define GL_NO_ERROR                       0
#define GL_INVALID_ENUM                   0x0500
#define GL_INVALID_VALUE                  0x0501
#define GL_INVALID_OPERATION              0x0502
#define GL_STACK_OVERFLOW                 0x0503
#define GL_STACK_UNDERFLOW                0x0504
#define GL_OUT_OF_MEMORY                  0x0505
#define GL_2D                             0x0600
#define GL_3D                             0x0601
#define GL_3D_COLOR                       0x0602
#define GL_3D_COLOR_TEXTURE               0x0603
#define GL_4D_COLOR_TEXTURE               0x0604
#define GL_PASS_THROUGH_TOKEN             0x0700
#define GL_POINT_TOKEN                    0x0701
#define GL_LINE_TOKEN                     0x0702
#define GL_POLYGON_TOKEN                  0x0703
#define GL_BITMAP_TOKEN                   0x0704
#define GL_DRAW_PIXEL_TOKEN               0x0705
#define GL_COPY_PIXEL_TOKEN               0x0706
#define GL_LINE_RESET_TOKEN               0x0707
#define GL_EXP                            0x0800
#define GL_EXP2                           0x0801
#define GL_CW                             0x0900
#define GL_CCW                            0x0901
#define GL_COEFF                          0x0A00
#define GL_ORDER                          0x0A01
#define GL_DOMAIN                         0x0A02
#define GL_CURRENT_COLOR                  0x0B00
#define GL_CURRENT_INDEX                  0x0B01
#define GL_CURRENT_NORMAL                 0x0B02
#define GL_CURRENT_TEXTURE_COORDS         0x0B03
#define GL_CURRENT_RASTER_COLOR           0x0B04
#define GL_CURRENT_RASTER_INDEX           0x0B05
#define GL_CURRENT_RASTER_TEXTURE_COORDS  0x0B06
#define GL_CURRENT_RASTER_POSITION        0x0B07
#define GL_CURRENT_RASTER_POSITION_VALID  0x0B08
#define GL_CURRENT_RASTER_DISTANCE        0x0B09
#define GL_POINT_SMOOTH                   0x0B10
#define GL_POINT_SIZE                     0x0B11
#define GL_POINT_SIZE_RANGE               0x0B12
#define GL_POINT_SIZE_GRANULARITY         0x0B13
#define GL_LINE_SMOOTH                    0x0B20
#define GL_LINE_WIDTH                     0x0B21
#define GL_LINE_WIDTH_RANGE               0x0B22
#define GL_LINE_WIDTH_GRANULARITY         0x0B23
#define GL_LINE_STIPPLE                   0x0B24
#define GL_LINE_STIPPLE_PATTERN           0x0B25
#define GL_LINE_STIPPLE_REPEAT            0x0B26
#define GL_LIST_MODE                      0x0B30
#define GL_MAX_LIST_NESTING               0x0B31
#define GL_LIST_BASE                      0x0B32
#define GL_LIST_INDEX                     0x0B33
#define GL_POLYGON_MODE                   0x0B40
#define GL_POLYGON_SMOOTH                 0x0B41
#define GL_POLYGON_STIPPLE                0x0B42
#define GL_EDGE_FLAG                      0x0B43
#define GL_CULL_FACE                      0x0B44
#define GL_CULL_FACE_MODE                 0x0B45
#define GL_FRONT_FACE                     0x0B46
#define GL_LIGHTING                       0x0B50
#define GL_LIGHT_MODEL_LOCAL_VIEWER       0x0B51
#define GL_LIGHT_MODEL_TWO_SIDE           0x0B52
#define GL_LIGHT_MODEL_AMBIENT            0x0B53
#define GL_SHADE_MODEL                    0x0B54
#define GL_COLOR_MATERIAL_FACE            0x0B55
#define GL_COLOR_MATERIAL_PARAMETER       0x0B56
#define GL_COLOR_MATERIAL                 0x0B57
#define GL_FOG                            0x0B60
#define GL_FOG_INDEX                      0x0B61
#define GL_FOG_DENSITY                    0x0B62
#define GL_FOG_START                      0x0B63
#define GL_FOG_END                        0x0B64
#define GL_FOG_MODE                       0x0B65
#define GL_FOG_COLOR                      0x0B66
#define GL_DEPTH_RANGE                    0x0B70
#define GL_DEPTH_TEST                     0x0B71
#define GL_DEPTH_WRITEMASK                0x0B72
#define GL_DEPTH_CLEAR_VALUE              0x0B73
#define GL_DEPTH_FUNC                     0x0B74
#define GL_ACCUM_CLEAR_VALUE              0x0B80
#define GL_STENCIL_TEST                   0x0B90
#define GL_STENCIL_CLEAR_VALUE            0x0B91
#define GL_STENCIL_FUNC                   0x0B92
#define GL_STENCIL_VALUE_MASK             0x0B93
#define GL_STENCIL_FAIL                   0x0B94
#define GL_STENCIL_PASS_DEPTH_FAIL        0x0B95
#define GL_STENCIL_PASS_DEPTH_PASS        0x0B96
#define GL_STENCIL_REF                    0x0B97
#define GL_STENCIL_WRITEMASK              0x0B98
#define GL_MATRIX_MODE                    0x0BA0
#define GL_NORMALIZE                      0x0BA1
#define GL_VIEWPORT                       0x0BA2
#define GL_MODELVIEW_STACK_DEPTH          0x0BA3
#define GL_PROJECTION_STACK_DEPTH         0x0BA4
#define GL_TEXTURE_STACK_DEPTH            0x0BA5
#define GL_MODELVIEW_MATRIX               0x0BA6
#define GL_PROJECTION_MATRIX              0x0BA7
#define GL_TEXTURE_MATRIX                 0x0BA8
#define GL_ATTRIB_STACK_DEPTH             0x0BB0
#define GL_CLIENT_ATTRIB_STACK_DEPTH      0x0BB1
#define GL_ALPHA_TEST                     0x0BC0
#define GL_ALPHA_TEST_FUNC                0x0BC1
#define GL_ALPHA_TEST_REF                 0x0BC2
#define GL_DITHER                         0x0BD0
#define GL_BLEND_DST                      0x0BE0
#define GL_BLEND_SRC                      0x0BE1
#define GL_BLEND                          0x0BE2
#define GL_LOGIC_OP_MODE                  0x0BF0
#define GL_INDEX_LOGIC_OP                 0x0BF1
#define GL_COLOR_LOGIC_OP                 0x0BF2
#define GL_AUX_BUFFERS                    0x0C00
#define GL_DRAW_BUFFER                    0x0C01
#define GL_READ_BUFFER                    0x0C02
#define GL_SCISSOR_BOX                    0x0C10
#define GL_SCISSOR_TEST                   0x0C11
#define GL_INDEX_CLEAR_VALUE              0x0C20
#define GL_INDEX_WRITEMASK                0x0C21
#define GL_COLOR_CLEAR_VALUE              0x0C22
#define GL_COLOR_WRITEMASK                0x0C23
#define GL_INDEX_MODE                     0x0C30
#define GL_RGBA_MODE                      0x0C31
#define GL_DOUBLEBUFFER                   0x0C32
#define GL_STEREO                         0x0C33
#define GL_RENDER_MODE                    0x0C40
#define GL_PERSPECTIVE_CORRECTION_HINT    0x0C50
#define GL_POINT_SMOOTH_HINT              0x0C51
#define GL_LINE_SMOOTH_HINT               0x0C52
#define GL_POLYGON_SMOOTH_HINT            0x0C53
#define GL_FOG_HINT                       0x0C54
#define GL_TEXTURE_GEN_S                  0x0C60
#define GL_TEXTURE_GEN_T                  0x0C61
#define GL_TEXTURE_GEN_R                  0x0C62
#define GL_TEXTURE_GEN_Q                  0x0C63
#define GL_PIXEL_MAP_I_TO_I               0x0C70
#define GL_PIXEL_MAP_S_TO_S               0x0C71
#define GL_PIXEL_MAP_I_TO_R               0x0C72
#define GL_PIXEL_MAP_I_TO_G               0x0C73
#define GL_PIXEL_MAP_I_TO_B               0x0C74
#define GL_PIXEL_MAP_I_TO_A               0x0C75
#define GL_PIXEL_MAP_R_TO_R               0x0C76
#define GL_PIXEL_MAP_G_TO_G               0x0C77
#define GL_PIXEL_MAP_B_TO_B               0x0C78
#define GL_PIXEL_MAP_A_TO_A               0x0C79
#define GL_PIXEL_MAP_I_TO_I_SIZE          0x0CB0
#define GL_PIXEL_MAP_S_TO_S_SIZE          0x0CB1
#define GL_PIXEL_MAP_I_TO_R_SIZE          0x0CB2
#define GL_PIXEL_MAP_I_TO_G_SIZE          0x0CB3
#define GL_PIXEL_MAP_I_TO_B_SIZE          0x0CB4
#define GL_PIXEL_MAP_I_TO_A_SIZE          0x0CB5
#define GL_PIXEL_MAP_R_TO_R_SIZE          0x0CB6
#define GL_PIXEL_MAP_G_TO_G_SIZE          0x0CB7
#define GL_PIXEL_MAP_B_TO_B_SIZE          0x0CB8
#define GL_PIXEL_MAP_A_TO_A_SIZE          0x0CB9
#define GL_UNPACK_SWAP_BYTES              0x0CF0
#define GL_UNPACK_LSB_FIRST               0x0CF1
#define GL_UNPACK_ROW_LENGTH              0x0CF2
#define GL_UNPACK_SKIP_ROWS               0x0CF3
#define GL_UNPACK_SKIP_PIXELS             0x0CF4
#define GL_UNPACK_ALIGNMENT               0x0CF5
#define GL_PACK_SWAP_BYTES                0x0D00
#define GL_PACK_LSB_FIRST                 0x0D01
#define GL_PACK_ROW_LENGTH                0x0D02
#define GL_PACK_SKIP_ROWS                 0x0D03
#define GL_PACK_SKIP_PIXELS               0x0D04
#define GL_PACK_ALIGNMENT                 0x0D05
#define GL_MAP_COLOR                      0x0D10
#define GL_MAP_STENCIL                    0x0D11
#define GL_INDEX_SHIFT                    0x0D12
#define GL_INDEX_OFFSET                   0x0D13
#define GL_RED_SCALE                      0x0D14
#define GL_RED_BIAS                       0x0D15
#define GL_ZOOM_X                         0x0D16
#define GL_ZOOM_Y                         0x0D17
#define GL_GREEN_SCALE                    0x0D18
#define GL_GREEN_BIAS                     0x0D19
#define GL_BLUE_SCALE                     0x0D1A
#define GL_BLUE_BIAS                      0x0D1B
#define GL_ALPHA_SCALE                    0x0D1C
#define GL_ALPHA_BIAS                     0x0D1D
#define GL_DEPTH_SCALE                    0x0D1E
#define GL_DEPTH_BIAS                     0x0D1F
#define GL_MAX_EVAL_ORDER                 0x0D30
#define GL_MAX_LIGHTS                     0x0D31
#define GL_MAX_CLIP_PLANES                0x0D32
#define GL_MAX_TEXTURE_SIZE               0x0D33
#define GL_MAX_PIXEL_MAP_TABLE            0x0D34
#define GL_MAX_ATTRIB_STACK_DEPTH         0x0D35
#define GL_MAX_MODELVIEW_STACK_DEPTH      0x0D36
#define GL_MAX_NAME_STACK_DEPTH           0x0D37
#define GL_MAX_PROJECTION_STACK_DEPTH     0x0D38
#define GL_MAX_TEXTURE_STACK_DEPTH        0x0D39
#define GL_MAX_VIEWPORT_DIMS              0x0D3A
#define GL_MAX_CLIENT_ATTRIB_STACK_DEPTH  0x0D3B
#define GL_SUBPIXEL_BITS                  0x0D50
#define GL_INDEX_BITS                     0x0D51
#define GL_RED_BITS                       0x0D52
#define GL_GREEN_BITS                     0x0D53
#define GL_BLUE_BITS                      0x0D54
#define GL_ALPHA_BITS                     0x0D55
#define GL_DEPTH_BITS                     0x0D56
#define GL_STENCIL_BITS                   0x0D57
#define GL_ACCUM_RED_BITS                 0x0D58
#define GL_ACCUM_GREEN_BITS               0x0D59
#define GL_ACCUM_BLUE_BITS                0x0D5A
#define GL_ACCUM_ALPHA_BITS               0x0D5B
#define GL_NAME_STACK_DEPTH               0x0D70
#define GL_AUTO_NORMAL                    0x0D80
#define GL_MAP1_COLOR_4                   0x0D90
#define GL_MAP1_INDEX                     0x0D91
#define GL_MAP1_NORMAL                    0x0D92
#define GL_MAP1_TEXTURE_COORD_1           0x0D93
#define GL_MAP1_TEXTURE_COORD_2           0x0D94
#define GL_MAP1_TEXTURE_COORD_3           0x0D95
#define GL_MAP1_TEXTURE_COORD_4           0x0D96
#define GL_MAP1_VERTEX_3                  0x0D97
#define GL_MAP1_VERTEX_4                  0x0D98
#define GL_MAP2_COLOR_4                   0x0DB0
#define GL_MAP2_INDEX                     0x0DB1
#define GL_MAP2_NORMAL                    0x0DB2
#define GL_MAP2_TEXTURE_COORD_1           0x0DB3
#define GL_MAP2_TEXTURE_COORD_2           0x0DB4
#define GL_MAP2_TEXTURE_COORD_3           0x0DB5
#define GL_MAP2_TEXTURE_COORD_4           0x0DB6
#define GL_MAP2_VERTEX_3                  0x0DB7
#define GL_MAP2_VERTEX_4                  0x0DB8
#define GL_MAP1_GRID_DOMAIN               0x0DD0
#define GL_MAP1_GRID_SEGMENTS             0x0DD1
#define GL_MAP2_GRID_DOMAIN               0x0DD2
#define GL_MAP2_GRID_SEGMENTS             0x0DD3
#define GL_TEXTURE_1D                     0x0DE0
#define GL_TEXTURE_2D                     0x0DE1
#define GL_FEEDBACK_BUFFER_POINTER        0x0DF0
#define GL_FEEDBACK_BUFFER_SIZE           0x0DF1
#define GL_FEEDBACK_BUFFER_TYPE           0x0DF2
#define GL_SELECTION_BUFFER_POINTER       0x0DF3
#define GL_SELECTION_BUFFER_SIZE          0x0DF4
#define GL_TEXTURE_WIDTH                  0x1000
#define GL_TEXTURE_HEIGHT                 0x1001
#define GL_TEXTURE_INTERNAL_FORMAT        0x1003
#define GL_TEXTURE_BORDER_COLOR           0x1004
#define GL_TEXTURE_BORDER                 0x1005
#define GL_DONT_CARE                      0x1100
#define GL_FASTEST                        0x1101
#define GL_NICEST                         0x1102
#define GL_LIGHT0                         0x4000
#define GL_LIGHT1                         0x4001
#define GL_LIGHT2                         0x4002
#define GL_LIGHT3                         0x4003
#define GL_LIGHT4                         0x4004
#define GL_LIGHT5                         0x4005
#define GL_LIGHT6                         0x4006
#define GL_LIGHT7                         0x4007
#define GL_AMBIENT                        0x1200
#define GL_DIFFUSE                        0x1201
#define GL_SPECULAR                       0x1202
#define GL_POSITION                       0x1203
#define GL_SPOT_DIRECTION                 0x1204
#define GL_SPOT_EXPONENT                  0x1205
#define GL_SPOT_CUTOFF                    0x1206
#define GL_CONSTANT_ATTENUATION           0x1207
#define GL_LINEAR_ATTENUATION             0x1208
#define GL_QUADRATIC_ATTENUATION          0x1209
#define GL_COMPILE                        0x1300
#define GL_COMPILE_AND_EXECUTE            0x1301
#define GL_CLEAR                          0x1500
#define GL_AND                            0x1501
#define GL_AND_REVERSE                    0x1502
#define GL_COPY                           0x1503
#define GL_AND_INVERTED                   0x1504
#define GL_NOOP                           0x1505
#define GL_XOR                            0x1506
#define GL_OR                             0x1507
#define GL_NOR                            0x1508
#define GL_EQUIV                          0x1509
#define GL_INVERT                         0x150A
#define GL_OR_REVERSE                     0x150B
#define GL_COPY_INVERTED                  0x150C
#define GL_OR_INVERTED                    0x150D
#define GL_NAND                           0x150E
#define GL_SET                            0x150F
#define GL_EMISSION                       0x1600
#define GL_SHININESS                      0x1601
#define GL_AMBIENT_AND_DIFFUSE            0x1602
#define GL_COLOR_INDEXES                  0x1603
#define GL_MODELVIEW                      0x1700
#define GL_PROJECTION                     0x1701
#define GL_TEXTURE                        0x1702
#define GL_COLOR                          0x1800
#define GL_DEPTH                          0x1801
#define GL_STENCIL                        0x1802
#define GL_COLOR_INDEX                    0x1900
#define GL_STENCIL_INDEX                  0x1901
#define GL_DEPTH_COMPONENT                0x1902
#define GL_RED                            0x1903
#define GL_GREEN                          0x1904
#define GL_BLUE                           0x1905
#define GL_ALPHA                          0x1906
#define GL_RGB                            0x1907
#define GL_RGBA                           0x1908
#define GL_LUMINANCE                      0x1909
#define GL_LUMINANCE_ALPHA                0x190A
#define GL_BITMAP                         0x1A00
#define GL_POINT                          0x1B00
#define GL_LINE                           0x1B01
#define GL_FILL                           0x1B02
#define GL_RENDER                         0x1C00
#define GL_FEEDBACK                       0x1C01
#define GL_SELECT                         0x1C02
#define GL_FLAT                           0x1D00
#define GL_SMOOTH                         0x1D01
#define GL_KEEP                           0x1E00
#define GL_REPLACE                        0x1E01
#define GL_INCR                           0x1E02
#define GL_DECR                           0x1E03
#define GL_VENDOR                         0x1F00
#define GL_RENDERER                       0x1F01
#define GL_VERSION                        0x1F02
#define GL_EXTENSIONS                     0x1F03
#define GL_S                              0x2000
#define GL_T                              0x2001
#define GL_R                              0x2002
#define GL_Q                              0x2003
#define GL_MODULATE                       0x2100
#define GL_DECAL                          0x2101
#define GL_TEXTURE_ENV_MODE               0x2200
#define GL_TEXTURE_ENV_COLOR              0x2201
#define GL_TEXTURE_ENV                    0x2300
#define GL_EYE_LINEAR                     0x2400
#define GL_OBJECT_LINEAR                  0x2401
#define GL_SPHERE_MAP                     0x2402
#define GL_TEXTURE_GEN_MODE               0x2500
#define GL_OBJECT_PLANE                   0x2501
#define GL_EYE_PLANE                      0x2502
#define GL_NEAREST                        0x2600
#define GL_LINEAR                         0x2601
#define GL_NEAREST_MIPMAP_NEAREST         0x2700
#define GL_LINEAR_MIPMAP_NEAREST          0x2701
#define GL_NEAREST_MIPMAP_LINEAR          0x2702
#define GL_LINEAR_MIPMAP_LINEAR           0x2703
#define GL_TEXTURE_MAG_FILTER             0x2800
#define GL_TEXTURE_MIN_FILTER             0x2801
#define GL_TEXTURE_WRAP_S                 0x2802
#define GL_TEXTURE_WRAP_T                 0x2803
#define GL_CLAMP                          0x2900
#define GL_REPEAT                         0x2901
#define GL_CLIENT_PIXEL_STORE_BIT         0x00000001
#define GL_CLIENT_VERTEX_ARRAY_BIT        0x00000002
#define GL_CLIENT_ALL_ATTRIB_BITS         0xffffffff
#define GL_POLYGON_OFFSET_FACTOR          0x8038
#define GL_POLYGON_OFFSET_UNITS           0x2A00
#define GL_POLYGON_OFFSET_POINT           0x2A01
#define GL_POLYGON_OFFSET_LINE            0x2A02
#define GL_POLYGON_OFFSET_FILL            0x8037
#define GL_ALPHA4                         0x803B
#define GL_ALPHA8                         0x803C
#define GL_ALPHA12                        0x803D
#define GL_ALPHA16                        0x803E
#define GL_LUMINANCE4                     0x803F
#define GL_LUMINANCE8                     0x8040
#define GL_LUMINANCE12                    0x8041
#define GL_LUMINANCE16                    0x8042
#define GL_LUMINANCE4_ALPHA4              0x8043
#define GL_LUMINANCE6_ALPHA2              0x8044
#define GL_LUMINANCE8_ALPHA8              0x8045
#define GL_LUMINANCE12_ALPHA4             0x8046
#define GL_LUMINANCE12_ALPHA12            0x8047
#define GL_LUMINANCE16_ALPHA16            0x8048
#define GL_INTENSITY                      0x8049
#define GL_INTENSITY4                     0x804A
#define GL_INTENSITY8                     0x804B
#define GL_INTENSITY12                    0x804C
#define GL_INTENSITY16                    0x804D
#define GL_R3_G3_B2                       0x2A10
#define GL_RGB4                           0x804F
#define GL_RGB5                           0x8050
#define GL_RGB8                           0x8051
#define GL_RGB10                          0x8052
#define GL_RGB12                          0x8053
#define GL_RGB16                          0x8054
#define GL_RGBA2                          0x8055
#define GL_RGBA4                          0x8056
#define GL_RGB5_A1                        0x8057
#define GL_RGBA8                          0x8058
#define GL_RGB10_A2                       0x8059
#define GL_RGBA12                         0x805A
#define GL_RGBA16                         0x805B
#define GL_TEXTURE_RED_SIZE               0x805C
#define GL_TEXTURE_GREEN_SIZE             0x805D
#define GL_TEXTURE_BLUE_SIZE              0x805E
#define GL_TEXTURE_ALPHA_SIZE             0x805F
#define GL_TEXTURE_LUMINANCE_SIZE         0x8060
#define GL_TEXTURE_INTENSITY_SIZE         0x8061
#define GL_PROXY_TEXTURE_1D               0x8063
#define GL_PROXY_TEXTURE_2D               0x8064
#define GL_TEXTURE_PRIORITY               0x8066
#define GL_TEXTURE_RESIDENT               0x8067
#define GL_TEXTURE_BINDING_1D             0x8068
#define GL_TEXTURE_BINDING_2D             0x8069
#define GL_VERTEX_ARRAY                   0x8074
#define GL_NORMAL_ARRAY                   0x8075
#define GL_COLOR_ARRAY                    0x8076
#define GL_INDEX_ARRAY                    0x8077
#define GL_TEXTURE_COORD_ARRAY            0x8078
#define GL_EDGE_FLAG_ARRAY                0x8079
#define GL_VERTEX_ARRAY_SIZE              0x807A
#define GL_VERTEX_ARRAY_TYPE              0x807B
#define GL_VERTEX_ARRAY_STRIDE            0x807C
#define GL_NORMAL_ARRAY_TYPE              0x807E
#define GL_NORMAL_ARRAY_STRIDE            0x807F
#define GL_COLOR_ARRAY_SIZE               0x8081
#define GL_COLOR_ARRAY_TYPE               0x8082
#define GL_COLOR_ARRAY_STRIDE             0x8083
#define GL_INDEX_ARRAY_TYPE               0x8085
#define GL_INDEX_ARRAY_STRIDE             0x8086
#define GL_TEXTURE_COORD_ARRAY_SIZE       0x8088
#define GL_TEXTURE_COORD_ARRAY_TYPE       0x8089
#define GL_TEXTURE_COORD_ARRAY_STRIDE     0x808A
#define GL_EDGE_FLAG_ARRAY_STRIDE         0x808C
#define GL_VERTEX_ARRAY_POINTER           0x808E
#define GL_NORMAL_ARRAY_POINTER           0x808F
#define GL_COLOR_ARRAY_POINTER            0x8090
#define GL_INDEX_ARRAY_POINTER            0x8091
#define GL_TEXTURE_COORD_ARRAY_POINTER    0x8092
#define GL_EDGE_FLAG_ARRAY_POINTER        0x8093
#define GL_V2F                            0x2A20
#define GL_V3F                            0x2A21
#define GL_C4UB_V2F                       0x2A22
#define GL_C4UB_V3F                       0x2A23
#define GL_C3F_V3F                        0x2A24
#define GL_N3F_V3F                        0x2A25
#define GL_C4F_N3F_V3F                    0x2A26
#define GL_T2F_V3F                        0x2A27
#define GL_T4F_V4F                        0x2A28
#define GL_T2F_C4UB_V3F                   0x2A29
#define GL_T2F_C3F_V3F                    0x2A2A
#define GL_T2F_N3F_V3F                    0x2A2B
#define GL_T2F_C4F_N3F_V3F                0x2A2C
#define GL_T4F_C4F_N3F_V4F                0x2A2D
#endif</t>
<t tx="ekr.20060513122613.7">#ifndef GL_DEFS
GL_PROC(void,glAccum,(GLenum op, GLfloat value))
GL_PROC(void,glAlphaFunc,(GLenum func, GLclampf ref))
GL_PROC(GLboolean,glAreTexturesResident,(GLsizei n, const GLuint *textures, GLboolean *residences))
GL_PROC(void,glArrayElement,(GLint i))
GL_PROC(void,glBegin,(GLenum mode))
GL_PROC(void,glBindTexture,(GLenum target, GLuint texture))
GL_PROC(void,glBitmap,(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap))
GL_PROC(void,glBlendFunc,(GLenum sfactor, GLenum dfactor))
GL_PROC(void,glCallList,(GLuint list))
GL_PROC(void,glCallLists,(GLsizei n, GLenum type, const GLvoid *lists))
GL_PROC(void,glClear,(GLbitfield mask))
GL_PROC(void,glClearAccum,(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha))
GL_PROC(void,glClearColor,(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha))
GL_PROC(void,glClearDepth,(GLclampd depth))
GL_PROC(void,glClearIndex,(GLfloat c))
GL_PROC(void,glClearStencil,(GLint s))
GL_PROC(void,glClipPlane,(GLenum plane, const GLdouble *equation))
GL_PROC(void,glColor3b,(GLbyte red, GLbyte green, GLbyte blue))
GL_PROC(void,glColor3bv,(const GLbyte *v))
GL_PROC(void,glColor3d,(GLdouble red, GLdouble green, GLdouble blue))
GL_PROC(void,glColor3dv,(const GLdouble *v))
GL_PROC(void,glColor3f,(GLfloat red, GLfloat green, GLfloat blue))
GL_PROC(void,glColor3fv,(const GLfloat *v))
GL_PROC(void,glColor3i,(GLint red, GLint green, GLint blue))
GL_PROC(void,glColor3iv,(const GLint *v))
GL_PROC(void,glColor3s,(GLshort red, GLshort green, GLshort blue))
GL_PROC(void,glColor3sv,(const GLshort *v))
GL_PROC(void,glColor3ub,(GLubyte red, GLubyte green, GLubyte blue))
GL_PROC(void,glColor3ubv,(const GLubyte *v))
GL_PROC(void,glColor3ui,(GLuint red, GLuint green, GLuint blue))
GL_PROC(void,glColor3uiv,(const GLuint *v))
GL_PROC(void,glColor3us,(GLushort red, GLushort green, GLushort blue))
GL_PROC(void,glColor3usv,(const GLushort *v))
GL_PROC(void,glColor4b,(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha))
GL_PROC(void,glColor4bv,(const GLbyte *v))
GL_PROC(void,glColor4d,(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha))
GL_PROC(void,glColor4dv,(const GLdouble *v))
GL_PROC(void,glColor4f,(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha))
GL_PROC(void,glColor4fv,(const GLfloat *v))
GL_PROC(void,glColor4i,(GLint red, GLint green, GLint blue, GLint alpha))
GL_PROC(void,glColor4iv,(const GLint *v))
GL_PROC(void,glColor4s,(GLshort red, GLshort green, GLshort blue, GLshort alpha))
GL_PROC(void,glColor4sv,(const GLshort *v))
GL_PROC(void,glColor4ub,(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha))
GL_PROC(void,glColor4ubv,(const GLubyte *v))
GL_PROC(void,glColor4ui,(GLuint red, GLuint green, GLuint blue, GLuint alpha))
GL_PROC(void,glColor4uiv,(const GLuint *v))
GL_PROC(void,glColor4us,(GLushort red, GLushort green, GLushort blue, GLushort alpha))
GL_PROC(void,glColor4usv,(const GLushort *v))
GL_PROC(void,glColorMask,(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha))
GL_PROC(void,glColorMaterial,(GLenum face, GLenum mode))
GL_PROC(void,glColorPointer,(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer))
GL_PROC(void,glCopyPixels,(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type))
GL_PROC(void,glCopyTexImage1D,(GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLint border))
GL_PROC(void,glCopyTexImage2D,(GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border))
GL_PROC(void,glCopyTexSubImage1D,(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width))
GL_PROC(void,glCopyTexSubImage2D,(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height))
GL_PROC(void,glCullFace,(GLenum mode))
GL_PROC(void,glDeleteLists,(GLuint list, GLsizei range))
GL_PROC(void,glDeleteTextures,(GLsizei n, const GLuint *textures))
GL_PROC(void,glDepthFunc,(GLenum func))
GL_PROC(void,glDepthMask,(GLboolean flag))
GL_PROC(void,glDepthRange,(GLclampd zNear, GLclampd zFar))
GL_PROC(void,glDisable,(GLenum cap))
GL_PROC(void,glDisableClientState,(GLenum array))
GL_PROC(void,glDrawArrays,(GLenum mode, GLint first, GLsizei count))
GL_PROC(void,glDrawBuffer,(GLenum mode))
GL_PROC(void,glDrawElements,(GLenum mode, GLsizei count, GLenum type, const GLvoid *indices))
GL_PROC(void,glDrawPixels,(GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels))
GL_PROC(void,glEdgeFlag,(GLboolean flag))
GL_PROC(void,glEdgeFlagPointer,(GLsizei stride, const GLvoid *pointer))
GL_PROC(void,glEdgeFlagv,(const GLboolean *flag))
GL_PROC(void,glEnable,(GLenum cap))
GL_PROC(void,glEnableClientState,(GLenum array))
GL_PROC(void,glEnd,(void))
GL_PROC(void,glEndList,(void))
GL_PROC(void,glEvalCoord1d,(GLdouble u))
GL_PROC(void,glEvalCoord1dv,(const GLdouble *u))
GL_PROC(void,glEvalCoord1f,(GLfloat u))
GL_PROC(void,glEvalCoord1fv,(const GLfloat *u))
GL_PROC(void,glEvalCoord2d,(GLdouble u, GLdouble v))
GL_PROC(void,glEvalCoord2dv,(const GLdouble *u))
GL_PROC(void,glEvalCoord2f,(GLfloat u, GLfloat v))
GL_PROC(void,glEvalCoord2fv,(const GLfloat *u))
GL_PROC(void,glEvalMesh1,(GLenum mode, GLint i1, GLint i2))
GL_PROC(void,glEvalMesh2,(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2))
GL_PROC(void,glEvalPoint1,(GLint i))
GL_PROC(void,glEvalPoint2,(GLint i, GLint j))
GL_PROC(void,glFeedbackBuffer,(GLsizei size, GLenum type, GLfloat *buffer))
GL_PROC(void,glFinish,(void))
GL_PROC(void,glFlush,(void))
GL_PROC(void,glFogf,(GLenum pname, GLfloat param))
GL_PROC(void,glFogfv,(GLenum pname, const GLfloat *params))
GL_PROC(void,glFogi,(GLenum pname, GLint param))
GL_PROC(void,glFogiv,(GLenum pname, const GLint *params))
GL_PROC(void,glFrontFace,(GLenum mode))
GL_PROC(void,glFrustum,(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar))
GL_PROC(GLuint,glGenLists,(GLsizei range))
GL_PROC(void,glGenTextures,(GLsizei n, GLuint *textures))
GL_PROC(void,glGetBooleanv,(GLenum pname, GLboolean *params))
GL_PROC(void,glGetClipPlane,(GLenum plane, GLdouble *equation))
GL_PROC(void,glGetDoublev,(GLenum pname, GLdouble *params))
GL_PROC(GLenum,glGetError,(void))
GL_PROC(void,glGetFloatv,(GLenum pname, GLfloat *params))
GL_PROC(void,glGetIntegerv,(GLenum pname, GLint *params))
GL_PROC(void,glGetLightfv,(GLenum light, GLenum pname, GLfloat *params))
GL_PROC(void,glGetLightiv,(GLenum light, GLenum pname, GLint *params))
GL_PROC(void,glGetMapdv,(GLenum target, GLenum query, GLdouble *v))
GL_PROC(void,glGetMapfv,(GLenum target, GLenum query, GLfloat *v))
GL_PROC(void,glGetMapiv,(GLenum target, GLenum query, GLint *v))
GL_PROC(void,glGetMaterialfv,(GLenum face, GLenum pname, GLfloat *params))
GL_PROC(void,glGetMaterialiv,(GLenum face, GLenum pname, GLint *params))
GL_PROC(void,glGetPixelMapfv,(GLenum map, GLfloat *values))
GL_PROC(void,glGetPixelMapuiv,(GLenum map, GLuint *values))
GL_PROC(void,glGetPixelMapusv,(GLenum map, GLushort *values))
GL_PROC(void,glGetPointerv,(GLenum pname, GLvoid* *params))
GL_PROC(void,glGetPolygonStipple,(GLubyte *mask))
GL_PROC(const GLubyte *,glGetString,(GLenum name))
GL_PROC(void,glGetTexEnvfv,(GLenum target, GLenum pname, GLfloat *params))
GL_PROC(void,glGetTexEnviv,(GLenum target, GLenum pname, GLint *params))
GL_PROC(void,glGetTexGendv,(GLenum coord, GLenum pname, GLdouble *params))
GL_PROC(void,glGetTexGenfv,(GLenum coord, GLenum pname, GLfloat *params))
GL_PROC(void,glGetTexGeniv,(GLenum coord, GLenum pname, GLint *params))
GL_PROC(void,glGetTexImage,(GLenum target, GLint level, GLenum format, GLenum type, GLvoid *pixels))
GL_PROC(void,glGetTexLevelParameterfv,(GLenum target, GLint level, GLenum pname, GLfloat *params))
GL_PROC(void,glGetTexLevelParameteriv,(GLenum target, GLint level, GLenum pname, GLint *params))
GL_PROC(void,glGetTexParameterfv,(GLenum target, GLenum pname, GLfloat *params))
GL_PROC(void,glGetTexParameteriv,(GLenum target, GLenum pname, GLint *params))
GL_PROC(void,glHint,(GLenum target, GLenum mode))
GL_PROC(void,glIndexMask,(GLuint mask))
GL_PROC(void,glIndexPointer,(GLenum type, GLsizei stride, const GLvoid *pointer))
GL_PROC(void,glIndexd,(GLdouble c))
GL_PROC(void,glIndexdv,(const GLdouble *c))
GL_PROC(void,glIndexf,(GLfloat c))
GL_PROC(void,glIndexfv,(const GLfloat *c))
GL_PROC(void,glIndexi,(GLint c))
GL_PROC(void,glIndexiv,(const GLint *c))
GL_PROC(void,glIndexs,(GLshort c))
GL_PROC(void,glIndexsv,(const GLshort *c))
GL_PROC(void,glIndexub,(GLubyte c))
GL_PROC(void,glIndexubv,(const GLubyte *c))
GL_PROC(void,glInitNames,(void))
GL_PROC(void,glInterleavedArrays,(GLenum format, GLsizei stride, const GLvoid *pointer))
GL_PROC(GLboolean,glIsEnabled,(GLenum cap))
GL_PROC(GLboolean,glIsList,(GLuint list))
GL_PROC(GLboolean,glIsTexture,(GLuint texture))
GL_PROC(void,glLightModelf,(GLenum pname, GLfloat param))
GL_PROC(void,glLightModelfv,(GLenum pname, const GLfloat *params))
GL_PROC(void,glLightModeli,(GLenum pname, GLint param))
GL_PROC(void,glLightModeliv,(GLenum pname, const GLint *params))
GL_PROC(void,glLightf,(GLenum light, GLenum pname, GLfloat param))
GL_PROC(void,glLightfv,(GLenum light, GLenum pname, const GLfloat *params))
GL_PROC(void,glLighti,(GLenum light, GLenum pname, GLint param))
GL_PROC(void,glLightiv,(GLenum light, GLenum pname, const GLint *params))
GL_PROC(void,glLineStipple,(GLint factor, GLushort pattern))
GL_PROC(void,glLineWidth,(GLfloat width))
GL_PROC(void,glListBase,(GLuint base))
GL_PROC(void,glLoadIdentity,(void))
GL_PROC(void,glLoadMatrixd,(const GLdouble *m))
GL_PROC(void,glLoadMatrixf,(const GLfloat *m))
GL_PROC(void,glLoadName,(GLuint name))
GL_PROC(void,glLogicOp,(GLenum opcode))
GL_PROC(void,glMap1d,(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points))
GL_PROC(void,glMap1f,(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points))
GL_PROC(void,glMap2d,(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points))
GL_PROC(void,glMap2f,(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points))
GL_PROC(void,glMapGrid1d,(GLint un, GLdouble u1, GLdouble u2))
GL_PROC(void,glMapGrid1f,(GLint un, GLfloat u1, GLfloat u2))
GL_PROC(void,glMapGrid2d,(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2))
GL_PROC(void,glMapGrid2f,(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2))
GL_PROC(void,glMaterialf,(GLenum face, GLenum pname, GLfloat param))
GL_PROC(void,glMaterialfv,(GLenum face, GLenum pname, const GLfloat *params))
GL_PROC(void,glMateriali,(GLenum face, GLenum pname, GLint param))
GL_PROC(void,glMaterialiv,(GLenum face, GLenum pname, const GLint *params))
GL_PROC(void,glMatrixMode,(GLenum mode))
GL_PROC(void,glMultMatrixd,(const GLdouble *m))
GL_PROC(void,glMultMatrixf,(const GLfloat *m))
GL_PROC(void,glNewList,(GLuint list, GLenum mode))
GL_PROC(void,glNormal3b,(GLbyte nx, GLbyte ny, GLbyte nz))
GL_PROC(void,glNormal3bv,(const GLbyte *v))
GL_PROC(void,glNormal3d,(GLdouble nx, GLdouble ny, GLdouble nz))
GL_PROC(void,glNormal3dv,(const GLdouble *v))
GL_PROC(void,glNormal3f,(GLfloat nx, GLfloat ny, GLfloat nz))
GL_PROC(void,glNormal3fv,(const GLfloat *v))
GL_PROC(void,glNormal3i,(GLint nx, GLint ny, GLint nz))
GL_PROC(void,glNormal3iv,(const GLint *v))
GL_PROC(void,glNormal3s,(GLshort nx, GLshort ny, GLshort nz))
GL_PROC(void,glNormal3sv,(const GLshort *v))
GL_PROC(void,glNormalPointer,(GLenum type, GLsizei stride, const GLvoid *pointer))
GL_PROC(void,glOrtho,(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar))
GL_PROC(void,glPassThrough,(GLfloat token))
GL_PROC(void,glPixelMapfv,(GLenum map, GLsizei mapsize, const GLfloat *values))
GL_PROC(void,glPixelMapuiv,(GLenum map, GLsizei mapsize, const GLuint *values))
GL_PROC(void,glPixelMapusv,(GLenum map, GLsizei mapsize, const GLushort *values))
GL_PROC(void,glPixelStoref,(GLenum pname, GLfloat param))
GL_PROC(void,glPixelStorei,(GLenum pname, GLint param))
GL_PROC(void,glPixelTransferf,(GLenum pname, GLfloat param))
GL_PROC(void,glPixelTransferi,(GLenum pname, GLint param))
GL_PROC(void,glPixelZoom,(GLfloat xfactor, GLfloat yfactor))
GL_PROC(void,glPointSize,(GLfloat size))
GL_PROC(void,glPolygonMode,(GLenum face, GLenum mode))
GL_PROC(void,glPolygonOffset,(GLfloat factor, GLfloat units))
GL_PROC(void,glPolygonStipple,(const GLubyte *mask))
GL_PROC(void,glPopAttrib,(void))
GL_PROC(void,glPopClientAttrib,(void))
GL_PROC(void,glPopMatrix,(void))
GL_PROC(void,glPopName,(void))
GL_PROC(void,glPrioritizeTextures,(GLsizei n, const GLuint *textures, const GLclampf *priorities))
GL_PROC(void,glPushAttrib,(GLbitfield mask))
GL_PROC(void,glPushClientAttrib,(GLbitfield mask))
GL_PROC(void,glPushMatrix,(void))
GL_PROC(void,glPushName,(GLuint name))
GL_PROC(void,glRasterPos2d,(GLdouble x, GLdouble y))
GL_PROC(void,glRasterPos2dv,(const GLdouble *v))
GL_PROC(void,glRasterPos2f,(GLfloat x, GLfloat y))
GL_PROC(void,glRasterPos2fv,(const GLfloat *v))
GL_PROC(void,glRasterPos2i,(GLint x, GLint y))
GL_PROC(void,glRasterPos2iv,(const GLint *v))
GL_PROC(void,glRasterPos2s,(GLshort x, GLshort y))
GL_PROC(void,glRasterPos2sv,(const GLshort *v))
GL_PROC(void,glRasterPos3d,(GLdouble x, GLdouble y, GLdouble z))
GL_PROC(void,glRasterPos3dv,(const GLdouble *v))
GL_PROC(void,glRasterPos3f,(GLfloat x, GLfloat y, GLfloat z))
GL_PROC(void,glRasterPos3fv,(const GLfloat *v))
GL_PROC(void,glRasterPos3i,(GLint x, GLint y, GLint z))
GL_PROC(void,glRasterPos3iv,(const GLint *v))
GL_PROC(void,glRasterPos3s,(GLshort x, GLshort y, GLshort z))
GL_PROC(void,glRasterPos3sv,(const GLshort *v))
GL_PROC(void,glRasterPos4d,(GLdouble x, GLdouble y, GLdouble z, GLdouble w))
GL_PROC(void,glRasterPos4dv,(const GLdouble *v))
GL_PROC(void,glRasterPos4f,(GLfloat x, GLfloat y, GLfloat z, GLfloat w))
GL_PROC(void,glRasterPos4fv,(const GLfloat *v))
GL_PROC(void,glRasterPos4i,(GLint x, GLint y, GLint z, GLint w))
GL_PROC(void,glRasterPos4iv,(const GLint *v))
GL_PROC(void,glRasterPos4s,(GLshort x, GLshort y, GLshort z, GLshort w))
GL_PROC(void,glRasterPos4sv,(const GLshort *v))
GL_PROC(void,glReadBuffer,(GLenum mode))
GL_PROC(void,glReadPixels,(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid *pixels))
GL_PROC(void,glRectd,(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2))
GL_PROC(void,glRectdv,(const GLdouble *v1, const GLdouble *v2))
GL_PROC(void,glRectf,(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2))
GL_PROC(void,glRectfv,(const GLfloat *v1, const GLfloat *v2))
GL_PROC(void,glRecti,(GLint x1, GLint y1, GLint x2, GLint y2))
GL_PROC(void,glRectiv,(const GLint *v1, const GLint *v2))
GL_PROC(void,glRects,(GLshort x1, GLshort y1, GLshort x2, GLshort y2))
GL_PROC(void,glRectsv,(const GLshort *v1, const GLshort *v2))
GL_PROC(GLint,glRenderMode,(GLenum mode))
GL_PROC(void,glRotated,(GLdouble angle, GLdouble x, GLdouble y, GLdouble z))
GL_PROC(void,glRotatef,(GLfloat angle, GLfloat x, GLfloat y, GLfloat z))
GL_PROC(void,glScaled,(GLdouble x, GLdouble y, GLdouble z))
GL_PROC(void,glScalef,(GLfloat x, GLfloat y, GLfloat z))
GL_PROC(void,glScissor,(GLint x, GLint y, GLsizei width, GLsizei height))
GL_PROC(void,glSelectBuffer,(GLsizei size, GLuint *buffer))
GL_PROC(void,glShadeModel,(GLenum mode))
GL_PROC(void,glStencilFunc,(GLenum func, GLint ref, GLuint mask))
GL_PROC(void,glStencilMask,(GLuint mask))
GL_PROC(void,glStencilOp,(GLenum fail, GLenum zfail, GLenum zpass))
GL_PROC(void,glTexCoord1d,(GLdouble s))
GL_PROC(void,glTexCoord1dv,(const GLdouble *v))
GL_PROC(void,glTexCoord1f,(GLfloat s))
GL_PROC(void,glTexCoord1fv,(const GLfloat *v))
GL_PROC(void,glTexCoord1i,(GLint s))
GL_PROC(void,glTexCoord1iv,(const GLint *v))
GL_PROC(void,glTexCoord1s,(GLshort s))
GL_PROC(void,glTexCoord1sv,(const GLshort *v))
GL_PROC(void,glTexCoord2d,(GLdouble s, GLdouble t))
GL_PROC(void,glTexCoord2dv,(const GLdouble *v))
GL_PROC(void,glTexCoord2f,(GLfloat s, GLfloat t))
GL_PROC(void,glTexCoord2fv,(const GLfloat *v))
GL_PROC(void,glTexCoord2i,(GLint s, GLint t))
GL_PROC(void,glTexCoord2iv,(const GLint *v))
GL_PROC(void,glTexCoord2s,(GLshort s, GLshort t))
GL_PROC(void,glTexCoord2sv,(const GLshort *v))
GL_PROC(void,glTexCoord3d,(GLdouble s, GLdouble t, GLdouble r))
GL_PROC(void,glTexCoord3dv,(const GLdouble *v))
GL_PROC(void,glTexCoord3f,(GLfloat s, GLfloat t, GLfloat r))
GL_PROC(void,glTexCoord3fv,(const GLfloat *v))
GL_PROC(void,glTexCoord3i,(GLint s, GLint t, GLint r))
GL_PROC(void,glTexCoord3iv,(const GLint *v))
GL_PROC(void,glTexCoord3s,(GLshort s, GLshort t, GLshort r))
GL_PROC(void,glTexCoord3sv,(const GLshort *v))
GL_PROC(void,glTexCoord4d,(GLdouble s, GLdouble t, GLdouble r, GLdouble q))
GL_PROC(void,glTexCoord4dv,(const GLdouble *v))
GL_PROC(void,glTexCoord4f,(GLfloat s, GLfloat t, GLfloat r, GLfloat q))
GL_PROC(void,glTexCoord4fv,(const GLfloat *v))
GL_PROC(void,glTexCoord4i,(GLint s, GLint t, GLint r, GLint q))
GL_PROC(void,glTexCoord4iv,(const GLint *v))
GL_PROC(void,glTexCoord4s,(GLshort s, GLshort t, GLshort r, GLshort q))
GL_PROC(void,glTexCoord4sv,(const GLshort *v))
GL_PROC(void,glTexCoordPointer,(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer))
GL_PROC(void,glTexEnvf,(GLenum target, GLenum pname, GLfloat param))
GL_PROC(void,glTexEnvfv,(GLenum target, GLenum pname, const GLfloat *params))
GL_PROC(void,glTexEnvi,(GLenum target, GLenum pname, GLint param))
GL_PROC(void,glTexEnviv,(GLenum target, GLenum pname, const GLint *params))
GL_PROC(void,glTexGend,(GLenum coord, GLenum pname, GLdouble param))
GL_PROC(void,glTexGendv,(GLenum coord, GLenum pname, const GLdouble *params))
GL_PROC(void,glTexGenf,(GLenum coord, GLenum pname, GLfloat param))
GL_PROC(void,glTexGenfv,(GLenum coord, GLenum pname, const GLfloat *params))
GL_PROC(void,glTexGeni,(GLenum coord, GLenum pname, GLint param))
GL_PROC(void,glTexGeniv,(GLenum coord, GLenum pname, const GLint *params))
GL_PROC(void,glTexImage1D,(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels))
GL_PROC(void,glTexImage2D,(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels))
GL_PROC(void,glTexParameterf,(GLenum target, GLenum pname, GLfloat param))
GL_PROC(void,glTexParameterfv,(GLenum target, GLenum pname, const GLfloat *params))
GL_PROC(void,glTexParameteri,(GLenum target, GLenum pname, GLint param))
GL_PROC(void,glTexParameteriv,(GLenum target, GLenum pname, const GLint *params))
GL_PROC(void,glTexSubImage1D,(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels))
GL_PROC(void,glTexSubImage2D,(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels))
GL_PROC(void,glTranslated,(GLdouble x, GLdouble y, GLdouble z))
GL_PROC(void,glTranslatef,(GLfloat x, GLfloat y, GLfloat z))
GL_PROC(void,glVertex2d,(GLdouble x, GLdouble y))
GL_PROC(void,glVertex2dv,(const GLdouble *v))
GL_PROC(void,glVertex2f,(GLfloat x, GLfloat y))
GL_PROC(void,glVertex2fv,(const GLfloat *v))
GL_PROC(void,glVertex2i,(GLint x, GLint y))
GL_PROC(void,glVertex2iv,(const GLint *v))
GL_PROC(void,glVertex2s,(GLshort x, GLshort y))
GL_PROC(void,glVertex2sv,(const GLshort *v))
GL_PROC(void,glVertex3d,(GLdouble x, GLdouble y, GLdouble z))
GL_PROC(void,glVertex3dv,(const GLdouble *v))
GL_PROC(void,glVertex3f,(GLfloat x, GLfloat y, GLfloat z))
GL_PROC(void,glVertex3fv,(const GLfloat *v))
GL_PROC(void,glVertex3i,(GLint x, GLint y, GLint z))
GL_PROC(void,glVertex3iv,(const GLint *v))
GL_PROC(void,glVertex3s,(GLshort x, GLshort y, GLshort z))
GL_PROC(void,glVertex3sv,(const GLshort *v))
GL_PROC(void,glVertex4d,(GLdouble x, GLdouble y, GLdouble z, GLdouble w))
GL_PROC(void,glVertex4dv,(const GLdouble *v))
GL_PROC(void,glVertex4f,(GLfloat x, GLfloat y, GLfloat z, GLfloat w))
GL_PROC(void,glVertex4fv,(const GLfloat *v))
GL_PROC(void,glVertex4i,(GLint x, GLint y, GLint z, GLint w))
GL_PROC(void,glVertex4iv,(const GLint *v))
GL_PROC(void,glVertex4s,(GLshort x, GLshort y, GLshort z, GLshort w))
GL_PROC(void,glVertex4sv,(const GLshort *v))
GL_PROC(void,glVertexPointer,(GLint size, GLenum type, GLsizei stride, const GLvoid *pointer))
GL_PROC(void,glViewport,(GLint x, GLint y, GLsizei width, GLsizei height))
#endif</t>
<t tx="ekr.20060513122613.8">#if USE_OPENGL &gt;= 2
	@others
#endif</t>
<t tx="ekr.20060513122613.9">#ifdef GL_DEFS
#define GL_UNSIGNED_BYTE_3_3_2            0x8032
#define GL_UNSIGNED_SHORT_4_4_4_4         0x8033
#define GL_UNSIGNED_SHORT_5_5_5_1         0x8034
#define GL_UNSIGNED_INT_8_8_8_8           0x8035
#define GL_UNSIGNED_INT_10_10_10_2        0x8036
#define GL_RESCALE_NORMAL                 0x803A
#define GL_TEXTURE_BINDING_3D             0x806A
#define GL_PACK_SKIP_IMAGES               0x806B
#define GL_PACK_IMAGE_HEIGHT              0x806C
#define GL_UNPACK_SKIP_IMAGES             0x806D
#define GL_UNPACK_IMAGE_HEIGHT            0x806E
#define GL_TEXTURE_3D                     0x806F
#define GL_PROXY_TEXTURE_3D               0x8070
#define GL_TEXTURE_DEPTH                  0x8071
#define GL_TEXTURE_WRAP_R                 0x8072
#define GL_MAX_3D_TEXTURE_SIZE            0x8073
#define GL_UNSIGNED_BYTE_2_3_3_REV        0x8362
#define GL_UNSIGNED_SHORT_5_6_5           0x8363
#define GL_UNSIGNED_SHORT_5_6_5_REV       0x8364
#define GL_UNSIGNED_SHORT_4_4_4_4_REV     0x8365
#define GL_UNSIGNED_SHORT_1_5_5_5_REV     0x8366
#define GL_UNSIGNED_INT_8_8_8_8_REV       0x8367
#define GL_UNSIGNED_INT_2_10_10_10_REV    0x8368
#define GL_BGR                            0x80E0
#define GL_BGRA                           0x80E1
#define GL_MAX_ELEMENTS_VERTICES          0x80E8
#define GL_MAX_ELEMENTS_INDICES           0x80E9
#define GL_CLAMP_TO_EDGE                  0x812F
#define GL_TEXTURE_MIN_LOD                0x813A
#define GL_TEXTURE_MAX_LOD                0x813B
#define GL_TEXTURE_BASE_LEVEL             0x813C
#define GL_TEXTURE_MAX_LEVEL              0x813D
#define GL_LIGHT_MODEL_COLOR_CONTROL      0x81F8
#define GL_SINGLE_COLOR                   0x81F9
#define GL_SEPARATE_SPECULAR_COLOR        0x81FA
#define GL_SMOOTH_POINT_SIZE_RANGE        0x0B12
#define GL_SMOOTH_POINT_SIZE_GRANULARITY  0x0B13
#define GL_SMOOTH_LINE_WIDTH_RANGE        0x0B22
#define GL_SMOOTH_LINE_WIDTH_GRANULARITY  0x0B23
#define GL_ALIASED_POINT_SIZE_RANGE       0x846D
#define GL_ALIASED_LINE_WIDTH_RANGE       0x846E
#endif</t>
<t tx="ekr.20060513122613.10">#ifndef GL_DEFS
GL_EXT(void,glBlendColor,(GLclampf, GLclampf, GLclampf, GLclampf))
GL_EXT(void,glBlendEquation,(GLenum))
GL_EXT(void,glDrawRangeElements,(GLenum, GLuint, GLuint, GLsizei, GLenum, const GLvoid *))
GL_EXT(void,glColorTable,(GLenum, GLenum, GLsizei, GLenum, GLenum, const GLvoid *))
GL_EXT(void,glColorTableParameterfv,(GLenum, GLenum, const GLfloat *))
GL_EXT(void,glColorTableParameteriv,(GLenum, GLenum, const GLint *))
GL_EXT(void,glCopyColorTable,(GLenum, GLenum, GLint, GLint, GLsizei))
GL_EXT(void,glGetColorTable,(GLenum, GLenum, GLenum, GLvoid *))
GL_EXT(void,glGetColorTableParameterfv,(GLenum, GLenum, GLfloat *))
GL_EXT(void,glGetColorTableParameteriv,(GLenum, GLenum, GLint *))
GL_EXT(void,glColorSubTable,(GLenum, GLsizei, GLsizei, GLenum, GLenum, const GLvoid *))
GL_EXT(void,glCopyColorSubTable,(GLenum, GLsizei, GLint, GLint, GLsizei))
GL_EXT(void,glConvolutionFilter1D,(GLenum, GLenum, GLsizei, GLenum, GLenum, const GLvoid *))
GL_EXT(void,glConvolutionFilter2D,(GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, const GLvoid *))
GL_EXT(void,glConvolutionParameterf,(GLenum, GLenum, GLfloat))
GL_EXT(void,glConvolutionParameterfv,(GLenum, GLenum, const GLfloat *))
GL_EXT(void,glConvolutionParameteri,(GLenum, GLenum, GLint))
GL_EXT(void,glConvolutionParameteriv,(GLenum, GLenum, const GLint *))
GL_EXT(void,glCopyConvolutionFilter1D,(GLenum, GLenum, GLint, GLint, GLsizei))
GL_EXT(void,glCopyConvolutionFilter2D,(GLenum, GLenum, GLint, GLint, GLsizei, GLsizei))
GL_EXT(void,glGetConvolutionFilter,(GLenum, GLenum, GLenum, GLvoid *))
GL_EXT(void,glGetConvolutionParameterfv,(GLenum, GLenum, GLfloat *))
GL_EXT(void,glGetConvolutionParameteriv,(GLenum, GLenum, GLint *))
GL_EXT(void,glGetSeparableFilter,(GLenum, GLenum, GLenum, GLvoid *, GLvoid *, GLvoid *))
GL_EXT(void,glSeparableFilter2D,(GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, const GLvoid *, const GLvoid *))
GL_EXT(void,glGetHistogram,(GLenum, GLboolean, GLenum, GLenum, GLvoid *))
GL_EXT(void,glGetHistogramParameterfv,(GLenum, GLenum, GLfloat *))
GL_EXT(void,glGetHistogramParameteriv,(GLenum, GLenum, GLint *))
GL_EXT(void,glGetMinmax,(GLenum, GLboolean, GLenum, GLenum, GLvoid *))
GL_EXT(void,glGetMinmaxParameterfv,(GLenum, GLenum, GLfloat *))
GL_EXT(void,glGetMinmaxParameteriv,(GLenum, GLenum, GLint *))
GL_EXT(void,glHistogram,(GLenum, GLsizei, GLenum, GLboolean))
GL_EXT(void,glMinmax,(GLenum, GLenum, GLboolean))
GL_EXT(void,glResetHistogram,(GLenum))
GL_EXT(void,glResetMinmax,(GLenum))
GL_EXT(void,glTexImage3D,(GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, const GLvoid *))
GL_EXT(void,glTexSubImage3D,(GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, const GLvoid *))
GL_EXT(void,glCopyTexSubImage3D,(GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei))
#endif</t>
<t tx="ekr.20060513122613.11">#if USE_OPENGL &gt;= 3
	@others
#endif</t>
<t tx="ekr.20060513122613.12">#ifdef GL_DEFS
#define GL_TEXTURE0                       0x84C0
#define GL_TEXTURE1                       0x84C1
#define GL_TEXTURE2                       0x84C2
#define GL_TEXTURE3                       0x84C3
#define GL_TEXTURE4                       0x84C4
#define GL_TEXTURE5                       0x84C5
#define GL_TEXTURE6                       0x84C6
#define GL_TEXTURE7                       0x84C7
#define GL_TEXTURE8                       0x84C8
#define GL_TEXTURE9                       0x84C9
#define GL_TEXTURE10                      0x84CA
#define GL_TEXTURE11                      0x84CB
#define GL_TEXTURE12                      0x84CC
#define GL_TEXTURE13                      0x84CD
#define GL_TEXTURE14                      0x84CE
#define GL_TEXTURE15                      0x84CF
#define GL_TEXTURE16                      0x84D0
#define GL_TEXTURE17                      0x84D1
#define GL_TEXTURE18                      0x84D2
#define GL_TEXTURE19                      0x84D3
#define GL_TEXTURE20                      0x84D4
#define GL_TEXTURE21                      0x84D5
#define GL_TEXTURE22                      0x84D6
#define GL_TEXTURE23                      0x84D7
#define GL_TEXTURE24                      0x84D8
#define GL_TEXTURE25                      0x84D9
#define GL_TEXTURE26                      0x84DA
#define GL_TEXTURE27                      0x84DB
#define GL_TEXTURE28                      0x84DC
#define GL_TEXTURE29                      0x84DD
#define GL_TEXTURE30                      0x84DE
#define GL_TEXTURE31                      0x84DF
#define GL_ACTIVE_TEXTURE                 0x84E0
#define GL_CLIENT_ACTIVE_TEXTURE          0x84E1
#define GL_MAX_TEXTURE_UNITS              0x84E2
#define GL_TRANSPOSE_MODELVIEW_MATRIX     0x84E3
#define GL_TRANSPOSE_PROJECTION_MATRIX    0x84E4
#define GL_TRANSPOSE_TEXTURE_MATRIX       0x84E5
#define GL_TRANSPOSE_COLOR_MATRIX         0x84E6
#define GL_MULTISAMPLE                    0x809D
#define GL_SAMPLE_ALPHA_TO_COVERAGE       0x809E
#define GL_SAMPLE_ALPHA_TO_ONE            0x809F
#define GL_SAMPLE_COVERAGE                0x80A0
#define GL_SAMPLE_BUFFERS                 0x80A8
#define GL_SAMPLES                        0x80A9
#define GL_SAMPLE_COVERAGE_VALUE          0x80AA
#define GL_SAMPLE_COVERAGE_INVERT         0x80AB
#define GL_MULTISAMPLE_BIT                0x20000000
#define GL_NORMAL_MAP                     0x8511
#define GL_REFLECTION_MAP                 0x8512
#define GL_TEXTURE_CUBE_MAP               0x8513
#define GL_TEXTURE_BINDING_CUBE_MAP       0x8514
#define GL_TEXTURE_CUBE_MAP_POSITIVE_X    0x8515
#define GL_TEXTURE_CUBE_MAP_NEGATIVE_X    0x8516
#define GL_TEXTURE_CUBE_MAP_POSITIVE_Y    0x8517
#define GL_TEXTURE_CUBE_MAP_NEGATIVE_Y    0x8518
#define GL_TEXTURE_CUBE_MAP_POSITIVE_Z    0x8519
#define GL_TEXTURE_CUBE_MAP_NEGATIVE_Z    0x851A
#define GL_PROXY_TEXTURE_CUBE_MAP         0x851B
#define GL_MAX_CUBE_MAP_TEXTURE_SIZE      0x851C
#define GL_COMPRESSED_ALPHA               0x84E9
#define GL_COMPRESSED_LUMINANCE           0x84EA
#define GL_COMPRESSED_LUMINANCE_ALPHA     0x84EB
#define GL_COMPRESSED_INTENSITY           0x84EC
#define GL_COMPRESSED_RGB                 0x84ED
#define GL_COMPRESSED_RGBA                0x84EE
#define GL_TEXTURE_COMPRESSION_HINT       0x84EF
#define GL_TEXTURE_COMPRESSED_IMAGE_SIZE  0x86A0
#define GL_TEXTURE_COMPRESSED             0x86A1
#define GL_NUM_COMPRESSED_TEXTURE_FORMATS 0x86A2
#define GL_COMPRESSED_TEXTURE_FORMATS     0x86A3
#define GL_CLAMP_TO_BORDER                0x812D
#define GL_CLAMP_TO_BORDER_SGIS           0x812D
#define GL_COMBINE                        0x8570
#define GL_COMBINE_RGB                    0x8571
#define GL_COMBINE_ALPHA                  0x8572
#define GL_SOURCE0_RGB                    0x8580
#define GL_SOURCE1_RGB                    0x8581
#define GL_SOURCE2_RGB                    0x8582
#define GL_SOURCE0_ALPHA                  0x8588
#define GL_SOURCE1_ALPHA                  0x8589
#define GL_SOURCE2_ALPHA                  0x858A
#define GL_OPERAND0_RGB                   0x8590
#define GL_OPERAND1_RGB                   0x8591
#define GL_OPERAND2_RGB                   0x8592
#define GL_OPERAND0_ALPHA                 0x8598
#define GL_OPERAND1_ALPHA                 0x8599
#define GL_OPERAND2_ALPHA                 0x859A
#define GL_RGB_SCALE                      0x8573
#define GL_ADD_SIGNED                     0x8574
#define GL_INTERPOLATE                    0x8575
#define GL_SUBTRACT                       0x84E7
#define GL_CONSTANT                       0x8576
#define GL_PRIMARY_COLOR                  0x8577
#define GL_PREVIOUS                       0x8578
#define GL_DOT3_RGB                       0x86AE
#define GL_DOT3_RGBA                      0x86AF
#endif
</t>
<t tx="ekr.20060513122613.13">#ifndef GL_DEFS
GL_EXT(void,glActiveTexture,(GLenum))
GL_EXT(void,glClientActiveTexture,(GLenum))
GL_EXT(void,glMultiTexCoord1d,(GLenum,GLdouble))
GL_EXT(void,glMultiTexCoord1dv,(GLenum,const GLdouble *))
GL_EXT(void,glMultiTexCoord1f,(GLenum,GLfloat))
GL_EXT(void,glMultiTexCoord1fv,(GLenum,const GLfloat *))
GL_EXT(void,glMultiTexCoord1i,(GLenum,GLint))
GL_EXT(void,glMultiTexCoord1iv,(GLenum,const GLint*))
GL_EXT(void,glMultiTexCoord1s,(GLenum,GLshort))
GL_EXT(void,glMultiTexCoord1sv,(GLenum,const GLshort*))
GL_EXT(void,glMultiTexCoord2d,(GLenum,GLdouble,GLdouble))
GL_EXT(void,glMultiTexCoord2dv,(GLenum,const GLdouble*))
GL_EXT(void,glMultiTexCoord2f,(GLenum,GLfloat,GLfloat))
GL_EXT(void,glMultiTexCoord2fv,(GLenum,const GLfloat*))
GL_EXT(void,glMultiTexCoord2i,(GLenum,GLint,GLint))
GL_EXT(void,glMultiTexCoord2iv,(GLenum,const GLint*))
GL_EXT(void,glMultiTexCoord2s,(GLenum,GLshort,GLshort))
GL_EXT(void,glMultiTexCoord2sv,(GLenum,const GLshort*))
GL_EXT(void,glMultiTexCoord3d,(GLenum,GLdouble,GLdouble,GLdouble))
GL_EXT(void,glMultiTexCoord3dv,(GLenum,const GLdouble*))
GL_EXT(void,glMultiTexCoord3f,(GLenum,GLfloat,GLfloat,GLfloat))
GL_EXT(void,glMultiTexCoord3fv,(GLenum,const GLfloat*))
GL_EXT(void,glMultiTexCoord3i,(GLenum,GLint,GLint,GLint))
GL_EXT(void,glMultiTexCoord3iv,(GLenum,const GLint*))
GL_EXT(void,glMultiTexCoord3s,(GLenum,GLshort,GLshort,GLshort))
GL_EXT(void,glMultiTexCoord3sv,(GLenum,const GLshort*))
GL_EXT(void,glMultiTexCoord4d,(GLenum,GLdouble,GLdouble,GLdouble,GLdouble))
GL_EXT(void,glMultiTexCoord4dv,(GLenum,const GLdouble *))
GL_EXT(void,glMultiTexCoord4f,(GLenum,GLfloat,GLfloat,GLfloat,GLfloat))
GL_EXT(void,glMultiTexCoord4fv,(GLenum,const GLfloat *))
GL_EXT(void,glMultiTexCoord4i,(GLenum,GLint,GLint,GLint,GLint))
GL_EXT(void,glMultiTexCoord4iv,(GLenum,const GLint *))
GL_EXT(void,glMultiTexCoord4s,(GLenum,GLshort,GLshort,GLshort,GLshort))
GL_EXT(void,glMultiTexCoord4sv,(GLenum,const GLshort *))
GL_EXT(void,glLoadTransposeMatrixf,(const GLfloat *))
GL_EXT(void,glLoadTransposeMatrixd,(const GLdouble *))
GL_EXT(void,glMultTransposeMatrixf,(const GLfloat *))
GL_EXT(void,glMultTransposeMatrixd,(const GLdouble *))
GL_EXT(void,glSampleCoverage,(GLclampf,GLboolean))
GL_EXT(void,glCompressedTexImage3D,(GLenum,GLint,GLenum,GLsizei,GLsizei,GLsizei,GLint,GLsizei,const GLvoid *))
GL_EXT(void,glCompressedTexImage2D,(GLenum,GLint,GLenum,GLsizei,GLsizei,GLint,GLsizei,const GLvoid *))
GL_EXT(void,glCompressedTexImage1D,(GLenum,GLint,GLenum,GLsizei,GLint,GLsizei,const GLvoid *))
GL_EXT(void,glCompressedTexSubImage3D,(GLenum,GLint,GLint,GLint,GLint,GLsizei,GLsizei,GLsizei,GLenum,GLsizei,const GLvoid *))
GL_EXT(void,glCompressedTexSubImage2D,(GLenum,GLint,GLint,GLint,GLsizei,GLsizei,GLenum,GLsizei,const GLvoid *))
GL_EXT(void,glCompressedTexSubImage1D,(GLenum,GLint,GLint,GLsizei,GLenum,GLsizei,const GLvoid *))
GL_EXT(void,glGetCompressedTexImage,(GLenum,GLint,GLvoid *))
#endif</t>
<t tx="ekr.20060513122613.14">#if USE_OPENGL &gt;= 4
	@others
#endif</t>
<t tx="ekr.20060513122613.15">#ifdef GL_DEFS
#define GL_BLEND_DST_RGB                  0x80C8
#define GL_BLEND_SRC_RGB                  0x80C9
#define GL_BLEND_DST_ALPHA                0x80CA
#define GL_BLEND_SRC_ALPHA                0x80CB
#define GL_POINT_SIZE_MIN                 0x8126
#define GL_POINT_SIZE_MAX                 0x8127
#define GL_POINT_FADE_THRESHOLD_SIZE      0x8128
#define GL_POINT_DISTANCE_ATTENUATION     0x8129
#define GL_GENERATE_MIPMAP                0x8191
#define GL_GENERATE_MIPMAP_HINT           0x8192
#define GL_DEPTH_COMPONENT16              0x81A5
#define GL_DEPTH_COMPONENT24              0x81A6
#define GL_DEPTH_COMPONENT32              0x81A7
#define GL_MIRRORED_REPEAT                0x8370
#define GL_FOG_COORDINATE_SOURCE          0x8450
#define GL_FOG_COORDINATE                 0x8451
#define GL_FRAGMENT_DEPTH                 0x8452
#define GL_CURRENT_FOG_COORDINATE         0x8453
#define GL_FOG_COORDINATE_ARRAY_TYPE      0x8454
#define GL_FOG_COORDINATE_ARRAY_STRIDE    0x8455
#define GL_FOG_COORDINATE_ARRAY_POINTER   0x8456
#define GL_FOG_COORDINATE_ARRAY           0x8457
#define GL_COLOR_SUM                      0x8458
#define GL_CURRENT_SECONDARY_COLOR        0x8459
#define GL_SECONDARY_COLOR_ARRAY_SIZE     0x845A
#define GL_SECONDARY_COLOR_ARRAY_TYPE     0x845B
#define GL_SECONDARY_COLOR_ARRAY_STRIDE   0x845C
#define GL_SECONDARY_COLOR_ARRAY_POINTER  0x845D
#define GL_SECONDARY_COLOR_ARRAY          0x845E
#define GL_MAX_TEXTURE_LOD_BIAS           0x84FD
#define GL_TEXTURE_FILTER_CONTROL         0x8500
#define GL_TEXTURE_LOD_BIAS               0x8501
#define GL_INCR_WRAP                      0x8507
#define GL_DECR_WRAP                      0x8508
#define GL_TEXTURE_DEPTH_SIZE             0x884A
#define GL_DEPTH_TEXTURE_MODE             0x884B
#define GL_TEXTURE_COMPARE_MODE           0x884C
#define GL_TEXTURE_COMPARE_FUNC           0x884D
#define GL_COMPARE_R_TO_TEXTURE           0x884E
#endif</t>
<t tx="ekr.20060513122613.16">#ifndef GL_DEFS
GL_EXT(void,glBlendFuncSeparate,(GLenum,GLenum,GLenum,GLenum))
GL_EXT(void,glFogCoordf,(GLfloat))
GL_EXT(void,glFogCoordfv,(const GLfloat *))
GL_EXT(void,glFogCoordd,(GLdouble))
GL_EXT(void,glFogCoorddv,(const GLdouble *))
GL_EXT(void,glFogCoordPointer,(GLenum,GLsizei,const GLvoid *))
GL_EXT(void,glMultiDrawArrays,(GLenum,GLint *,GLsizei *,GLsizei))
GL_EXT(void,glMultiDrawElements,(GLenum,const GLsizei *,GLenum,const GLvoid* *,GLsizei))
GL_EXT(void,glPointParameterf,(GLenum,GLfloat))
GL_EXT(void,glPointParameterfv,(GLenum,const GLfloat *))
GL_EXT(void,glPointParameteri,(GLenum,GLint))
GL_EXT(void,glPointParameteriv,(GLenum,const GLint *))
GL_EXT(void,glSecondaryColor3b,(GLbyte,GLbyte,GLbyte))
GL_EXT(void,glSecondaryColor3bv,(const GLbyte *))
GL_EXT(void,glSecondaryColor3d,(GLdouble,GLdouble,GLdouble))
GL_EXT(void,glSecondaryColor3dv,(const GLdouble *))
GL_EXT(void,glSecondaryColor3f,(GLfloat,GLfloat,GLfloat))
GL_EXT(void,glSecondaryColor3fv,(const GLfloat *))
GL_EXT(void,glSecondaryColor3i,(GLint,GLint,GLint))
GL_EXT(void,glSecondaryColor3iv,(const GLint *))
GL_EXT(void,glSecondaryColor3s,(GLshort,GLshort,GLshort))
GL_EXT(void,glSecondaryColor3sv,(const GLshort *))
GL_EXT(void,glSecondaryColor3ub,(GLubyte,GLubyte,GLubyte))
GL_EXT(void,glSecondaryColor3ubv,(const GLubyte *))
GL_EXT(void,glSecondaryColor3ui,(GLuint,GLuint,GLuint))
GL_EXT(void,glSecondaryColor3uiv,(const GLuint *))
GL_EXT(void,glSecondaryColor3us,(GLushort,GLushort,GLushort))
GL_EXT(void,glSecondaryColor3usv,(const GLushort *))
GL_EXT(void,glSecondaryColorPointer,(GLint,GLenum,GLsizei,const GLvoid *))
GL_EXT(void,glWindowPos2d,(GLdouble,GLdouble))
GL_EXT(void,glWindowPos2dv,(const GLdouble *))
GL_EXT(void,glWindowPos2f,(GLfloat,GLfloat))
GL_EXT(void,glWindowPos2fv,(const GLfloat *))
GL_EXT(void,glWindowPos2i,(GLint,GLint))
GL_EXT(void,glWindowPos2iv,(const GLint *))
GL_EXT(void,glWindowPos2s,(GLshort,GLshort))
GL_EXT(void,glWindowPos2sv,(const GLshort *))
GL_EXT(void,glWindowPos3d,(GLdouble,GLdouble,GLdouble))
GL_EXT(void,glWindowPos3dv,(const GLdouble *))
GL_EXT(void,glWindowPos3f,(GLfloat,GLfloat,GLfloat))
GL_EXT(void,glWindowPos3fv,(const GLfloat *))
GL_EXT(void,glWindowPos3i,(GLint,GLint,GLint))
GL_EXT(void,glWindowPos3iv,(const GLint *))
GL_EXT(void,glWindowPos3s,(GLshort,GLshort,GLshort))
GL_EXT(void,glWindowPos3sv,(const GLshort *))
#endif</t>
<t tx="ekr.20060513122613.17">#if USE_OPENGL &gt;= 5
	@others
#endif</t>
<t tx="ekr.20060513122613.18">#ifdef GL_DEFS
#define GL_BUFFER_SIZE                    0x8764
#define GL_BUFFER_USAGE                   0x8765
#define GL_QUERY_COUNTER_BITS             0x8864
#define GL_CURRENT_QUERY                  0x8865
#define GL_QUERY_RESULT                   0x8866
#define GL_QUERY_RESULT_AVAILABLE         0x8867
#define GL_ARRAY_BUFFER                   0x8892
#define GL_ELEMENT_ARRAY_BUFFER           0x8893
#define GL_ARRAY_BUFFER_BINDING           0x8894
#define GL_ELEMENT_ARRAY_BUFFER_BINDING   0x8895
#define GL_VERTEX_ARRAY_BUFFER_BINDING    0x8896
#define GL_NORMAL_ARRAY_BUFFER_BINDING    0x8897
#define GL_COLOR_ARRAY_BUFFER_BINDING     0x8898
#define GL_INDEX_ARRAY_BUFFER_BINDING     0x8899
#define GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING 0x889A
#define GL_EDGE_FLAG_ARRAY_BUFFER_BINDING 0x889B
#define GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING 0x889C
#define GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING 0x889D
#define GL_WEIGHT_ARRAY_BUFFER_BINDING    0x889E
#define GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING 0x889F
#define GL_READ_ONLY                      0x88B8
#define GL_WRITE_ONLY                     0x88B9
#define GL_READ_WRITE                     0x88BA
#define GL_BUFFER_ACCESS                  0x88BB
#define GL_BUFFER_MAPPED                  0x88BC
#define GL_BUFFER_MAP_POINTER             0x88BD
#define GL_STREAM_DRAW                    0x88E0
#define GL_STREAM_READ                    0x88E1
#define GL_STREAM_COPY                    0x88E2
#define GL_STATIC_DRAW                    0x88E4
#define GL_STATIC_READ                    0x88E5
#define GL_STATIC_COPY                    0x88E6
#define GL_DYNAMIC_DRAW                   0x88E8
#define GL_DYNAMIC_READ                   0x88E9
#define GL_DYNAMIC_COPY                   0x88EA
#define GL_SAMPLES_PASSED                 0x8914
#define GL_FOG_COORD_SOURCE               GL_FOG_COORDINATE_SOURCE
#define GL_FOG_COORD                      GL_FOG_COORDINATE
#define GL_CURRENT_FOG_COORD              GL_CURRENT_FOG_COORDINATE
#define GL_FOG_COORD_ARRAY_TYPE           GL_FOG_COORDINATE_ARRAY_TYPE
#define GL_FOG_COORD_ARRAY_STRIDE         GL_FOG_COORDINATE_ARRAY_STRIDE
#define GL_FOG_COORD_ARRAY_POINTER        GL_FOG_COORDINATE_ARRAY_POINTER
#define GL_FOG_COORD_ARRAY                GL_FOG_COORDINATE_ARRAY
#define GL_FOG_COORD_ARRAY_BUFFER_BINDING GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING
#define GL_SRC0_RGB                       GL_SOURCE0_RGB
#define GL_SRC1_RGB                       GL_SOURCE1_RGB
#define GL_SRC2_RGB                       GL_SOURCE2_RGB
#define GL_SRC0_ALPHA                     GL_SOURCE0_ALPHA
#define GL_SRC1_ALPHA                     GL_SOURCE1_ALPHA
#define GL_SRC2_ALPHA                     GL_SOURCE2_ALPHA
#endif</t>
<t tx="ekr.20060513122613.19">#ifndef GL_DEFS
GL_EXT(void,glGenQueries,(GLsizei,GLuint *))
GL_EXT(void,glDeleteQueries,(GLsizei,const GLuint *))
GL_EXT(GLboolean,glIsQuery,(GLuint))
GL_EXT(void,glBeginQuery,(GLenum,GLuint))
GL_EXT(void,glEndQuery,(GLenum))
GL_EXT(void,glGetQueryiv,(GLenum,GLenum,GLint *))
GL_EXT(void,glGetQueryObjectiv,(GLuint,GLenum,GLint *))
GL_EXT(void,glGetQueryObjectuiv,(GLuint,GLenum,GLuint *))
GL_EXT(void,glBindBuffer,(GLenum,GLuint))
GL_EXT(void,glDeleteBuffers,(GLsizei,const GLuint *))
GL_EXT(void,glGenBuffers,(GLsizei,GLuint *))
GL_EXT(GLboolean,glIsBuffer,(GLuint))
GL_EXT(void,glBufferData,(GLenum,GLsizeiptr,const GLvoid *,GLenum))
GL_EXT(void,glBufferSubData,(GLenum,GLintptr,GLsizeiptr,const GLvoid *))
GL_EXT(void,glGetBufferSubData,(GLenum,GLintptr,GLsizeiptr,GLvoid *))
GL_EXT(GLvoid*,glMapBuffer,(GLenum,GLenum))
GL_EXT(GLboolean,glUnmapBuffer,(GLenum))
GL_EXT(void,glGetBufferParameteriv,(GLenum,GLenum,GLint *))
GL_EXT(void,glGetBufferPointerv,(GLenum,GLenum,GLvoid* *))
#endif</t>
<t tx="ekr.20060513122613.20">#ifndef GL_DEFS
WGL_PROC(BOOL,wglCopyContext,(HGLRC,HGLRC,UINT))
WGL_PROC(HGLRC,wglCreateContext,(HDC))
WGL_PROC(HGLRC,wglCreateLayerContext,(HDC,int))
WGL_PROC(BOOL,wglDeleteContext,(HGLRC))
WGL_PROC(HGLRC,wglGetCurrentContext,(VOID))
WGL_PROC(HDC,wglGetCurrentDC,(VOID))
WGL_PROC(PROC,wglGetProcAddress,(LPCSTR))
WGL_PROC(BOOL,wglMakeCurrent,(HDC,HGLRC))
WGL_PROC(BOOL,wglShareLists,(HGLRC,HGLRC))
WGL_PROC(BOOL,wglUseFontBitmapsA,(HDC,DWORD,DWORD,DWORD))
WGL_PROC(BOOL,wglUseFontBitmapsW,(HDC,DWORD,DWORD,DWORD))
WGL_PROC(BOOL,wglSwapBuffers,(HDC))
WGL_PROC(BOOL,wglUseFontOutlinesA,(HDC,DWORD,DWORD,DWORD,FLOAT,FLOAT,int,LPGLYPHMETRICSFLOAT))
WGL_PROC(BOOL,wglUseFontOutlinesW,(HDC,DWORD,DWORD,DWORD,FLOAT,FLOAT,int,LPGLYPHMETRICSFLOAT))
WGL_PROC(BOOL,wglDescribeLayerPlane,(HDC,int,int,UINT,LPLAYERPLANEDESCRIPTOR))
WGL_PROC(int,wglSetLayerPaletteEntries,(HDC,int,int,int,CONST COLORREF *))
WGL_PROC(int,wglGetLayerPaletteEntries,(HDC,int,int,int,COLORREF *))
WGL_PROC(BOOL,wglRealizeLayerPalette,(HDC,int,BOOL))
WGL_PROC(BOOL,wglSwapLayerBuffers,(HDC,UINT))
#if (WINVER &gt;= 0x0500)
	WGL_PROC(DWORD,SwapMultipleBuffers,(UINT,CONST WGLSWAP *))
#endif
#endif
</t>
<t tx="ekr.20060513122613.21">@language c++
</t>
<t tx="ekr.20060513122613.22"></t>
<t tx="ekr.20060513122613.23">#define WIN32_LEAN_AND_MEAN
#include &lt;windows.h&gt; // the main windows headers
#include &lt;windowsx.h&gt; // a lot of cool macros</t>
<t tx="ekr.20060513122613.24">char* a ="allo";
// call message box api with NULL for parent window handle
MessageBox(NULL, "THERE CAN BE ONLY ONE!!!",
"MY FIRST WINDOWS PROGRAM",
MB_OK | MB_ICONEXCLAMATION);
a="salut";
a="jean";
a="pierre";
a="pierre";
// exit program
return(0);

</t>
<t tx="ekr.20060513122613.25">@language c++
</t>
<t tx="ekr.20060513123144">def init ():
    
    data = (
        (("new","open2"), OnCreate),
        # ("start2",      OnStart2),
        ("select2",     OnSelect2),
        ("idle",        OnIdle),
        ("command2",    OnCommand2),
        ("bodydclick2", OnBodyDoubleClick),
        ("bodykey2",    OnBodyKey2),
        ("headkey2",    OnHeadKey2),
        ("end1",        OnQuit),
    )
    
    for hook,f in data:
        leoPlugins.registerHandler(hook,f)

    g.plugin_signon(__name__)

    return True


</t>
<t tx="ekr.20060513141418">class controllerClass:

    @others</t>
<t tx="ekr.20060513142641"></t>
<t tx="ekr.20060513142641.1"></t>
<t tx="ekr.20060513142641.2">def __init__ (self,c):
    
    self.c = c
    
    @others
    g.enableIdleTimeHook(idleTimeDelay=100)</t>
<t tx="ekr.20060513152023"></t>
<t tx="ekr.20060513152032.3">def onSelect(self):    
    cc = self
    p = cc.c.currentPosition()
    
    if IsXcc(p):
        cc.cSelect()
        cc.sSelect(p)        
    else:
        p2 = GetXccNode(p)
        if p2:
            if p2 != cc.SELECTED_NODE:
                cc.sSelect(p2)
            cc.cSelect(p)			
        else:
            cc.cSelect()
            cc.sSelect()
            </t>
<t tx="ekr.20060513152032.4">def onIdle(self):

    cc = self
    cc.UpdateProcess()
    cc.BreakBar.IdleUpdate()</t>
<t tx="ekr.20060513152032.5">def onCommand2(self,keywords):
    cc = self
    label = keywords.get("label")
    if label in ["undo","redo","backward-delete-char","delete-char","cut-text","paste-text"]:
        if cc.SELECTED_NODE:
            cc.BreakBar.bodychanged = True</t>
<t tx="ekr.20060513152032.6">def onBodyDoubleClick(self):

    cc = self

    if cc.SELECTED_NODE == cc.c.currentPosition():
        cc.sGoToError()</t>
<t tx="ekr.20060513152032.7">def onBodyKey2(self,keywords):   
    cc = self
    ch = keywords.get("ch")    
    
    cc.LeoBodyText.tag_delete("xcc_error")
        
    if cc.CHILD_NODE and ch == "\n":
        cc.BreakBar.BreaksFromTags()</t>
<t tx="ekr.20060513152032.8">def onHeadKey2(self,keywords):    
    cc = self
    p = cc.c.currentPosition()
    
    if IsXcc(p):
        
        if cc.c.openDirectory == None:
            p.setHeadString(p.headString()[1:])
            Error("xcc: ","Must save Leo file before using xcc node!")
            return
        
        
        if not cc.SELECTED_NODE:
            cc.sSelect(p)
        
        if cc.sGet("INITED","False") == "False":
            cc.sInitDict()
        
        cc.sGetBrowseInfo()
    else:
        p2 = GetXccNode(p)
        if p2:
            cc.sSelect(p2)
            cc.cSelect(p)
            
        #    try:
        #        cc.ParseTree()
        #        cc.c.redraw()
        #    except:
        #        TraceBack();
        #cc.sSelect(p2)
            #cc.cSelect(p)</t>
<t tx="ekr.20060513152032.9">def onQuit(self):    
    cc = self
  
    if cc.ACTIVE_NODE:
        cc.GoToNode(cc.ACTIVE_NODE)
        cc.aStop()
        while cc.ACTIVE_NODE:
            cc.UpdateProcess()</t>
<t tx="ekr.20060513153648"></t>
<t tx="ekr.20060513160819">def pause (pid):
    
    if os.name == "nt":
        winPause(pid)
    else:
        linPause(pid)</t>
<t tx="ekr.20060513183934">@nocolor
@

v 0.1: Alexis Gendron Paquette. - web &amp; graphics: Felix Malboeuf

v 0.2 EKR:
- Add per-node controller class.  This required many changes.
- Many stylistic changes.  More are coming.

v 0.3 EKR:
- Fixed a large number of crashers due to the reorganized code.
- The major panels now appear to work.

v 0.4 EKR:
- Added a ``what I did`` section.
- Made UpdateProcess a cc method.
- It appears that cc.OPTS is not set properly in PageClass.LoadObjects.
  This prevents the compiler from working.
v 0.5 AGP:
- Asserted compatibility with leo 4.4.2.1 final
- Many bug fix and improvement regarding line numbers and scroll system.
- Added Language pane allowing to configure the node for almost any language.
- Added a tool launch sequencer in the option pane.
- Added a Xcmd toggleable pane.
- Began basic Linux testing, major problem reside in the use of "\" wich worked in win32 wherea linux seem to require "/". Since window use both, the solution is to always use "/".
- Lot of other improvement.</t>
<t tx="ekr.20060513225814">def __init__ (self,Parser):    
    self.Parser = Parser</t>
<t tx="ekr.20060513225814.1">def __init__ (self,Parser):    
    self.Parser = Parser</t>
<t tx="ekr.20060513225814.2">def __init__ (self,Parser):    
    self.Parser = Parser</t>
<t tx="ekr.20060514121335">@nocolor
@

**Important**: I have spent 8 or more hours making the following changes.
Without doubt I have introduced some bugs while doing so. However, it was
important to make these changes, for the following reasons:

1. This is very important code, and deserves the best packaging.

2. This code may form the basis of a Python-oriented debugger, so I wanted
   to make the code base as solid as possible.

3. Working and debugging code is the best way for me to really understand it.

Here is what I have done in detail:

- Eliminated * imports:
    ``* imports`` are bad style in complex code.
    Replaced ``from leoPlugins import *`` by ``import leoPlugins``
    Replaced ``from leoGlobals import *`` by ``import leoGlobals as g``
    Replaced ``from Tkinter import *`` by import Tkinter as Tk.
        Replaced Tk constants like END, FLAT, NW, etc. by 'end','flat','nw', etc.

- Created the module-level init function that registers all hooks.
  This is the recommended style: it shows in one place where all the hooks are.

- Removed most try/except handling.
    - Such handling is *usually* unnecessary, especially since Leo does a good job
      of recovering from crashes. However, try/except blocks might be important
      when executing user code, so perhaps it will be necessary to put some back in.
    - Replaced ``x = aDict[key]`` by ``x = aDict.get(key)`` to avoid exceptions.

*** Eliminated *all* global variables (except commanders) as follows:

- Created per-commander controller class instances.
    - The controllers dictionary is the only global variable.
    - The new OnCreate event handler creates controller instances.
    - Replaced all global variables by ivars of the controller class.
    - Global constants still exist.
    - Most former global functions now are methods of the controller class.
    - By convention, cc refers to the proper controller, i.e., the controller for the proper commander c.
    - cc gets passed to the constructor of almost all classes.
    - Replaced init logic (start2 hook) by logic in the ctor for the controller class.

- Simplified module-level event handlers.
    - They simply call the corresponding event handler in the proper controller instance.

- Renamed most classes from XXX to XxxClass.

- Eliminated the Parser global.
    - All Rule classes now get a Parser argument and define self.Parser.

- Disabled some weird code in OnIdle.  I'm not sure what this is supposed to do.

- Create a new pause module-level function that calls winPause or linPause as appropriate.

- Used more Pythonic or Leonic ideoms in many places:
    - Replaced ``if x == True:`` by ``if x:``.
    - Replaced ``if x == False:`` by ``if not x:``.
    - Replaced ``if x != '':`` by ``if not x:``
    etc.
    *** Warning: these simplifications might cause problems.
        For example, the re module uses None as a sentinal, and can also return 0,
        so tests like ``if result:`` are not correct in such cases.  I have tried
        not to simplify the code "too much" but I may have made mistakes.
    *** if p is a node, ``if p == None:`` *must* be replaced by ``if not p:``.
    - cc.VERBOSE and cc.FILTER_OUTPUT now have values True/False instead of 'true'/'false'.
    - Defined TraceBack as g.es_exception.
    - Changed ``Error(x) ; return`` to ``return Error(x)``, and similarly for Warning, etc.

- Simplified the code wherever possible.
    - Sometimes the change can be dramatic, as in cc.cGetDict.

* There does not seem to be any definition of ExtractLines.</t>
<t tx="ekr.20060514122829"></t>
<t tx="ekr.20060514125256"></t>
<t tx="ekr.20060530091119"></t>
<t tx="ekr.20060530091119.2"></t>
<t tx="ekr.20060623075925.1">@nocolor

- Rewrite recolor_all to handle images.</t>
<t tx="ekr.20060629124102">@nocolor

Cleanup:
    
- tkBody has two methods: getSelectedText and getTextSelection.
  Eliminate one of them!
  
- Eliminate the component classes??
  

- Important:
    
- Add minibuffer widget.</t>
<t tx="ekr.20060703162826"></t>
<t tx="ekr.20060715100156"></t>
<t tx="ekr.20060715100156.1"></t>
<t tx="ekr.20060715100156.2">@color

import leoTest

print "\nStart of Do @test"
leoTest.doTests(c,all=False)
print "End of Do @test"</t>
<t tx="ekr.20060715100156.3">@doc
This is the most complicated part of the plugin, and needs most testing.

All the tags should be tested at least once (equal, replace, delete, insert).

The replace, delete, insert operations should happen at least once:
    1. At the beginning of a node.
    2. In the middle of a node.
    3. At the end of a node.
    

For the delete and replace operators we must also test the case that the
deletion or replacement spans more than one block.</t>
<t tx="ekr.20060715100156.4">import mod_shadow
reload(mod_shadow)
mod_shadow.do_test_propagate_changes_Leo(c)
</t>
<t tx="ekr.20060715100156.5">#@string1
line 1
line 2
</t>
<t tx="ekr.20060715100156.6">#@string2
xxx
</t>
<t tx="ekr.20060715100156.7">xxx
</t>
<t tx="ekr.20060816094306"></t>
<t tx="ekr.20060827163237">name = "scripts.leo"
fileName = g.os_path_join(g.app.loadDir,"..","scripts",name)
ok,frame = g.openWithFileName(fileName,c)
if not ok:
    g.es("not found: %s" % name)</t>
<t tx="ekr.20060924180348"></t>
<t tx="ekr.20061023141459"></t>
<t tx="ekr.20061023141638"></t>
<t tx="ekr.20061023142737"></t>
<t tx="ekr.20061023142737.1"></t>
<t tx="rogererens.20041014110709">@

How about other plugins that create a status line? Should I test whether the status line is already created?

Don't know exactly yet about the interaction with other plugins. The info in the status line may be overwritten by them. That's fine with me: I can always click on the icon of the node again to show the info again.

Keep the pane of the UNL referred to on top (now the pane with the referring node stays on top).
Maybe this should be a settings-dependent behaviour. Could this be solved by using the 'onCreate' idiom and a UNLclass?

Find out about the difference between the event 'select2' and 'select3'.

A UNL checker script would be handy to check whether all references are still valid.

Deal with path-separators for various platforms?

Handle relative paths?

Introduce a menu item to improve documentation? By firing up a browser, directing it to leo on sourceforge (sourceforge userid needed?). EKR could start up a new thread beforehand, "documentation improvements", where a new message might be posted with the relevant UNL placed automatically in the text box. Then the user just needs to type in his/her comments and post the message.</t>
<t tx="rogererens.20041130095659">@ It is possible to link to nodes within the same file.  However clones might be better.
</t>
</tnodes>
</leo_file>
