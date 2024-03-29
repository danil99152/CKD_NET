from pydantic import BaseModel, conint, confloat


class Analysis(BaseModel):
    priem: conint()
    debjut_v_vozraste: confloat()
    vozrast_gruppa_debjut: conint()
    dz: bool
    pol: conint()
    vozrast_gruppy: confloat()
    tr_v_den: conint()
    trpenia_debjut: conint()
    dlit_trpenii: conint()
    nv_v_den: conint()
    er_v_den: confloat()
    ley_v_den: confloat()
    kr_v_den: conint()
    kr_max: confloat()
    skf_v_den: confloat()
    skf_min: confloat()
    dlit_skf: conint()
    mochevina_v_den: confloat()
    mochevina_max: confloat()
    alt_v_den: confloat()
    alt_v_max: confloat()
    ast_v_den: confloat()
    ast_max: confloat()
    ldg_v_den: conint()
    ldg_max: conint()
    ob_v_den: confloat()
    soe_max: conint()
    soe_v_den: conint()
    srb_max: confloat()
    srb_v_den: confloat()
    c3_min: confloat()
    c4_min: confloat()
    gaptoglobin_min: confloat()
    cns: bool
    porazhenie_cns: bool
    porazhenie_serdca: bool
    echo_ks: conint()
    chls: conint()
    parenhima_pochek: conint()
    debjut_zabolevaniya: conint()
    gemokolit: bool
    diareya: conint()
    temperature: confloat()
    rvota: conint()
    ag: bool
    sad: conint()
    dad: conint()
    jkt: conint()
    pechen: conint()
    sut_belok_max: confloat()
    protenuria_dan: conint()
    gematury: conint()
    gematury_dney: conint()
    leykocituria: conint()
    leykuria_dney: conint()
    narushenie_mochespuskania: conint()
    olig_anuria_dney: conint()
    ekulizymab: conint()
    dlit_OPP: conint()
    peritonealny: bool
    gemodializ: bool
    giuk5: confloat()
    NT5VPlazme: confloat()
