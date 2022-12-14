from django.urls import path
from . import views
urlpatterns = [

    path('main/firstsemester/', views.firstsemester, name="firstsemester"),
    
    path('main/firstsemester/GMA/AGMA3', views.AGMA3, name="AGMA3"),
    
    path('main/firstsemester/GMA/AMGA3/AGrammar3', views.AGrammer3, name='AGrammar3'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar31M/AGrammar31', views.AGrammer31, name='AGrammar31'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar31M/AGrammar31E/<int:number>', views.AGrammar31E,name='AGrammar31E'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar31M', views.AGrammar31M, name='AGrammar31M'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar34M', views.AGrammar34M, name='AGrammar34M'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar34M/AGrammar34Add', views.AGrammar34Add, name='AGrammar34Add'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar34M/AGrammar34E/<int:number>', views.AGrammar34E,name='AGrammar34E'),
    path('main/firstsemester/GMA/AMGA3/AGrammar3/AGrammar34M/AGrammar34/<int:number>', views.AGrammar34, name='AGrammar34'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3', views.AMorphology3, name='AMorphology3'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology31M/AMorphology31', views.AMorphology31, name='AMorphology31'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology31M/AMorphology31E/<int:number>', views.AMorphology31E,name='AMorphology31E'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology31M', views.AMorphology31M, name='AMorphology31M'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology34M', views.AMorphology34M, name='AMorphology34M'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology34M/AMorphology34Add', views.AMorphology34Add,name='AMorphology34Add'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology34M/AMorphology34E/<int:number>', views.AMorphology34E,name='AMorphology34E'),
    path('main/firstsemester/GMA/AMGA3/AMorphology3/AMorphology34M/AMorphology34/<int:number>', views.AMorphology34,name='AMorphology34'),
    path('main/firstsemester/GMA/AMGA3/AGMA3GoldenM', views.AGMA3GoldenM, name='AGMA3GoldenM'),
    path('main/firstsemester/GMA/AMGA3/AGMA3GoldenM/AGMA3Golden', views.AGMA3Golden, name='AGMA3Golden'),
    path('main/firstsemester/GMA/AMGA3/AGMA3GoldenM/AGMA3GoldenAdd', views.AGMA3GoldenAdd, name='AGMA3GoldenAdd'),
    path('main/firstsemester/GMA/AMGA3/AGMA3GoldenM/AGMA3GoldenE', views.AGMA3GoldenE, name='AGMA3GoldenE'),
    path('main/firstsemester/GMA/AMGA3/AGMA3PriveosS', views.AGMA3PriveosS, name='AGMA3PriveosS'),
    path('main/firstsemester/GMA/AMGA3/AGMA3PriveosS/AGMA3PriveosAdd', views.AGMA3PriveosAdd, name='AGMA3PriveosAdd'),
    path('main/firstsemester/GMA/AMGA3/AGMA3PriveosS/AGMA3PriveosM/<int:ExNo>/<int:semestery>', views.AGMA3PriveosM,name='AGMA3PriveosM'),
    path('main/firstsemester/GMA/AMGA3/AGMA3PriveosS/AGMA3Priveos/<int:ExNo>/<int:semestery>', views.AGMA3Priveos,name='AGMA3Priveos'),

    path('main/firstsemester/QuranSciences/', views.QuranSciences, name="QuranSciences"),
    path('main/firstsemester/QuranSciences/AQuranSciencesM/AQuranSciences', views.AQuranSciences, name='AQuranSciences'),
    path('main/firstsemester/QuranSciences/AQuranSciencesM/AQuranSciencesE/<int:number>', views.AQuranSciencesE,name='AQuranSciencesE'),
    path('main/firstsemester/QuranSciences/AQuranSciencesM', views.AQuranSciencesM, name='AQuranSciencesM'),
    path('main/firstsemester/QuranSciences/HQuranSciencesM/HQuranSciences', views.HQuranSciences, name='HQuranSciences'),
    path('main/firstsemester/QuranSciences/HQuranSciencesM/HQuranSciencesE/<int:number>', views.HQuranSciencesE,name='HQuranSciencesE'),
    path('main/firstsemester/QuranSciences/HQuranSciencesM', views.HQuranSciencesM, name='HQuranSciencesM'),
    path('main/firstsemester/QuranSciences/MaryamM/Maryam', views.Maryam, name='Maryam'),
    path('main/firstsemester/QuranSciences/MaryamM/MaryamE/<int:number>', views.MaryamE,name='MaryamE'),
    path('main/firstsemester/QuranSciences/MaryamM', views.MaryamM, name='MaryamM'),
    path('main/firstsemester/QuranSciences/AMMM/AMM', views.AMM, name='AMM'),
    path('main/firstsemester/QuranSciences/AMMM/AMME/<int:number>', views.AMME,name='AMME'),
    path('main/firstsemester/QuranSciences/AMMM', views.AMMM, name='AMMM'),
    path('main/firstsemester/QuranSciences/QuranSciencesGM/QuranSciencesG', views.QuranSciencesG, name='QuranSciencesG'),
    path('main/firstsemester/QuranSciences/QuranSciencesGM/QuranSciencesGE', views.QuranSciencesGE,name='QuranSciencesGE'),
    path('main/firstsemester/QuranSciences/QuranSciencesGM', views.QuranSciencesGM, name='QuranSciencesGM'),
    path('main/firstsemester/QuranSciences/QuranSciencesPM', views.QuranSciencesPM, name="QuranSciencesPM"),
    path('main/firstsemester/QuranSciences/QuranSciencesPM/QuranSciencesP', views.QuranSciencesP, name="QuranSciencesP"),
    path('main/firstsemester/QuranSciences/QuranSciencesPM/QuranSciencesPE/<int:pyear>/<int:number>', views.QuranSciencesPE,name="QuranSciencesPE"),

    path('main/firstsemester/IslamicLiterature/', views.IslamicLiterature, name="IslamicLiterature"),
    path('main/firstsemester/IslamicLiterature/AIslamicLiteratureM/AIslamicLiterature', views.AIslamicLiterature,name='AIslamicLiterature'),
    path('main/firstsemester/IslamicLiterature/AIslamicLiteratureM/AIslamicLiteratureE/<int:number>', views.AIslamicLiteratureE,name='AIslamicLiteratureE'),
    path('main/firstsemester/IslamicLiterature/AIslamicLiteratureM', views.AIslamicLiteratureM, name='AIslamicLiteratureM'),
    path('main/firstsemester/IslamicLiterature/HIslamicLiteratureM/HIslamicLiterature', views.HIslamicLiterature,name='HIslamicLiterature'),
    path('main/firstsemester/IslamicLiterature/HIslamicLiteratureM/HIslamicLiteratureE/<int:number>', views.HIslamicLiteratureE,name='HIslamicLiteratureE'),
    path('main/firstsemester/IslamicLiterature/HIslamicLiteratureM', views.HIslamicLiteratureM, name='HIslamicLiteratureM'),
    path('main/firstsemester/IslamicLiterature/IslamicLiteratureGM/IslamicLiteratureG', views.IslamicLiteratureG, name='IslamicLiteratureG'),
    path('main/firstsemester/IslamicLiterature/IslamicLiteratureGM/IslamicLiteratureGE', views.IslamicLiteratureGE,name='IslamicLiteratureGE'),
    path('main/firstsemester/IslamicLiterature/IslamicLiteratureGM', views.IslamicLiteratureGM, name='IslamicLiteratureGM'),
    path('main/firstsemester/IslamicLiterature/IslamicLiteraturePM', views.IslamicLiteraturePM, name="IslamicLiteraturePM"),
    path('main/firstsemester/IslamicLiterature/IslamicLiteraturePM/IslamicLiteratureP', views.IslamicLiteratureP, name="IslamicLiteratureP"),
    path('main/firstsemester/IslamicLiterature/IslamicLiteraturePM/IslamicLiteraturePE/<int:pyear>/<int:number>', views.IslamicLiteraturePE,name="IslamicLiteraturePE"),

    path('main/firstsemester/Semantics', views.Semantics, name='Semantics'),
    path('main/firstsemester/Semantics/WSemantics', views.WSemantics, name='WSemantics'),
    path('main/firstsemester/Semantics/WSemantics/WPSemanticsM', views.WPSemanticsM, name='WPSemanticsM'),
    path('main/firstsemester/Semantics/WSemantics/WPSemanticsM/WPSemantics', views.WPSemantics, name='WPSemantics'),
    path('main/firstsemester/Semantics/WSemantics/WPSemanticsM/WPSemantics/<int:number>', views.WPSemanticsE, name='WPSemanticsE'),
    path('main/firstsemester/Semantics/WSemantics/WTSemanticsM', views.WTSemanticsM, name='WTSemanticsM'),
    path('main/firstsemester/Semantics/WSemantics/WTSemanticsM/WTSemantics', views.WTSemantics, name='WTSemantics'),
    path('main/firstsemester/Semantics/WSemantics/WTSemanticsM/WTSemantics/<int:number>', views.WTSemanticsE, name='WTSemanticsE'),
    path('main/firstsemester/Semantics/WSemantics/WGSemanticsM', views.WGSemanticsM, name="WGSemanticsM"),
    path('main/firstsemester/Semantics/WSemantics/WGSemanticsM/WGSemantics', views.WGSemantics, name="WGSemantics"),
    path('main/firstsemester/Semantics/WSemantics/WGSemanticsM/WGSemanticsE', views.WGSemanticsE, name="WGSemanticsE"),
    path('main/firstsemester/Semantics/WSemantics/WPPSemanticsM', views.WPPSemanticsM, name="WPPSemanticsM"),
    path('main/firstsemester/Semantics/WSemantics/WPPSemanticsM/WPPSemantics', views.WPPSemantics, name="WPPSemantics"),
    path('main/firstsemester/Semantics/WSemantics/WPPSemanticsM/WPPSemanticsE/<int:pyear>/<int:number>', views.WPPSemanticsE,name="WPPSemanticsE"),
    path('main/firstsemester/Semantics/ASemantics', views.ASemantics, name='ASemantics'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics', views.ATSemantics, name='ATSemantics'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics1M/ATSemantics1', views.ATSemantics1, name='ATSemantics1'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics1M/ATSemantics1E/<int:number>', views.ATSemantics1E,name='ATSemantics1E'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics1M', views.ATSemantics1M, name='ATSemantics1M'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics4M', views.ATSemantics4M, name='ATSemantics4M'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics4M/ATSemantics4Add', views.ATSemantics4Add, name='ATSemantics4Add'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics4M/ATSemantics4E/<int:number>', views.ATSemantics4E,name='ATSemantics4E'),
    path('main/firstsemester/Semantics/ASemantics/ATSemantics/ATSemantics4M/ATSemantics4/<int:number>', views.ATSemantics4, name='ATSemantics4'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics', views.APSemantics, name='APSemantics'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics1M/APSemantics1', views.APSemantics1, name='APSemantics1'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics1M/APSemantics1E/<int:number>', views.APSemantics1E,name='APSemantics1E'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics1M', views.APSemantics1M, name='APSemantics1M'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics4M', views.APSemantics4M, name='APSemantics4M'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics4M/APSemantics4Add', views.APSemantics4Add,name='APSemantics4Add'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics4M/APSemantics4E/<int:number>', views.APSemantics4E,name='APSemantics4E'),
    path('main/firstsemester/Semantics/ASemantics/APSemantics/APSemantics4M/APSemantics4/<int:number>', views.APSemantics4,name='APSemantics4'),
    path('main/firstsemester/Semantics/ASemantics/AGSemanticsM', views.AGSemanticsM, name='AGSemanticsM'),
    path('main/firstsemester/Semantics/ASemantics/AGSemanticsM/AGSemantics', views.AGSemantics, name='AGSemantics'),
    path('main/firstsemester/Semantics/ASemantics/AGSemanticsM/AGSemanticsAdd', views.AGSemanticsAdd, name='AGSemanticsAdd'),
    path('main/firstsemester/Semantics/ASemantics/AGSemanticsM/AGSemanticsE', views.AGSemanticsE, name='AGSemanticsE'),
    path('main/firstsemester/Semantics/ASemantics/APPSemanticsS', views.APPSemanticsS, name='APPSemanticsS'),
    path('main/firstsemester/Semantics/ASemantics/APPSemanticsS/APPSemanticsAdd', views.APPSemanticsAdd, name='APPSemanticsAdd'),
    path('main/firstsemester/Semantics/ASemantics/APPSemanticsS/APPSemanticsM/<int:ExNo>/<int:semestery>', views.APPSemanticsM,name='APPSemanticsM'),
    path('main/firstsemester/Semantics/ASemantics/APPSemanticsS/APPSemantics/<int:ExNo>/<int:semestery>', views.APPSemantics,name='APPSemantics'),
    
    path('main/firstsemester/E3/AE3', views.AEn3, name='AEn3'),
    path('main/firstsemester/E3/AE3/AEn31M/AEn31', views.AEn31, name='AEn31'),
    path('main/firstsemester/E3/AE3/AEn31M/AEn31E/<int:number>', views.AEn31E, name='AEn31E'),
    path('main/firstsemester/E3/AE3/En31M', views.AEn31M, name='AEn31M'),
    path('main/firstsemester/E3/AE3/AEn34M', views.AEn34M, name='AEn34M'),
    path('main/firstsemester/E3/AE3/AEn34M/AEn34Add', views.AEn34Add,name='AEn34Add'),
    path('main/firstsemester/E3/AE3/AEn34M/AEn34E/<int:number>', views.AEn34E,name='AEn34E'),
    path('main/firstsemester/E3/AE3/AEn34M/AEn34/<int:number>', views.AEn34,name='AEn34'),
    path('main/firstsemester/E3/AE3/AEn3PS', views.AEn3PS, name='AEn3PS'),
    path('main/firstsemester/E3/AE3/AEn3PS/AEn3PAdd', views.AEn3PAdd, name='AEn3PAdd'),
    path('main/firstsemester/E3/AE3/AEn3PS/AEn3PM/<int:ExNo>/<int:semestery>', views.AEn3PM, name='AEn3PM'),
    path('main/firstsemester/E3/AE3/AEn3PS/AEn3P/<int:ExNo>/<int:semestery>', views.AEn3P, name='AEn3P'),

    path('main/firstsemester/PersianM/Persian', views.Persian, name='Persian'),
    path('main/firstsemester/PersianM/PersianE/<int:number>', views.PersianE, name='PersianE'),
    path('main/firstsemester/PersianM', views.PersianM, name='PersianM'),
    
    path('main/firstsemester/History2/AHistory2', views.AHistory2, name='AHistory2'),
    path('main/firstsemester/History2/AHistory2/AHistory21M/AHistory21', views.AHistory21, name='AHistory21'),
    path('main/firstsemester/History2/AHistory2/AHistory21M/AHistory21E/<int:number>', views.AHistory21E, name='AHistory21E'),
    path('main/firstsemester/History2/AHistory2/History21M', views.AHistory21M, name='AHistory21M'),
    path('main/firstsemester/History2/AHistory2/AHistory24M', views.AHistory24M, name='AHistory24M'),
    path('main/firstsemester/History2/AHistory2/AHistory24M/AHistory24Add', views.AHistory24Add,name='AHistory24Add'),
    path('main/firstsemester/History2/AHistory2/AHistory24M/AHistory24E/<int:number>', views.AHistory24E,name='AHistory24E'),
    path('main/firstsemester/History2/AHistory2/AHistory24M/AHistory24/<int:number>', views.AHistory24,name='AHistory24'),
    path('main/firstsemester/History2/AHistory2/AHistory2GM', views.AHistory2GM, name='AHistory2GM'),
    path('main/firstsemester/History2/AHistory2/AHistory2GM/AHistory2G', views.AHistory2G, name='AHistory2G'),
    path('main/firstsemester/History2/AHistory2/AHistory2GM/AHistory2GE', views.AHistory2GE, name='AHistory2GE'),
    path('main/firstsemester/History2/AHistory2/AHistory2GM/AHistory2GAdd', views.AHistory2GAdd, name='AHistory2GAdd'),
    path('main/firstsemester/History2/AHistory2/AHistory2PS', views.AHistory2PS, name='AHistory2PS'),
    path('main/firstsemester/History2/AHistory2/AHistory2PS/AHistory2PAdd', views.AHistory2PAdd, name='AHistory2PAdd'),
    path('main/firstsemester/History2/AHistory2/AHistory2PS/AHistory2PM/<int:ExNo>/<int:semestery>', views.AHistory2PM, name='AHistory2PM'),
    path('main/firstsemester/History2/AHistory2/AHistory2PS/AHistory2P/<int:ExNo>/<int:semestery>', views.AHistory2P, name='AHistory2P'),

    
    
    
]