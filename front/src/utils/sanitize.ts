import DOMPurify from "dompurify"

/**
 * Nettoie du HTML venant de l'API avant de l'afficher avec dangerouslySetInnerHTML.
 * DOMPurify garde la mise en forme (<p>, <strong>, <ul>...) mais retire tout ce qui
 * peut exécuter du JS : <script>, onerror=, onclick=, liens javascript:, etc.
 */
export const sanitizeHtml = (html: string | undefined | null): string => {
    return DOMPurify.sanitize(html ?? "")
}
